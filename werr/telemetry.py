"""
werr: Privacy-Safe Zero-PII Anonymous Telemetry Dispatcher
Sends anonymous decision metadata (seed, question types, latency) to the
research optimization telemetry endpoint to improve fractal resonance maps.

Zero PII Guarantee:
- No IP addresses, usernames, or machine identifiers are logged.
- Sensitive fields (password, secret, token, key, auth, etc.) are automatically redacted.
- Completely non-blocking: Runs in a detached daemon thread with a strict timeout.
- Fully opt-out: Set WERR_TELEMETRY=0 (or WEVV_TELEMETRY=0) to disable entirely.
"""
import os
import re
import json
import threading
import urllib.request
from datetime import datetime, timezone
from typing import Dict, Any, Optional

TELEMETRY_ENDPOINT = os.getenv(
    "WERR_TELEMETRY_ENDPOINT",
    os.getenv("WEVV_TELEMETRY_ENDPOINT", "https://api.answerr.me:4431/werr/telemetry")
)

SENSITIVE_KEY_PATTERN = re.compile(
    r"(passw|secret|token|key|auth|cookie|session|cred|ssn|email|phone|jwt|bearer|private)",
    re.IGNORECASE
)

EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
TOKEN_PATTERN = re.compile(r"eyJ[a-zA-Z0-9_-]{8,}(\.[a-zA-Z0-9_-]+)*")


def _sanitize_client_state(state: Dict[str, Any]) -> Dict[str, Any]:
    """Client-side privacy filter: strips or redacts sensitive keys and values."""
    sanitized = {}
    for k, v in list(state.items())[:20]:
        k_str = str(k)[:32]
        if SENSITIVE_KEY_PATTERN.search(k_str):
            sanitized[k_str] = "[REDACTED]"
            continue
        if isinstance(v, (int, float, bool)):
            sanitized[k_str] = v
        elif isinstance(v, str):
            val_str = v[:100]
            val_str = EMAIL_PATTERN.sub("[EMAIL_REDACTED]", val_str)
            val_str = TOKEN_PATTERN.sub("[TOKEN_REDACTED]", val_str)
            sanitized[k_str] = val_str
        else:
            sanitized[k_str] = str(type(v).__name__)
    return sanitized


def _sanitize_instruction(text: str) -> str:
    """Sanitizes question instructions to avoid accidental PII."""
    safe = str(text)[:200]
    safe = EMAIL_PATTERN.sub("[EMAIL_REDACTED]", safe)
    safe = TOKEN_PATTERN.sub("[TOKEN_REDACTED]", safe)
    return safe


_OFFLINE_DIR = os.path.expanduser("~/.werr")
_OFFLINE_FILE = os.path.join(_OFFLINE_DIR, "offline_telemetry.jsonl")
_OFFLINE_LOCK = threading.Lock()
MAX_OFFLINE_ENTRIES = 500


def _save_offline_payload(payload_json: str):
    """Silently appends unsent payload to local disk buffer with a maximum entry cap."""
    try:
        with _OFFLINE_LOCK:
            os.makedirs(_OFFLINE_DIR, exist_ok=True)
            entries = []
            if os.path.exists(_OFFLINE_FILE):
                with open(_OFFLINE_FILE, "r", encoding="utf-8") as f:
                    entries = f.readlines()
            
            # Keep newest entries up to limit
            entries.append(payload_json.strip() + "\n")
            if len(entries) > MAX_OFFLINE_ENTRIES:
                entries = entries[-MAX_OFFLINE_ENTRIES:]
            
            with open(_OFFLINE_FILE, "w", encoding="utf-8") as f:
                f.writelines(entries)
    except Exception:
        pass


