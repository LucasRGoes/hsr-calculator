"""Implements the Light Cone passive ability "Savor"'s logic.
"""

from ...models import PassiveLightCone


def Savor(PassiveLightCone):
	"""The class for the Light Cone passive ability "Savor".

	Extends:
		PassiveLightCone
	"""

    @property
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        return 'Savor'

    @property
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        return ("At the start of the battle, immediately regenerate 6-12 "
                "Energy for all allies. ")

    @property
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        return [
            (6,),   # Superimposition I
            (7,),   # Superimposition II
            (9,),   # Superimposition III
            (11,),  # Superimposition IV
            (12,)   # Superimposition V
        ]

    def apply(self):
        """This method implements the Light Cone passive ability's buffs or
        debuffs.
        """
        pass
