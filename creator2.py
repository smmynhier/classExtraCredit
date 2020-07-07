#!/usr/bin/python
import random

# Created two lists, one for races and the other for classes
RACE = ["DWARF", "ELF", "HALFLING", "HUMAN", "DRAGONBORN", "GNOME", "HALF-ELF", "HALF-ORC", "TIEFLING"]
CLASS=["BARBARIAN", "BARD", "CLERIC", "DRUID", "FIGHTER", "MONK", "PALADIN", "RANGER", "ROGUE", "SORCEROR", "WARLOCK", "WIZARD"]

# Defined class object, containing values and behaviors for Ability Scores, Modifiers, HP, AC and Initiative
class Statistic(object):
	value=0
	newMod=0
	HP=0
	AC=0
	INITIATIVE=0
	def __init__(self):
		stats = []
		mod=0
		for i in range(6):
			rolls = [random.randint(1,6) for _ in range(4) ]
			stats.append(sum(rolls) - min(rolls))
			self.value = stats[i]
		
			if self.value is 20:
				mod = 5
			elif self.value is 19 or self.value is 18:
				mod = 4
			elif self.value is 17 or self.value is 16:
				mod = 3
			elif self.value is 15 or self.value is 14:
				mod = 2
			elif self.value is 13 or self.value is 12:
				mod = 1
			elif self.value is 11 or self.value is 10:
				mod = 0
			elif self.value is 9 or self.value is 8:
				mod = 0-1
			elif self.value is 7 or self.value is 6:
				mod = 0-2
			elif self.value is 5 or self.value is 4:
				mod = 0-3
			elif self.value is 3:
				mod = 0-4
			self.mod = mod

	def updateMods(self):
			if self.value is 20:
				mod = 5
			elif self.value is 19 or self.value is 18:
				mod = 4
			elif self.value is 17 or self.value is 16:
				mod = 3
			elif self.value is 15 or self.value is 14:
				mod = 2
			elif self.value is 13 or self.value is 12:
				mod = 1
			elif self.value is 11 or self.value is 10:
				mod = 0
			elif self.value is 9 or self.value is 8:
				mod = 0-1
			elif self.value is 7 or self.value is 6:
				mod = 0-2
			elif self.value is 5 or self.value is 4:
				mod = 0-3
			elif self.value is 3:
				mod = 0-4
			self.mod = mod	
			return mod

# Initialize variables as Statistic objects, to use in script
HP=Statistic()
AC=Statistic()
INITIATIVE=Statistic()
STR=Statistic()
DEX=Statistic()
CON=Statistic()
INT=Statistic()
WIS=Statistic()
CHA=Statistic()

# Define the printed script for the initial table of stats
def stats():
	print('=' * 40)
	print("Stat\t\tValue\t\tModifier")
	print("STR\t\t%i\t\t%i") % (STR.value, STR.mod)
	print("DEX\t\t%i\t\t%i") % (DEX.value, DEX.mod)
	print("CON\t\t%i\t\t%i") % (CON.value, CON.mod)
	print("INT\t\t%i\t\t%i") % (INT.value, INT.mod)
	print("WIS\t\t%i\t\t%i") % (WIS.value, WIS.mod)
	print("CHA\t\t%i\t\t%i") % (CHA.value, CHA.mod)
	
# Called upon the updateMods behavior to update modifiers based of score changes
def updateMods():
	STR.updateMods()
	DEX.updateMods()
	CON.updateMods()
	INT.updateMods()
	WIS.updateMods()
	CHA.updateMods()

# Defined various race behaviors, to initialize stat changes
def dwarf():
		CON.value += 2
def elf():
		DEX.value += 2
def halfling():
		DEX.value += 2
def human():
		STR.value += 1
		DEX.value += 1
		CON.value += 1
		INT.value += 1
		WIS.value += 1
		CHA.value += 1
def dragonborn():
	STR.value += 2
	CHA.value += 1
def gnome():
	INT.value += 2
def halfelf():
		while True:
				choice1 = raw_input("Choose a stat to increase by 1: ").upper()
				choice2 = raw_input("Choose another stat to increase by 1: ").upper()
				print('=' * 40)
				if choice1 == "STR":
						STR.value += 1
				elif choice1 == "DEX":
						DEX.value += 1
				elif choice1 == "CON":
						CON.value += 1
				elif choice1 == "INT":
						INT.value += 1
				elif choice1 == "WIS":
						WIS.value += 1
				elif choice1 == "CHA":
						CHA.value += 1
				else:
						print("\tInvalid choice. Try again.")
						continue
				if choice2 == "STR":
						STR.value += 1
				elif choice2 == "DEX":
						DEX.value += 1
				elif choice2 == "CON":
						CON.value += 1
				elif choice2 == "INT":
						INT.value += 1
				elif choice2 == "WIS":
						WIS.value += 1
				elif choice2 == "CHA":
						CHA.value += 1
				else:
						print("\tInvalid choice. Try again.")
						continue
				CHA.value += 2
		print("A Half-Elf. Decide your destiny.\nYou get a +2 to Charisma\nand a +1 to " + choice1 + " and " + choice2 + "." )
		return
def halforc():
		STR.value += 2
		CON.value += 1
def tiefling():
		INT.value += 1
		CHA.value += 2

