from textwrap import dedent

import rooms

import signal

def introduction() :

	print("""

You've been chased by ugly orcs accross the Middle Earth. Your only escape was this strange dark temple located near the south of the mountains.

You decided to enter.

The door closed suddenly just after you crossed the treshold.

You need to find a way out.


To win this game, you must kill all the creatures that live here or find an escape.

Type either the name of the option or its number to make a decision.

You have 10 minutes to complete the game.

		""")

LIFE_HERO = 100

LIFE_MONSTER = 110

STRIKE_HERO = 10

STRIKE_MONSTER = 20

LIFE_SECOND_DEMON = 240

STRIKE_SECOND_DEMON = 35

LIFE_THIRD_DEMON = 300

STRIKE_THIRD_DEMON = 50

LIFE_BOSS = 400

STRIKE_BOSS = 85

Map = rooms.Map(LIFE_HERO, LIFE_MONSTER, STRIKE_HERO, STRIKE_MONSTER, LIFE_SECOND_DEMON, STRIKE_SECOND_DEMON, LIFE_THIRD_DEMON, STRIKE_THIRD_DEMON, LIFE_BOSS, STRIKE_BOSS)

next_room_string = "entrance"

def handler(signum, frame):

	raise Exception

signal.signal(signal.SIGALRM, handler)

signal.alarm(120)

iterator = 0

minutes_left = [8, 6, 4, 2]

introduction()

while(True) :

	try : 

		if next_room_string == "entrance":

			next_room_string = Map.entrance.play(Map.hero)

		elif (next_room_string == "left1" ):

			if (Map.monster.life > 0 ):

				next_room_string = Map.left1.play(Map.monster,Map.hero)

			else:

				print("You've already killed the first demon.")

				next_room_string = "entrance"

		elif next_room_string == "equipment":

			print(f"Your striking power : {Map.hero.strikeHero}")

			print(f"Your weapon : {Map.hero.weapon}")

			print(f"Your armor : {Map.hero.armor} ({Map.hero.resistance})")

			if Map.hero.key == True :

				print("You have a key.")

			if Map.hero.big_key == True :

				print("You have a big key.")

			next_room_string = "entrance"

		elif next_room_string == "right1" :

			if Map.hero.has_basic_sword == False:

				next_room_string = Map.right1.play(Map.hero)

			else:

				print("You already have the first sword\n")

				next_room_string = "entrance"

		elif next_room_string == "center1":

			if Map.second_demon.life > 0:

				next_room_string = Map.center1.play(Map.second_demon, Map.hero)

			else:

				print("You've already killed the second demon.")

				next_room_string = "entrance"

		elif next_room_string == "stairs":

			next_room_string = Map.upstairs.play(Map.hero)

		elif next_room_string == "left2":

			if Map.third_demon.life > 0 :

				next_room_string = Map.left2.play(Map.third_demon, Map.hero)

			else:

				print("You've already killed the third demon.")

				next_room_string = "stairs"

		elif next_room_string == "right2":

			if Map.hero.has_great_sword == True :

				print("You already have the Great sword.")

				next_room_string = "stairs"

			else :

				next_room_string = Map.right2.play(Map.hero)

		elif next_room_string == "center2":

			next_room_string = Map.center2.play(Map.boss, Map.hero)

		elif next_room_string == "basement" :

			next_room_string = Map.basement.play(Map.hero)

		elif next_room_string == "door" :

			next_room_string = Map.door.play(Map.hero)

		else :

			next_room_string = Map.entrance.play(Map.hero)

	except Exception:

		if iterator <= 2 :

			print(f"You have {minutes_left[iterator]} minutes left.")

			iterator += 1

			signal.alarm(120)

		elif iterator == 3 :

			print("You have 2 minutes left.")

			iterator += 1

			signal.alarm(60)

		elif iterator == 4 :

			print("You have 1 minutes left.")

			iterator += 1

			signal.alarm(30)

		elif iterator == 5 :

			print("You have 30 secondes left.")

			iterator += 1

			signal.alarm(20)

		elif iterator == 6 :

			print("You have 10 secondes left.")

			iterator += 1

			signal.alarm(10)

		else :

			print("Time out! You lose!")

			exit(0)





































