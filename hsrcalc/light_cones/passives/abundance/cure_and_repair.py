"""Implements the Light Cone passive ability "Cure and Repair"'s logic.
"""

from ...models import PassiveLightCone


class CureAndRepair(PassiveLightCone):
    """The class for the Light Cone passive ability "Cure and Repair".

    Extends:
        PassiveLightCone
    """

    @property
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        return 'Cure and Repair'

    @property
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        return ("Increases the wearer's Outgoing Healing by 10-20\%. When "
                "using Skill, regenerates 2-4 Energy for all allies.")

    @property
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        return [
            (10, 2),        # Superimposition I
            (12.5, 2.5),    # Superimposition II
            (15, 3),        # Superimposition III
            (17.5, 3.5),    # Superimposition IV
            (20, 4)         # Superimposition V
        ]

    def apply(self):
        """This method implements the Light Cone passive ability's buffs or
        debuffs.
        """
        pass
