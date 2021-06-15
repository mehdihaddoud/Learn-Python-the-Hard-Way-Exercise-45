
class Character(object):

	def __init__(self, life) :

		self.life = life

		isDead = False

class Hero(Character) :
	
	def __init__(self,life, strikeHero) :

		super().__init__(life)

		self.strikeHero = strikeHero

		self.weapon = "Bare hands"

		self.resistance = 5

		self.armor = "No armor"

		self.key = False

		self.big_key = False

		self.has_basic_sword = False

		self.has_great_sword = False


class Monster(Character):

	def __init__(self, life, strike):

		super().__init__(life)

		self.strike = strike
