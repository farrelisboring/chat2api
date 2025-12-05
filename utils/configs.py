"""Compatibility shim for configuration imports.

Historically modules imported settings from ``utils.configs``. The primary
configuration module is :mod:`utils.config`, so this shim re-exports its
symbols to avoid import errors without duplicating logic.
"""
from utils.config import *  # noqa: F401,F403
