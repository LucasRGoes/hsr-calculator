"""Implements the Light Cone passive ability "Tiny Light"'s logic.
"""

from ...models import PassiveLightCone


def TinyLight(PassiveLightCone):
	"""The class for the Light Cone passive ability "Tiny Light".

	Extends:
		PassiveLightCone
	"""

    @property
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        return 'Tiny Light'

    @property
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        return ("Increases the wearer's Max HP by 16-32\%. When using Basic "
                "ATK or Skill, restores all allies' HP by an amount equal to "
                "2.0-4.0\% of their respective Max HP.")

    @property
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        return [
            (16, 2),    # Superimposition I
            (20, 2.5),  # Superimposition II
            (24, 3),    # Superimposition III
            (28, 3.5),  # Superimposition IV
            (32, 4)     # Superimposition V
        ]

    def apply(self):
        """This method implements the Light Cone passive ability's buffs or
        debuffs.
        """
        pass
