#!/usr/bin/python
import random

# define statistics values
STATS = {
	"STR" : random.randint(6,20),
	"DEX" : random.randint(6,20),
	"CON" : random.randint(6,20),
	"INT" : random.randint(6,20),
	"WIS" : random.randint(6,20),
	"CHA" : random.randint(6,20),
}
def stats():
	mod = 0
	print '-' * 40
        print("Stat \t\tScore \t\tModifier")
        for key, val in STATS.items():
		if val==22 or val==23:
			mod=6
                elif val==20 or val==21:
                        mod=5
                elif val==18 or val==19:
                        mod=4
                elif val==16 or val==17:
                        mod=3
                elif val==14 or val==15:
                        mod=2
                elif val==12 or val==13:
                        mod=1
                elif val==10 or val==11:
                        mod=0
                elif val==8 or val==9:
                        mod=(0-1)
                elif val==6 or val==7:
                        mod=(0-2)
                print("%s \t\t%i \t\t%i") % (key, val, mod)

# define races
RACE = ["DWARF", "ELF", "HALFLING", "HUMAN", "DRAGONBORN", "GNOME", "HALF-ELF", "HALF-ORC", "TIEFLING"]
def dwarf():
	STATS['CON'] += 2
def elf():
	STATS['DEX'] += 2
def halfling():
	STATS['DEX'] += 2
def human():
	STATS['STR'] += 1
	STATS['DEX'] += 1
	STATS['CON'] += 1
	STATS['INT'] += 1
	STATS['WIS'] += 1
	STATS['CHA'] += 1
def dragonborn():
	STATS['STR'] += 2
	STATS['CHA'] += 1
def gnome():
	STATS['INT'] += 2
def halfelf():
	while True:
		choice1 = raw_input("Choose a stat to increase by 1: ").upper()
		choice2 = raw_input("Choose another stat to increase by 1: ").upper()
		print '-' * 40
		if choice1 == "STR":
			STATS['STR'] += 1
		elif choice1 == "DEX":
                	STATS['DEX'] += 1
		elif choice1 == "CON":
			STATS['CON'] += 1
		elif choice1 == "INT":
			STATS['INT'] += 1
		elif choice1 == "WIS":
			STATS['WIS'] += 1
		elif choice1 == "CHA":
			STATS['CHA'] += 1
		else:
			print("Invalid choice. Try again.")
			continue
		if choice2 == "STR":
			STATS['STR'] += 1
                elif choice2 == "DEX":
                        STATS['DEX'] += 1
                elif choice2 == "CON":
                        STATS['CON'] += 1
                elif choice2 == "INT":
                        STATS['INT'] += 1
                elif choice2 == "WIS":
                        STATS['WIS'] += 1
                elif choice2 == "CHA":
                        STATS['CHA'] += 1
                else:
                        print("Invalid choice. Try again.")
                        continue
		STATS['CHA'] += 2
		print("A Half-Elf. Let's see who you take after, mom or dad. \nYou get a +2 to Charisma and a +1 to " + choice1 + " and " + choice2 + "." )
		return
def halforc():
	STATS['STR'] += 2
	STATS['CON'] += 1
def tiefling():
	STATS['INT'] += 1
	STATS['CHA'] += 2


# prompt to choose race
def chosenRace():
	while True:
		print '-' * 40
		chosenRace = raw_input("Which race would you like? \nDwarf\t\tElf\t\tHalfling\nHuman\t\tDragonborn\tGnome\nHalf-Elf\tHalf-Orc\tTiefling\n").upper()
		print '-' * 40
		if chosenRace == RACE[0] :
			print("A Dwarf! They're pretty cool.\n You get a +2 to Constitution.")
			dwarf()
		elif chosenRace == RACE[1] :
			print("An Elf!! That's fantastic! \nYou get a +2 to Dexterity.")
			elf()
		elif chosenRace == RACE[2] :
			print("A Halfling? Interesting... \nYou get a +2 to Dexterity. ")
			halfling()
		elif chosenRace == RACE[3] :
			print("A Human? Why? \nI mean, I guess they get a +1 to everything...")
			human()
		elif chosenRace == RACE[4] :
			print("Ahhhh... a Dragonborn. Very nice choice. \nA +2 to Strength and a +1 to Charisma.")
			dragonborn()
		elif chosenRace == RACE[5] :
			print("A Gnome, eh? Must be a tinkerer. \nYou get a +2 to Intelligence.") 
			gnome()
		elif chosenRace == RACE[6] :
			halfelf() 	
		elif chosenRace == RACE[7] :
        		print("A Half-Orc?! Well this should make for an interesting story... \nYou get a +2 to Strength and a +1 to Constitution.")
			halforc()
		elif chosenRace == RACE[8] :
        		print("Oooohhhh... A Tiefling! Scary. \nYou get a +2 to Charisma and a +1 to Intelligence.")
			tiefling()
		else :
			print("Invalid selection. Check your spelling.")
			continue
		return

stats()
chosenRace()
print("Well done!!! Here's your final stats!")
stats()



	

