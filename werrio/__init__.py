"""
WERRIO: Official PyPI distribution of the WERR Zero-Memory Decision Engine (werr.io).
Provides direct access to all core modules of `werr`.
"""
from werr import *
try:
    from werr.engine import WerrEngine
except ImportError:
    pass

__version__ = "0.5.1"
__all__ = ["WerrEngine", "__version__"]