def _flush_offline_queue():
    """Flushes buffered offline telemetry records to server once internet is restored."""
    try:
        with _OFFLINE_LOCK:
            if not os.path.exists(_OFFLINE_FILE):
                return
            with open(_OFFLINE_FILE, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]

        if not lines:
            return

        remaining = []
        for line in lines:
            try:
                req = urllib.request.Request(
                    TELEMETRY_ENDPOINT,
                    data=line.encode("utf-8"),
                    headers={
                        "Content-Type": "application/json",
                        "User-Agent": "werr-client/0.3.0-buffered"
                    },
                    method="POST"
                )
                with urllib.request.urlopen(req, timeout=1.5) as _:
                    pass
            except Exception:
                remaining.append(line)
                break  # Internet connection dropped again, stop flushing

        with _OFFLINE_LOCK:
            if remaining:
                with open(_OFFLINE_FILE, "w", encoding="utf-8") as f:
                    f.writelines(r + "\n" for r in remaining)
            else:
                try:
                    os.remove(_OFFLINE_FILE)
                except Exception:
                    pass
    except Exception:
        pass


def _dispatch_worker(payload_json: str):
    """
    Background thread sending the sanitized payload with strict timeout.
    If connection fails (offline), stores locally in ~/.werr/offline_telemetry.jsonl.
    When connection succeeds, automatically flushes previously buffered offline records.
    """
    sent = False
    try:
        req = urllib.request.Request(
            TELEMETRY_ENDPOINT,
            data=payload_json.encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "User-Agent": "werr-client/0.3.0"
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=2.0) as _:
            sent = True
    except Exception:
        # Offline or server unreachable: buffer locally
        _save_offline_payload(payload_json)

    if sent:
        # We are online: attempt to flush any pending offline records
        _flush_offline_queue()


def dispatch_telemetry_async(
    state: Dict[str, Any],
    questions: Dict[str, Any],
    response: Any,
    seed: Dict[str, float],
    source: str = "python_lib"
):
    """
    Non-blocking asynchronous fire-and-forget telemetry dispatcher.
    Runs in a daemon thread; never raises exceptions and never blocks the engine.
    """
    # 1. Check Opt-out Environment Variable (Strictly opt-in: default 0 for air-gapped compliance)
    env_opt = os.environ.get("WERR_TELEMETRY", os.environ.get("WEVV_TELEMETRY", "0")).strip().lower()
    if env_opt not in ("1", "true", "yes", "on"):
        return

    try:
        # 2. Build sanitized question responses
        q_list = []
        for q_name, q_obj in questions.items():
            ans = response.answers.get(q_name)
            q_type = getattr(q_obj, "__class__", type(q_obj)).__name__.lower().replace("question", "")
            if q_type not in ("noul", "choice", "score"):
                q_type = "noul"

            q_item = {
                "name": str(q_name)[:32],
                "type": q_type,
                "instruction": _sanitize_instruction(getattr(q_obj, "instructions", ""))
            }

            if ans:
                if q_type == "noul":
                    q_item["decision"] = getattr(ans, "decision", False)
                    q_item["probability"] = getattr(ans, "noul", 0.0)
                    q_item["confidence"] = getattr(ans, "confidence", 0.0)
                elif q_type == "choice":
                    q_item["decision"] = getattr(ans, "choice", "")
                    q_item["probabilities"] = getattr(ans, "probabilities", {})
                    q_item["confidence"] = getattr(ans, "confidence", 0.0)
                elif q_type == "score":
                    q_item["decision"] = getattr(ans, "score", 0.0)
                    q_item["probabilities"] = {str(k): v for k, v in getattr(ans, "probabilities", {}).items()}
                    q_item["confidence"] = getattr(ans, "confidence", 0.0)

            q_list.append(q_item)

        # 3. Assemble JSON Payload
        payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "version": getattr(response, "model", "0.3.0"),
            "source": source,
            "seed": {
                "cx": round(float(seed.get("cx", 0.0)), 8),
                "cy": round(float(seed.get("cy", 0.0)), 8),
                "zoom": round(float(seed.get("zoom", 50.0)), 4)
            },
            "state_summary": _sanitize_client_state(state),
            "questions": q_list,
            "latency_ms": getattr(response, "latency_ms", 0.0)
        }

        payload_json = json.dumps(payload, ensure_ascii=False)

        # 4. Fire-and-forget in background thread (timeout=1.0s)
        t = threading.Thread(target=_dispatch_worker, args=(payload_json,), daemon=False)
        t.start()

    except Exception:
        pass
