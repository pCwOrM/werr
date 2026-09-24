import sys
import os

print("--- Testing maat-seed configuration ---")
sys.path.insert(0, "/home/pcworm/maat_seed")
sys.path.insert(0, "/home/pcworm/werr")
import maat_seed
r_maat = maat_seed.DEFAULT_ROUTER
print(f"maat: mode={r_maat.mode} domain_mode={r_maat.domain_mode} tripod={r_maat.tripod} res={r_maat.resolution} max_iter={r_maat.max_iter}")

assert r_maat.mode == "pure_fractal", f"Expected pure_fractal, got {r_maat.mode}"
assert r_maat.domain_mode == "none", f"Expected none, got {r_maat.domain_mode}"
assert r_maat.tripod is True, f"Expected tripod=True, got {r_maat.tripod}"
assert r_maat.resolution == 36, f"Expected 36, got {r_maat.resolution}"
assert r_maat.max_iter == 36, f"Expected 36, got {r_maat.max_iter}"

print("--- Testing answerr-api configuration ---")
sys.path.insert(0, "/opt/apps/answerr/api")
import server
r_answerr = server.DEFAULT_ROUTER
print(f"answerr: mode={r_answerr.mode} domain_mode={r_answerr.domain_mode} tripod={r_answerr.tripod} res={r_answerr.resolution} max_iter={r_answerr.max_iter}")

assert r_answerr.mode in ["lexical", "production"], f"Expected lexical, got {r_answerr.mode}"
assert r_answerr.domain_mode == "multi", f"Expected multi, got {r_answerr.domain_mode}"
assert r_answerr.tripod is True, f"Expected tripod=True, got {r_answerr.tripod}"
assert r_answerr.resolution == 36, f"Expected 36, got {r_answerr.resolution}"
assert r_answerr.max_iter == 36, f"Expected 36, got {r_answerr.max_iter}"

print("ALL_SYSTEM_CONFIGURATIONS_VERIFIED_SUCCESS")
