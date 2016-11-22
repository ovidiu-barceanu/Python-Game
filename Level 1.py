from sys import exit
from random import randint
# from random import choice
# import msvcrt as m

# This is for press enter to continue stuff, it uses msvcrt import
"""
def wait():
    m.getch()
"""

print
print "=============="
print "We will this story with introducing ourselves."
print "I'l go first... I am the Narrator."
print "And you are ?"
print "=============="
print

user_name = raw_input("Type your name > ")

player = user_name

print
print "=============="
print "Very well, I am pleased to met you, " + player
print
print "Now let's tell you the story of detective Smith"
print "Who took a case that gave him a little bit of troubles"
print "It all starts in an abandoned sanatorium,"
print "in a dark room"
print "=============="
print

raw_input("Press enter to continue")

"""
wrong_input = ['That is not how you do it ',
               'You have to do something ',
               'That is not gonna work ',
               'Nope, not that way '
               ]

wrong = choice(wrong_input)
"""

inventory = []


class Room(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):
    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('elevator')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)

        # be sure to print out the last scene
        current_room.enter()


class Death(Room):
    quips = [
        "You died.  You kinda suck at this.",
        "Nice job numbnuts",
        "You are dead...again...great",
        "Wow...you really suck at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips) - 1)]
        exit(1)


class Room1(Room):

    def enter(self):

        print "=============="
        print "You wake up in what a appears to be a bed"
        print "You can't see to much since there is a complete darkness in the room"
        print "A headache is ripping through your skull, but you try to figure out what is going on,"
        print "and where you are."
        print "=============="
        print
        print "**************"
        print "You can:"
        print "=> GET UP"
        print "=> CONTEMPLATE A LITTLE BIT "
        print "**************"
        print

        action = raw_input('what should you do, ' + player + ": ")

        if action == 'get up':

            print
            print "=============="
            print "You try to get your bearings,"
            print "and grab the side of the bed."
            print "You turn your head and notice that the darkness is not that complete."
            print "A slim ray of light is coming beneath what appears to be a door"
            print "=============="
            print

            raw_input("Press enter to continue")

            return 'room1A'


        elif action == 'contemplate a little bit':

            print
            print "=============="
            print "You stay in the bed and stare in the darkness."
            print "Eventualy you starve to death."
            print "=============="
            print
            return 'death'

        else:

            print
            print "=============="
            print "That is not gonna work " + player
            print "=============="
            print

            return 'room1'


class Room1A(Room):

    global inventory

    def enter(self):

        print
        print "=============="
        print "You get up and site on the side of the bed"
        print "For a moment the pain intensifies and you realize it's located"
        print "at the back of your head."
        print "You put your hand there and fell a rather large bump"
        print "and what appears to be some blood"
        print "Somebody knocked you out really good,"
        print "but apparently didn't want to kill you"
        print "=============="
        print

        raw_input("Press enter to continue")

        print
        print "**************"
        print "You can: "
        print "=> REACH THE DOOR"
        print "=> SEARCH YOUR POCKETS"
        print "**************"
        print

        action2 = raw_input('what do you do: ')

        if action2 == 'reach the door':

            print
            print "=============="
            print "You get up and try to reach the door"
            print "but you stumble on something,"
            print "fall down, break you neck and die"
            print "=============="
            print

            return 'death'

        elif action2 == 'search your pockets':

            inventory.append('lighter')

            print "++++++++++++++"
            print "You have %d items in your inventory" % len(inventory)
            print "You have ", inventory
            print "++++++++++++++"

            raw_input("Press enter to continue")

            print
            print "=============="
            print "You search your pockets and in one inner pockets"
            print "you find a pack of cigarettes with a lighter in it"
            print "Lucky you didn't quit smoking today"
            print "=============="
            print

            raw_input("Press enter to continue")

            return 'room1B'

        else:
            print
            print "=============="
            print "That is not gonna work " + player
            print "=============="
            print


            return 'room1A'


class Room1B(Room):

    global inventory



    def enter(self):


        raw_input("Press enter to continue")

        print
        print "=============="
        print "You keep the lighter in your hand, look towards the door,"
        print "and decide it is time to find out where the hell you are"
        print "=============="
        print

        print
        print "**************"
        print "You can:"
        print "=> REACH THE DOOR"
        print "=> LIGHT THE LIGHTER"
        print "=> CHECK INVENTORY"
        print "**************"
        print

        action = raw_input('What will you do, ' + player)

        if action == 'reach the door':

            print
            print "=============="
            print "While holding the lighter in your hand"
            print "You stand up and go for the door."
            print "But beeing still dark in the room,"
            print "You stumble on something, fall down"
            print "and broke your neck"
            print "Gee, if only you had something to make some light"

            return 'death'

        elif action == 'check inventory':

            print "++++++++++++++"
            print "You have %d items in your inventory" % len(inventory)
            print "You have ", inventory
            print "++++++++++++++"

            return 'room1B'

        elif action == 'light the lighter':

            print
            print "=============="
            print "You light the lighter and look around the room."
            print "The once white and clean wall were now covered with"
            print "musk and blood stains."
            print "It makes your stomach sick when you realise that the"
            print "bed was in the same condition"
            print "A closer look reveals what appears to be a desk near the door,"
            print "all kind of junk on the ground and a wheelchair right  "
            print "between you and the door"
            print "You move it aside and reach the door, "
            print "grab the handle and try to open it but it doesn't give up that easy "
            print "=============="
            print

            raw_input("Press enter to continue")

            return 'hallway'

        else:
            print "That is not gonna work"
            raw_input("Press enter to continue")
            return 'room1B'


class Hallway(Room):

    global inventory

    def enter(self):

        print
        print "=============="
        print "You are in a long hallway"
        print "There are several rooms you can reach from here"
        print "=============="
        print

        print
        print "**************"
        print "From here you can go to:"
        print
        print "ROOM1"
        print "hallway"
        print "ROOM2"
        print "ROOM3"
        print "ROOM4"
        print "CLOSET"
        print "SECURITY ROOM"
        print "VENT"
        print "RECREATIONAL ROOM"
        print "ELEVATOR"
        print "**************"
        print


        action = raw_input('Where do you go ' + player + " ")

        if action == 'room1':

            if 'lighter' in inventory:
                print "There is nothing to do there"
                print "You should move on"
                raw_input("Press enter to continue")
                return 'hallway'

            else:
                print "getting in room 1"
                return 'room1'

        elif action == 'room2':
            if 'screwdriver' in inventory:
                print "There is nothing left to do in there"
                print "You should move on."
                raw_input("Press enter to continue")
                return 'hallway'

            else:
                return 'room2'


        elif action =='room3':
            # door is locked until set of keys are found in security room
            return 'room3'

        elif action == 'room4':
            # door is locked until set of keys are found in security room

            return 'room4'

        elif action == 'closet':

            # you need a key to open this door. it can be found in the security room" \
            # add condition to check if it is opened"
            return 'closet'

        elif action == "security room":
            # the door from the hallway is locked" \
            # must get in there via the vent"

            return 'security_room'

        elif action == 'vent':

            # screwdriver from room2 is required to open grill

            return 'vent'

        elif action == 'recreational room':
            # door is locked with key card
            # Key card is found in security room
            return 'rec_room'

        else:
            print "Well we have to do something."
            return 'hallway'




class Room2(Room):

    global inventory

    def enter(self):

        print
        print"""
        ===============================================
        You see a door marked with Patient Reserve No. 2
        You grab the handle and push the door
        With some difficulty you manage to open it
        and manage to slip in.
        The lights are out, of course,
        and you barely see anythingSomething is blocking the door,
        and you can't fully open it
        to let the light from the hallway to get in
        ===============================================
        """
        print

        raw_input("Press enter to continue")

        print
        print "**************"
        print "You can:"
        print "=> SEARCH THE LIGHT SWITCH"
        print "=> RETURN TO HALLWAY"
        print "=> LIGHT THE LIGHTER"
        print "**************"
        print


        action = raw_input('well, now what '+ player + " ")

        if action == 'return to hallway':
            print
            print """
            ==============
            I guess a little bit of dark got you scared...pussy
            ==============
            """
            print
            raw_input("Press enter to continue")
            return 'hallway'

        elif action == 'search the light switch':
            print
            print"""
            ==============
            You check the wall on your right and
            walk your hands up and down on it, where
            usually the light switches are located.
            You make a few steps from the door,
            and finally you find something.
            You put your hands on it and
            the last thing you feel are the two
            wires coming out of it before feeling
            the jolt of electricity filling your body.
            ==============
            """
            print
            return 'death'

        elif action == 'light the lighter':
            print
            print"""
            ==============
            You light the lighter and look around
            the door, on the left side, where usually
            the light switches are located.
            You find it but notice that the frame and the flips
            are torn apart and a couple of wires are coming
            out of it. You carefully connect the two wires
            together. With a buzz the light bulb turns to life,
            and you can see around the room
            ==============
            """
            print
            raw_input("Press enter to continue")

            return 'room2A'





class Room2A(Room):

    global inventory



    def enter(self):
        print "this is Room 3"
        return 'room4'




class Room3(Room):
    def enter(self):
        print "this is Room 3"
        return 'room4'


class Room4(Room):
    def enter(self):
        print "This is room 4"
        return 'closet'


class Closet(Room):
    def enter(self):
        print 'This is the closet'
        return 'security_room'


class Security(Room):
    def enter(self):
        print "this the security room"
        return 'vent'


class Vent(Room):

    global inventory

    def enter(self):

        if 'screwdriver' in inventory:
            print " you use the screwdriver and reach the security room"
            return 'security room'
        else:
            print "you need somethig to open the grill"
            raw_input("Press enter to continue")
            return 'hallway'


class Recreation(Room):
    def enter(self):
        print "this is the recreation room"
        return 'elevator'


class Elevator(Room):
    def enter(self):
        print "this is the elvator"


class Map(object):
    rooms = {
        'room1': Room1(),
        'room1A': Room1A(),
        'room1B': Room1B(),
        'hallway': Hallway(),
        'room2': Room2(),
        'room3': Room3(),
        'room4': Room4(),
        'closet': Closet(),
        'security_room': Security(),
        'vent': Vent(),
        'recurity room': Recreation(),
        'elevator': Elevator(),
        'death': Death(),
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def opening_room(self):
        return self.next_room(self.start_room)


a_map = Map('room1')
a_game = Engine(a_map)
a_game.play()



"""
To do for next level

=> Make only one class with several def. EG : to remove room1A, room1B, and keep only one room1 with several def's
=> Make a wrong input class

"""