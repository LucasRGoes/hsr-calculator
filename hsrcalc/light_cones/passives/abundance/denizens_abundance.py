"""Implements the Light Cone passive ability "Denizens of Abundance"'s logic.
"""

from ...models import PassiveLightCone


class DenizensAbundance(PassiveLightCone):
    """The class for the Light Cone passive ability "Denizens of Abundance".

    Extends:
        PassiveLightCone
    """

    @property
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        return 'Denizens of Abundance'

    @property
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        return ("After the wearer uses their Basic ATK, their next action "
                "will be Advanced Forward by 12-20\%.")

    @property
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        return [
            (12,),  # Superimposition I
            (14,),  # Superimposition II
            (16,),  # Superimposition III
            (18,),  # Superimposition IV
            (20,)   # Superimposition V
        ]

    def apply(self):
        """This method implements the Light Cone passive ability's buffs or
        debuffs.
        """
        pass
