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
        if (self.currentRoom is None):
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
        for player in self.thePlayers:
            player.display()
            # show the destinations for this room


class Dungeon:
    def __init__(self, name, mainRoomName, mainRoomDescription):
        self.name = name
        self.entrance = Room(mainRoomName, mainRoomDescription)
        self.rooms = []
        self.rooms.append(self.entrance)

    def addPlayer(self, player):
        self.entrance.addPlayer(player)
        while (True):
            player.lookAround()
            option = player.showMenu()
            if (option == "-1"):
                break
            elif (option == "create"):
                option = input("What kind of room is this: new or old?")
                if (option == "new"):
                    direction = input("In what direction should we add this room? ")
                    newRoomName = input("What is the name of the new room? ")
                    newRoomDescription = input("What is the description of the new room? ")
                    newRoom = Room(newRoomName, newRoomDescription)
                    self.rooms.append(newRoom)
                    player.currentRoom.addRoom(direction, newRoom)
                else:
                    # we need to show a list of existing rooms
                    # and be able to uniquely identify them so
                    # we can pick the room we want our new exit
                    # to lead.
                    for i in range(0, self.rooms.__len__()):
                        existingRoom = self.rooms[i]
                        print("\nThis room is available:")
                        print(existingRoom.name)
                        print(existingRoom.description)
                        pick = input("\nDo you want to go to it? [yes OR no]")
                        while (pick == "yes"):  # if not go through other rooms in rooms
                            player.currentRoom.removePlayer(player)
                            existingRoom.addPlayer(player)
                            break

            else:
                player.currentRoom.takeExit(player, option)


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
# s120.addPlayer(p1)

csDept = Dungeon("CS Department", "CS Hallway", "A boring hallway")
csDept.addPlayer(p1)
