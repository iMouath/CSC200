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
            print("You are in the void...")
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
        option = input("What would you like to do? 1 - Hit or 2 - Heal: ")
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
        player.currentRoom = self

    def removePlayer(self, player):
        self.thePlayers.remove(player)
        player.currentRoom = None

    def roomMenu(self, player, room):
        player.lookAround()
        x = input("What Direction you want to go: [N,S,E,W]")
        if (x == "N"):
            room.removePlayer(player)
            macLab.addPlayer(player)
        elif (x == "S"):
            room.removePlayer(player)
            s120.addPlayer(player)
        elif (x == "E"):
            room.removePlayer(player)
            csHallWay.addPlayer(player)
        elif (x == "W"):
            room.removePlayer(player)
            s118.addPlayer(player)
        else:
            print("Invalid key!")

    def display(self):
        print(self.name)
        print(self.description)
        print("Possible Exists:")
        exitList = []
        for exit in self.destinations:
            exitList.append(exit)
        exitList.sort()
        print(exitList)
        print("Also here:")
        for player in self.thePlayers:
            player.display()
            # show the destinations for this room


p1 = Player("Mike")
s120 = Room("S120", "Litman classroom....")
csHallWay = Room("CS Hallway", "A boring hallway")
s118 = Room("S118", "Locklair classroom")
macLab = Room("Mac Lab", "The mac lab")
s120.addRoom("north", csHallWay)
csHallWay.addRoom("south", s120)
csHallWay.addRoom("north", macLab)
csHallWay.addRoom("west", s118)
s118.addRoom("east", csHallWay)
macLab.addRoom("south", csHallWay)
s120.addPlayer(p1)
p1.lookAround()
print("REMOVED")
s120.removePlayer(p1)
p1.lookAround()
s120.roomMenu(p1, s120)
