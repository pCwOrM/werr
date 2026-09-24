import sys
import os

if __name__ == "__main__":
    from werr import __version__
    if len(sys.argv) > 1 and sys.argv[1] in ("--version", "-v", "version"):
        print(f"werr {__version__} (0-VRAM Fractal System-One Decision Engine)")
        sys.exit(0)
    if len(sys.argv) > 1 and sys.argv[1] in ("--help", "-h"):
        print("werr: Zero-Memory Fractal System-One Decision Engine (Waves & Errors)")
        print("Usage:")
        print("  werr                 # Start interactive decision CLI (sor.py)")
        print("  werr admin           # Evaluate admin role scenario")
        print("  werr attacker        # Evaluate attacker/bot scenario")
        print("  werr --version       # Show version")
        print("  werr --help          # Show this help")
        sys.exit(0)

    sor_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sor.py")
    if os.path.exists(sor_path):
        import runpy
        runpy.run_path(sor_path, run_name="__main__")
    else:
        print(f"werr v{__version__} - Zero-Memory Decision Engine")
