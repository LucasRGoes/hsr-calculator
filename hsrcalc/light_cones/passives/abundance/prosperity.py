"""Implements the Light Cone passive ability "Prosperity"'s logic.
"""

from ...models import PassiveLightCone


class Prosperity(PassiveLightCone):
    """The class for the Light Cone passive ability "Prosperity".

    Extends:
        PassiveLightCone
    """

    @property
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        return 'Prosperity'

    @property
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        return ("When the wearer uses their Skill or Ultimate, their Outgoing "
                "Healing increases by 12-24\%.")

    @property
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        return [
            (12,),  # Superimposition I
            (15,),  # Superimposition II
            (18,),  # Superimposition III
            (21,),  # Superimposition IV
            (24,)   # Superimposition V
        ]

    def apply(self):
        """This method implements the Light Cone passive ability's buffs or
        debuffs.
        """
        pass
