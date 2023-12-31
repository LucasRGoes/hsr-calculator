"""The terminology module holds information for pre-determined variables of
HSR.
"""

from enum import Enum


class Element(Enum):
    """Represents HSR's elements.

    Extends:
        Enum
    """
    FIRE = 1
    ICE = 2
    IMAGINARY = 3
    LIGHTNING = 4
    PHYSICAL = 5
    QUANTUM = 6
    WIND = 7


class Path(Enum):
    """Represents HSR's paths.

    Extends:
        Enum
    """
    ABUNDANCE = 1
    DESTRUCTION = 2
    ERUDITION = 3
    HARMONY = 4
    NIHILITY = 5
    PRESERVATION = 6
    THE_HUNT = 7


class Rarity(Enum):
    """Represents HSR's rarities.

    Extends:
        Enum
    """
    THREE_STARS = 1
    FOUR_STARS = 2
    FIVE_STARS = 3
