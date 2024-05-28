locatoins = ["caveLocations", "forestLocation", "mountainLocation", "riverLocation"]
caveLocations = ["caveRoom1" , "caveRoom2"]
forestLocation = ["forestRoom1" , "forestRoom2"]
mountainLocations = ["mountainRoom1" , "mountainRoom2"]
riverLocations = ["riverRoom1" , "riverRoom2"]

#or

def cave():
	print("you're in the cave!")
	print("you can go NORTH, SOUTH, EAST, and WEST
	playerchoice = input (">>").lower()
	if playerChoice == "north":
		caveRoom1()
	elif playerChoice == "south":
		caveRoom2()
		
def caveRoom1():
	print("You're in cave Room 1")
	playerChoice = input(">>")

def caveRoom2():
	print("You're in cave Room 2")
	playerChoice = input(">>")
	
cave()