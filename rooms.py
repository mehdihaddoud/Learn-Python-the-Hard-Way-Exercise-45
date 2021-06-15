from textwrap import dedent

import random

import time

import characters

password = random.randint(100,999)

def endFight(hero, monster) :

	if (hero.life <= 0 or monster.life <= 0):

		if (hero.life <= 0):

			hero.isDead = True

		else:

			monster.isDead = True

		return True

	else:

		return False

class Room(object):

	def __init__(self):

		self.first = True


class Entrance(Room) :

	def play(self, hero):

		if self.first == True :

			self.first = False

			print("This is the main entrance. You can either cross the doors on the left, right or center or you can take the stairs. You can also check your equipment.")

		print(f"Your life : {hero.life}")

		print(dedent("""

			Room : Entrance

			Choose an option.

			1 - Left

			2 - Center

			3 - Right

			4 - Stairs

			5 - Equipment

		"""))


		choice = True

		while (choice) :

			decision = input("> ")

			if ("eft" in decision or "1" in decision):

				choice = False

				return "left1"

			elif ("enter" in decision or "2" in decision):

				choice = False

				return "center1"

			elif("ight" in decision or "3" in decision):

				choice = False

				return "right1"

			elif("tairs" in decision or "4" in decision):

				choice = False

				return "stairs"

			elif("quipment" in decision or "5" in decision):

				choice = False

				return "equipment"

			else :

				print("Not an option, retry please.")



class Left1(Room) :

	def play(self, monster, hero):

		if (self.first == True):

			print("You've met the first demon. Make sure to be sufficiently equipped to kill it.\n")

			self.first = False

		print("Room : First demon")

		print(f"Your life : {hero.life}")

		print(f"First demon's life : {monster.life}")

		print(dedent("""

			Strike or leave this room.

			1 - Leave

			2 - Strike

			"""))

		choice = True


		while choice :

			decision = input("> ")


			if ("eave" in decision or "1" in decision):

				choice = False

				return "entrance"

			elif ("trike" in decision or "2" in decision):

				monster.life -= hero.strikeHero

				hero.life -= monster.strike

				hero.life += hero.resistance

				if (endFight(monster,hero) == True):

					choice = False

					if (hero.life <= 0):

						print("You've been killed! You lose!")

						exit(0)


					else :

						print("You've killed the first demon and your life is upgraded to 200 extra points.")

						print("You've also found the steel armor which upgrades your resistance to 10 extra points")

						hero.life += 200

						hero.resistance += 10

						hero.armor = "Steel Armor"


					return "entrance"


				else:

					print(f"Your life : {hero.life} ")

					print(f"First demon's life : {monster.life}")

					print("\nKeep choosing!\n")

			else:

				print("Not a command, retry.")

class Right1(object):

	def play(self, hero) :

		print("Room : First Sword\n")

		print("You have acquired the basic sword. This sword boost your striking power to 25 more points\n")

		hero.strikeHero += 25

		print(f"Your striking power is now : {hero.strikeHero}\n")

		hero.weapon = "Basic sword"

		hero.has_basic_sword = True

		return "entrance"

class Center1(Room) :

	def play(self, monster, hero):

		if self.first == True :

			print("This is the second demon. It is stronger than the first demon.")

			self.first = False

		print("Room : Second demon")

		print(f"Your life : {hero.life}")

		print(f"Second demon's life : {monster.life}")

		print(dedent("""

			Strike or leave this room.

			1 - Leave

			2 - Strike

			"""))

		choice = True


		while choice :

			decision = input("> ")


			if ("eave" in decision or "1" in decision):

				choice = False

				return "entrance"

			elif ("trike" in decision or "2" in decision):

				monster.life -= hero.strikeHero

				hero.life -= monster.strike

				hero.life += hero.resistance

				if (endFight(monster,hero) == True):

					choice = False

					if (hero.life <= 0):

						print("You've been killed! You lose!")

						exit(0)


					else :

						print("You've killed the second demon and your life is upgraded to 200 extra points.\n")

						hero.life += 200

						print("You've also found the gold armor which upgrades your resistance to 15 extra points\n")

						hero.armor = "Gold armor"

						hero.resistance += 15

						print("You've also found a key.")

						hero.key = True


					return "entrance"


				else:

					print(f"Your life : {hero.life} ")

					print(f"Second demon's life : {monster.life}")

					print("\nKeep choosing!\n")

			else:

				print("Not a command, retry.")

