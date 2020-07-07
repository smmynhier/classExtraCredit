#!/usr/bin/python
import random

CLASS=["CLERIC", "PALADIN", "RANGER", "ROGUE", "WIZARD"]

STATS = {
	"CON" : random.randint(0,5),
	"DEX" : 4,
}

def cleric():
	HP=(8 + STATS['CON'])
	AP=(10 + STATS['DEX'])
	print("Your CON modifier is %i, so your HP is 8 + %i.") % (STATS['CON'], STATS['CON'])
        print("Your DEX modifier is %i, so your AP is 10 + %i. Add armor to increase it.") % (STATS['DEX'], STATS['DEX'])
	print("HP: \t%i\tAP: \t%i") % (HP, AP)
def paladin():
	HP=(10 + STATS['CON'])
	AP=(10 + STATS['DEX'])
	print("Your CON modifier is %i, so your HP is 10 + %i.") % (STATS['CON'], STATS['CON'])
        print("Your DEX modifier is %i, so your AP is 10 + %i. Add armor to increase it.") % (STATS['DEX'], STATS['DEX'])
	print("HP: \t%i\tAP: \t%i") % (HP, AP)
def ranger():
	HP=(10 + STATS['CON'])
        AP=(10 + STATS['DEX'])
        print("Your CON modifier is %i, so your HP is 10 + %i.") % (STATS['CON'], STATS['CON'])
        print("Your DEX modifier is %i, so your AP is 10 + %i. Add armor to increase it.") % (STATS['DEX'], STATS['DEX'])
	print("HP: \t%i\tAP: \t%i") % (HP, AP)
def rogue():
	HP=(8 + STATS['CON'])
        AP=(10 + STATS['DEX'])
        print("Your CON modifier is %i, so your HP is 8 + %i.") % (STATS['CON'], STATS['CON'])
        print("Your DEX modifier is %i, so your AP is 10 + %i. Add armor to increase it.") % (STATS['DEX'], STATS['DEX'])
	print("HP: \t%i\tAP: \t%i") % (HP, AP)
def wizard():
	HP=(6 + STATS['CON'])
        AP=(10 + STATS['DEX'])
	print("Your CON modifier is %i, so your HP is 6 + %i.") % (STATS['CON'], STATS['CON'])
	print("Your DEX modifier is %i, so your AP is 10 + %i. Add armor to increase it.") % (STATS['DEX'], STATS['DEX'])
	print("HP: \t%i\tAP: \t%i") % (HP, AP)
def chosenClass():
	while True:
		chosenClass=raw_input("Which class would you like? \n").upper()
		if chosenClass == CLASS[0] :
			print("A Cleric. Bring the light to your allies.")
			cleric()
		elif chosenClass == CLASS[1] :
			print("A Paladin. Your allies' faithful shield.")
			paladin()
		elif chosenClass == CLASS[2] :
			print("A Ranger. Defeat your foes from a distance, before they get near enough to strike.")
			ranger()
		elif chosenClass == CLASS[3] :
			print("A Rogue. They won't see you coming.")
			rogue()
		elif chosenClass == CLASS[4] :
			print("A Wizard. Unleash arcane power upon all who stand in your way.")
			wizard()
		else :
			print("Invalid choice. Try again.")
			continue
		return
	
chosenClass()