# Defined the chosenRace portion of the script, calling for an input and taking action based off response.
def chosenRace():
		while True:
				print('=' * 40)
				chosenRace = raw_input("\tWhich race would you like? \nDwarf\t\tElf\t\tHalfling\nHuman\t\tDragonborn\tGnome\nHalf-Elf\tHalf-Orc\tTiefling\n").upper()
				print('=' * 40)
				if chosenRace == RACE[0] :
					print("A Dwarf! They're pretty cool.\nYou get a +2 to Constitution.")
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
					print("Ahhhh... a Dragonborn.\nVery nice choice. \nA +2 to Strength and a +1 to Charisma.")
					dragonborn()
				elif chosenRace == RACE[5] :
					print("A Gnome, eh? Must be a tinkerer. \nYou get a +2 to Intelligence.")
					gnome()
				elif chosenRace == RACE[6] :
					print("A Half-Elf. Decide your own destiny.")
					halfelf()
				elif chosenRace == RACE[7] :
					print("A Half-Orc?! Well this should\nmake for an interesting story... \nYou get a +2 to Strength and a +1 to Constitution.")
					halforc()
				elif chosenRace == RACE[8] :
					print("Oooohhhh... A Tiefling! Scary. \nYou get a +2 to Charisma and a +1 to Intelligence.")
					tiefling()
				else :
					print("\tInvalid selection. Check your spelling.")	               
					continue
				return

def barbarian():
	HP.value=(12 + CON.mod)
	AC.value=(10 + DEX.mod + CON.mod)
	INITIATIVE.value=DEX.mod
def bard():
	HP.value=(8 + CON.mod)
	AC.value=(10 + DEX.mod)
	INITIATIVE.value=DEX.mod
def cleric():
	HP.value=(8 + CON.mod)
	AC.value=(10 + DEX.mod)
	INITIATIVE.value=DEX.mod
def druid():
	HP.value=(8 + CON.mod)
	AC.value=(10 + DEX.mod)
	INITIATIVE.value=DEX.mod
def fighter():
	HP.value=(10 + CON.mod)
	AC.value=(10 + DEX.mod)
	INITIATIVE.value=DEX.mod
def monk():
	HP.value=(8 + CON.mod)
	AC.value=(10 + DEX.mod + WIS.mod)
	INITIATIVE.value=DEX.mod
def paladin():
	HP.value=(10 + CON.mod)
	AC.value=(10 + DEX.mod)
	INITIATIVE.value=DEX.mod
def ranger():
	HP.value=(10 + CON.mod)
	AC.value=(10 + DEX.mod)
	INITIATIVE.value=DEX.mod
def rogue():
	HP.value=(8 + CON.mod)
	AC.value=(10 + DEX.mod)
	INITIATIVE.value=DEX.mod
def sorceror():
	HP.value=(6 + CON.mod)
	AC.value=(10 + DEX.mod)
	INITIATIVE.value=DEX.mod
def warlock():
	HP.value=(8 + CON.mod)
	AC.value=(10 + DEX.mod)
	INITIATIVE.value=DEX.mod
def wizard():
	HP.value=(6 + CON.mod)
	AC.value=(10 + DEX.mod)
	INITIATIVE.value=DEX.mod

def chosenClass():
	while True:
		print('=' * 40)
		chosenClass=raw_input("\tWhich class would you like? \nBarbarian\tBard\t\tCleric\nDruid\t\tFighter\t\tMonk\nPaladin\t\tRanger\t\tRogue\nSorceror\tWarlock\t\tWizard\n").upper()
		if chosenClass == CLASS[0] :
			print("A Barbarian. Harness your rage!!")
			barbarian()
		elif chosenClass == CLASS[1] :
			print("A Bard. Prepare for your audience.")
			bard()
		elif chosenClass == CLASS[2] :
			print("A Cleric. Bring the light to your allies.")
			cleric()
		elif chosenClass == CLASS[3] :
			print("A Druid. One with nature.")
			druid()
		elif chosenClass == CLASS[4] :
			print("A Fighter. A martial expert")
			fighter()
		elif chosenClass == CLASS[5] :
			print("A Monk. Focus and discipline.")
			monk()
		elif chosenClass == CLASS[6] :
			print("A Paladin. Your allies' faithful shield.")
			paladin()
		elif chosenClass == CLASS[7] :
			print("A Ranger. Defeat your foes from a distance, before they get near enough to strike.")
			ranger()
		elif chosenClass == CLASS[8] :
			print("A Rogue. They won't see you coming.")
			rogue()
		elif chosenClass == CLASS[9] :
			print("A Sorceror. Unleash wild magics.")
			sorceror()
		elif chosenClass == CLASS[10] :
			print("A Warlock. Your pact is your power.")
			warlock()
		elif chosenClass == CLASS[11] :
			print("A Wizard. Unleash arcane power upon all who stand in your way.")
			wizard()
		else :
			print("Invalid choice. Try again.")
			continue
		return

# Define the final stats printed table, showing the final results.  
def finalStats():
	print('=' * 40)
	print("HP: %i\t\tAC: %i\t\tInitiative: %i") % (HP.value, AC.value, INITIATIVE.value)
	print(" ")
	print("Stat\t\tValue\t\tModifier")
	print("STR\t\t%i\t\t%i") % (STR.value, STR.mod)
	print("DEX\t\t%i\t\t%i") % (DEX.value, DEX.mod)
	print("CON\t\t%i\t\t%i") % (CON.value, CON.mod)
	print("INT\t\t%i\t\t%i") % (INT.value, INT.mod)
	print("WIS\t\t%i\t\t%i") % (WIS.value, WIS.mod)
	print("CHA\t\t%i\t\t%i") % (CHA.value, CHA.mod)	

stats()
chosenRace()
updateMods()
chosenClass()
finalStats()