class Upstairs(Room):

	def play(self, hero):

		if self.first == True :

			print(dedent("""This is the room upstairs. You can either come back to the main entrance, take the left door, right door or take the big door in the center.
There are also stairs that take you to the basement.
				"""))

			self.first = False


		print(f"Your life : {hero.life}")

		print(dedent("""

			Room : Upstairs

			Choose an option.

			1 - Entrance

			2 - Left

			3 - Center

			4 - Right

			5 - Basement

		"""))


		choice = True

		while (choice) :

			decision = input("> ")

			if ("ntrance" in decision or "1" in decision):

				choice = False

				return "entrance"

			elif ("eft" in decision or "2" in decision):

				choice = False

				return "left2"

			elif("enter" in decision or "3" in decision):

				choice = False

				return "center2"

			elif("ight" in decision or "4" in decision):

				choice = False

				return "right2"

			elif("asement" in decision or "5" in decision):

				choice = False

				return "basement"

			else :

				print("Not an option, retry.")

class Left2(Room) :

	def play(self, monster, hero):

		if self.first == True :

			print("This is the last demon. It is the strongest of all.")

			self.first = False

		print("Room : Third demon")

		print(f"Your life : {hero.life}")

		print(f"Third demon's life : {monster.life}")

		print(dedent("""

			Strike or leave this room.

			1 - Leave

			2 - Strike

			"""))

		choice = True


		while choice :

			decision = input("> ")


			if ("eave" in decision or "1" in decision):

				choice = False

				return "stairs"

			elif ("trike" in decision or "2" in decision):

				monster.life -= hero.strikeHero

				hero.life -= monster.strike

				hero.life += hero.resistance

				if (endFight(monster,hero) == True):

					choice = False

					if (hero.life <= 0):

						print("You've been killed! You lose!")

						exit(0)


					else :

						print("You've killed the third demon and your life is upgraded to 200 extra points.")

						hero.life += 200

						print("You've found the platinium armor which upgrades your resistance to 20 extra points")

						hero.armor = "Platinium"

						hero.resistance += 20

						print("You've also found a big key.")

						hero.big_key = True

						print("Now that you have the big key, You can take the big door in the center upstairs and kill the master of this dark temple.")


					return "stairs"


				else:

					print(f"Your life : {hero.life} ")

					print(f"Third demon's life : {monster.life}")

					print("\nKeep choosing!\n")

			else:

				print("Not a command, retry.")

class Right2(object):

	def play(self,hero):

		if hero.key == True:

			print("Room : Great Sword\n")

			print("You have acquired the great sword. This sword boosts your striking power to 30 more points\n")

			hero.strikeHero += 30

			print(f"Your striking power is now : {hero.strikeHero}\n")

			hero.weapon = "Great sword"

			hero.has_great_sword = True

			return "stairs"

		else:

			print("You don't have the key to open this door.")

			return "stairs"

class Center2(Room) :

	def play(self,monster, hero):

		if (hero.big_key == True):

			if (self.first == True) :

				print("This is the boss of the game. Kill it to win the game.")

				self.first = False

			print("Room : Boss")

			print(f"Your life : {hero.life}")

			print(f"Boss life : {monster.life}")

			print(dedent("""

				Strike or leave this room.

				1 - Leave

				2 - Strike

				"""))

			choice = True


			while choice :

				decision = input("> ")


				if ("eave" in decision or "1" in decision):

					choice = False

					return "stairs"

				elif ("trike" in decision or "2" in decision):

					monster.life -= hero.strikeHero

					hero.life -= monster.strike

					hero.life += hero.resistance

					if (endFight(monster,hero) == True):

						choice = False

						if (hero.life <= 0):

							print("You've been killed! You lose!")

							exit(0)


						else :

							print("You've killed the Boss and won the game!")

							exit(0)


						return "stairs"


					else:

						print(f"Your life : {hero.life} ")

						print(f"Boss life : {monster.life}")

						print("\nKeep choosing!\n")

				else:

					print("Not a command, retry.")

		else:

			print("You don't have the key to open this door.")

			return "stairs"

