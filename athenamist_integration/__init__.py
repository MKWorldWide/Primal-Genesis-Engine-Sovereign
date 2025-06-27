"""
AthenaMist-Blended Integration Package
=====================================

This package provides comprehensive integration modules for:
- AI Integration (Multiple AI providers)
- LilithOSi Integration (iOS firmware development)
- Phantom Integration (Security scanning and reconnaissance)
- Primal Sovereign Core Integration (Voice processing and AWS optimization)

Author: AthenaMist-Blended Team
Version: 2.0
License: MIT
"""

from .ai_integration import AIIntegrationManager
from .lilithos_integration import LilithOSiManager
from .phantom_integration import PhantomManager
from .primal_sovereign_integration import PrimalSovereignManager, VoiceCommandType, ProcessingStatus

__all__ = [
    'AIIntegrationManager',
    'LilithOSiManager', 
    'PhantomManager',
    'PrimalSovereignManager',
    'VoiceCommandType',
    'ProcessingStatus'
]

__version__ = "2.0"
__author__ = "AthenaMist-Blended Team" 