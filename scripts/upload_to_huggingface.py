#!/usr/bin/env python3
"""
Automated Hugging Face Hub Dataset Publisher for WERR Open Decisions
Publishes werr_open_decisions.jsonl and its Dataset Card (README.md)
to Hugging Face Datasets Hub via huggingface_hub Python API.
"""

import os
import sys
from huggingface_hub import HfApi, login

def upload_dataset(token=None, repo_name="werr_open_decisions"):
    token = token or os.environ.get("HF_TOKEN")
    if not token:
        token_path = os.path.expanduser("~/.cache/huggingface/token")
        if os.path.exists(token_path):
            with open(token_path, "r", encoding="utf-8") as f:
                token = f.read().strip()

    if not token:
        print("ERROR: No Hugging Face access token found!")
        print("Please supply your HF write token via:")
        print("  1. python scripts/upload_to_huggingface.py hf_yourTokenHere")
        print("  2. set HF_TOKEN=hf_yourTokenHere")
        print("Get your token from: https://huggingface.co/settings/tokens (Write permission)")
        sys.exit(1)

    print("Authenticating with Hugging Face Hub...")
    api = HfApi(token=token)
    user_info = api.whoami()
    username = user_info["name"]
    print(f"Authenticated as Hugging Face user: {username}")

    full_repo_id = f"{username}/{repo_name}"
    print(f"Target dataset repository: {full_repo_id}")

    # 1. Create dataset repository if not existing
    print(f"Ensuring repository '{full_repo_id}' exists...")
    api.create_repo(
        repo_id=full_repo_id,
        repo_type="dataset",
        exist_ok=True,
        private=False
    )
    print(f"Repository ready: https://huggingface.co/datasets/{full_repo_id}")

    # 2. Upload dataset files
    dataset_dir = os.path.join(os.path.dirname(__file__), "..", "dataset")
    jsonl_path = os.path.abspath(os.path.join(dataset_dir, "werr_open_decisions.jsonl"))
    readme_path = os.path.abspath(os.path.join(dataset_dir, "README.md"))

    print(f"Uploading README.md (Dataset Card)...")
    api.upload_file(
        path_or_fileobj=readme_path,
        path_in_repo="README.md",
        repo_id=full_repo_id,
        repo_type="dataset"
    )

    print(f"Uploading werr_open_decisions.jsonl ({os.path.getsize(jsonl_path) / (1024*1024):.2f} MB)...")
    api.upload_file(
        path_or_fileobj=jsonl_path,
        path_in_repo="werr_open_decisions.jsonl",
        repo_id=full_repo_id,
        repo_type="dataset"
    )

    print("\n" + "=" * 60)
    print(f"SUCCESS! Dataset published to Hugging Face Hub:")
    print(f"URL: https://huggingface.co/datasets/{full_repo_id}")
    print("=" * 60)
    print("\nUsers can now load this dataset with one line:")
    print(f"  from datasets import load_dataset")
    print(f"  dataset = load_dataset('{full_repo_id}')")
    print("=" * 60)

if __name__ == "__main__":
    cli_token = sys.argv[1] if len(sys.argv) > 1 else None
    upload_dataset(token=cli_token)