class Basement(Room):

	def play(self, hero):

		if self.first == True :

			print("""This is the basement. You've seen a giant crack that leads to the outside but jumping it is risky. Try to jump it if you dare.
There is also another door that leads to the outside but it is locked by a 3 digits passcode. Try to find the combination if you don't want to kill
all the monsters here.\n""")

			self.first = False

		print(f"Your life : {hero.life}")

		print(dedent("""

			Room : Basement

			Choose an option.

			1 - Stairs

			2 - Jump

			3 - Password

			4 - Door

		"""))


		choice = True

		while (choice) :

			decision = input("> ")

			if ("tairs" in decision or "1" in decision):

				choice = False

				return "stairs"

			elif ("ump" in decision or "2" in decision):

				choice = False

				print("You might fall off and die. Are you sure you want to jump? (type \"yes\" or \"no\")")

				OK = False

				while(OK == False):

					decision = input("> ")

					if(decision == "yes" or decision == "Yes"):

						OK = True

						print("You are going to jump ...")

						result = random.randint(1,4)

						time.sleep(2)

						if (result == 1):

							print("You've jumped across the crack! You win!")

							exit(0)

						else:

							print("You've fallen off the crack! You lose!")

							exit(0)

					elif (decision == "No" or decision == "no" ):

						OK = True

						return "basement"

					else:

						print("Not an option, retry.")


			elif("assword" in decision or "3" in decision):

				print("Enter the 3 digits password or type \"quit\" to return to the basement.")

				#print(f"The password is : {password}")

				attempt = input("> ")

				while (attempt != "quit"):

					#print(f"The password is : {password}")

					if attempt == str(password) :

						print("You win!")

						exit(0)

					else:

						print("Bad combination. Retry.")

						attempt = input("> ")

				return "basement"

			elif("oor" in decision or "4" in decision):

				choice = False

				return "door"

			else :

				print("Not an option, retry.")


class Door(object):

	def __init__(self) :

		self.isFound = False


	def play(self, hero):

		if self.isFound == False:

			self.isFound = True

			print("You've found a health kit. Your life is upgraded to 100 extra points.")

			hero.life += 100

			return "basement"

		else :

			print("You've already found the health kit.")

			return "basement"

class Map(object):

	def __init__(self,LIFE_HERO,LIFE_MONSTER,STRIKE_HERO,STRIKE_MONSTER,LIFE_SECOND_DEMON, STRIKE_SECOND_DEMON, LIFE_THIRD_DEMON, STRIKE_THIRD_DEMON, LIFE_BOSS, STRIKE_BOSS):

		self.hero = characters.Hero(LIFE_HERO,STRIKE_HERO)

		self.monster = characters.Monster(LIFE_MONSTER, STRIKE_MONSTER)

		self.second_demon = characters.Monster(LIFE_SECOND_DEMON, STRIKE_SECOND_DEMON)

		self.third_demon = characters.Monster(LIFE_THIRD_DEMON, STRIKE_THIRD_DEMON)

		self.boss = characters.Monster(LIFE_BOSS, STRIKE_BOSS)

		self.left1 = Left1()

		self.left2 = Left2()

		self.entrance = Entrance()

		self.right1 = Right1()

		self.right2 = Right2()

		self.center1 = Center1()

		self.center2 = Center2()

		self.upstairs = Upstairs()

		self.basement = Basement()

		self.door = Door()
