import random


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.d20 = Dice(20)
        self.d8 = Dice(8)
        self.d6 = Dice(6)
        self.hp = self.d20.roll()
        self.currentRoom = None

    def lookAround(self):
        if (self.currentRoom == None):
            print("In the Eeeether....")
        else:
            self.currentRoom.display()

    def display(self):
        print(self.name + " : " + str(self.hp))

    def inflictDamage(self, dmg, player):
        player.receiveDamage(dmg)

    def receiveDamage(self, dmg):
        self.hp = self.hp - dmg

    def isDead(self):
        return self.hp <= 0

    def getMeleeDamage(self):
        return self.d8.roll()

    def getHealthPot(self):
        return self.d6.roll()

    def showMenu(self):
        # blocks until the user enters their action
        option = input("Where would you like to go? ")
        return option

    def fight(self, player):
        turn = 1
        while (not player.isDead() and not self.isDead()):
            self.display()
            player.display()
            if (turn % 2 == 1):
                print(self.name)
                action = self.showMenu()
                if (action == "1"):
                    dmg = self.d8.roll()
                    self.inflictDamage(dmg, player)
                else:
                    heal = self.d6.roll()
                    self.hp = self.hp + heal
                    print("Healing....")
                turn = turn + 1
            else:
                print(player.name)
                action = player.showMenu()
                if (action == "1"):
                    dmg = self.d8.roll()
                    player.inflictDamage(dmg, self)
                    self.display()
                else:
                    heal = self.d6.roll()
                    player.hp = player.hp + heal
                    print("Healing....")
                    player.display()
                turn = turn - 1
        self.display()
        player.display()


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.thePlayers = []
        self.destinations = {}

    def addRoom(self, direction, room):
        self.destinations[direction] = room

    def addPlayer(self, player):
        self.thePlayers.append(player)
        # let the player know about the room
        # it just entered
        player.currentRoom = self

    def removePlayer(self, player):
        self.thePlayers.remove(player)
        player.currentRoom = None

    def takeExit(self, player, direction):
        if (direction in self.destinations):
            # remove ourselves from the current room
            self.removePlayer(player)
            self.destinations[direction].addPlayer(player)
        else:
            print("No exit found")

    def display(self):
        print(self.name)
        print(self.description)
        print("Possible Exits")
        exitList = []
        for exit in self.destinations:
            exitList.append(exit)
        exitList.sort()
        print(exitList)

        print("Also here:")
        if (self.thePlayers.__len__() != 0):
            for player in self.thePlayers:
                player.display()
                # show the destinations for this room
        else:
            print("No one is here :(\n")


class Dungeon:
    def __init__(self, name):
        self.name = name
        self.entrance = Room(name + " Lobby", "At the cave entrance")
        self.rooms = []

    def addRoom(self, name, description, exitPath):
        # should add a room off the lobby with
        # this exit
        newRoom = Room(name, description)
        if(name == "CS Hallway"):
            self.entrance.addRoom("west", newRoom)
        self.rooms.append(newRoom)

cscDept = Dungeon("CSC Dept")
p1 = Player("Mike")
cscDept.addRoom("CS Hallway", "A boring hallway in Dungeon CSC Dept", ["north", "south", "west"])
cscDept.addRoom("S120", "Litman classroom in Dungeon CSC Dept", ["north"])
cscDept.addRoom("S118", "Locklair classroom in Dungeon CSC Dept", ["east"])
cscDept.addRoom("Mac Lab", "The Mac lab in Dungeon CSC Dept", ["south"])
cscDept.entrance.addPlayer(p1)

# s120 = Room("S120", "Litman classroom....")
# csHallWay = Room("CS Hallway", "A boring hallway")
# s118 = Room("S118", "Locklair classroom")
# macLab = Room("Mac Lab", "The mac lab")
# s120.addRoom("north", csHallWay)
# csHallWay.addRoom("south", s120)
# csHallWay.addRoom("north", macLab)
# csHallWay.addRoom("west", s118)
# s118.addRoom("east", csHallWay)
# macLab.addRoom("south", csHallWay)
# cscDept.entrance.display()
while (True):
    p1.lookAround()
    where = p1.showMenu()
    if (where == "-1"):
        break
    p1.currentRoom.takeExit(p1, where)
