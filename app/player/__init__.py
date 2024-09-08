__version__ = "0.1.0"
__author__ = "MrCode200", "Kian19955"

from .playerTemplate import Player
from .playerMovement import moving
from .playerEngine import player_list

__all__ = ["Player", "moving", "player_list"]