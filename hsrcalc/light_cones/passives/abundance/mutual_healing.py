"""Implements the Light Cone passive ability "Mutual Healing"'s logic.
"""

from ...models import PassiveLightCone


class MutualHealing(PassiveLightCone):
    """The class for the Light Cone passive ability "Mutual Healing".

    Extends:
        PassiveLightCone
    """

    @property
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        return 'Mutual Healing'

    @property
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        return ("Increases the wearer's Energy Regeneration Rate by 8-16\% "
                "and increases Outgoing Healing when they use their Ultimate "
                "by 12-24\%.")

    @property
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        return [
            (8, 12),    # Superimposition I
            (10, 15),   # Superimposition II
            (12, 18),   # Superimposition III
            (14, 21),   # Superimposition IV
            (16, 24)    # Superimposition V
        ]

    def apply(self):
        """This method implements the Light Cone passive ability's buffs or
        debuffs.
        """
        pass
