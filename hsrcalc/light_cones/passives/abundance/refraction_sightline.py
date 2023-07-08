"""Implements the Light Cone passive ability "Refraction of Sightline"'s logic.
"""

from ...models import PassiveLightCone


class RefractionSightline(PassiveLightCone):
    """The class for the Light Cone passive ability "Refraction of Sightline".

    Extends:
        PassiveLightCone
    """

    @property
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        return 'Refraction of Sightline'

    @property
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        return ("Increases the wearer's Effect RES by 16-32\% and increases "
                "Outgoing Healing by an amount that is equal to 33-45\% of "
                "Effect RES. Outgoing Healing can be increased this way by up "
                "to 15-27\%.")

    @property
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        return [
            (16, 33, 15),   # Superimposition I
            (20, 36, 18),   # Superimposition II
            (24, 39, 21),   # Superimposition III
            (28, 42, 24),   # Superimposition IV
            (32, 45, 27)    # Superimposition V
        ]

    def apply(self):
        """This method implements the Light Cone passive ability's buffs or
        debuffs.
        """
        pass
