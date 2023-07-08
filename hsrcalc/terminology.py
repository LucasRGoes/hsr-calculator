"""The terminology module holds information for pre-determined variables of
HSR.
"""

from enum import Enum


class Path(Enum):
    """Represents HSR's paths.

    Extends:
        Enum
    """
    DESTRUCTION = 1
    HUNT = 2
    ERUDITION = 3
    HARMONY = 4
    NIHILITY = 5
    PRESERVATION = 6
    ABUNDANCE = 7
