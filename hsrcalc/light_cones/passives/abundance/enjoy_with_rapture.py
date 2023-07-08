"""Implements the Light Cone passive ability "Enjoy With Rapture"'s logic.
"""

from ...models import PassiveLightCone


class EnjoyWithRapture(PassiveLightCone):
    """The class for the Light Cone passive ability "Enjoy With Rapture".

    Extends:
        PassiveLightCone
    """

    @property
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        return 'Enjoy With Rapture'

    @property
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        return ("At the start of the wearer's turn, regenerates 8-16 Energy "
                "for a randomly chosen ally (excluding the wearer) whose "
                "current Energy is lower than 50\%.")

    @property
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        return [
            (8,),   # Superimposition I
            (10,),  # Superimposition II
            (12,),  # Superimposition III
            (14,),  # Superimposition IV
            (16,)   # Superimposition V
        ]

    def apply(self):
        """This method implements the Light Cone passive ability's buffs or
        debuffs.
        """
        pass
