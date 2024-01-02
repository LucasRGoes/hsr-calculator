"""The terminology module holds information of generic usage between HSR's
aspects.
"""

from enum import Enum, auto


class Element(Enum):
    """Represents HSR's elements.

    Extends:
        Enum
    """
    FIRE = auto()
    ICE = auto()
    IMAGINARY = auto()
    LIGHTNING = auto()
    PHYSICAL = auto()
    QUANTUM = auto()
    WIND = auto()


class Path(Enum):
    """Represents HSR's paths.

    Extends:
        Enum
    """
    ABUNDANCE = auto()
    DESTRUCTION = auto()
    ERUDITION = auto()
    HARMONY = auto()
    NIHILITY = auto()
    PRESERVATION = auto()
    THE_HUNT = auto()


class Rarity(Enum):
    """Represents HSR's rarities.

    Extends:
        Enum
    """
    THREE_STARS = auto()
    FOUR_STARS = auto()
    FIVE_STARS = auto()
