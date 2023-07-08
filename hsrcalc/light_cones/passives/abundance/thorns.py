"""Implements the Light Cone passive ability "Thorns"'s logic.
"""

from ...models import PassiveLightCone


class Thorns(PassiveLightCone):
    """The class for the Light Cone passive ability "Thorns".

    Extends:
        PassiveLightCone
    """

    @property
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        return 'Thorns'

    @property
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        return ("Increases the wearer's ATK by 24-40\%. After the wearer uses "
                "an attack, for each different enemy target the wearer hits, "
                "regenerates 3-5 Energy. Each attack can regenerate Energy up "
                "to 3 time(s) this way. After the wearer uses their Ultimate, "
                "all allies gain 12-20 SPD for 1 turn.")

    @property
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        return [
            (24, 3, 12),    # Superimposition I
            (28, 3.5, 14),  # Superimposition II
            (32, 4, 16),    # Superimposition III
            (36, 4.5, 18),  # Superimposition IV
            (40, 5, 20)     # Superimposition V
        ]

    def apply(self):
        """This method implements the Light Cone passive ability's buffs or
        debuffs.
        """
        pass
