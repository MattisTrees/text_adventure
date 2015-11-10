import time, random


# ***** ALL FUNCTIONS RELEVANT TO OPTION 'E' - REST FOR THE NIGHT *****

# *** RANDOM CHANCE NUMBERS TAKEN FOR 'E': 5, 7 ***

def option_E(rand_chance, drive_speed, tiredness):
    """This function is for organizing all of the option 'E' related functions"""

    e_OpeningTxt()

    e_index = whatHappens_E(rand_chance, drive_speed, tiredness)

    return e_index


# *** The opening text to 'E' ***
def e_OpeningTxt():
    print "-------------------------------------------------------------------------------"
    print "You lock the doors to the car and lay the seat back."
    print "There's no chance anything could see you in here while"
    print "you sleep like a fuckin' baby. No way..."
    print "-------------------------------------------------------------------------------"
    print
    time.sleep(4)


# *** Someone/Something tries to break into the car (Takes rand_chance numbers 5 and 7) ***
def whatHappens_E(rand_chance, drive_speed, tiredness):
    """This function decides what will happen when you sleep"""

    zombie_dist_add = 0
    your_dist_add = 0

    if rand_chance == 5:
        tiredness += 2
        hunger_add = 2
        thirst_add = 2
        your_dist_add = drive_speed * 3
        time_add = 2
        zombie_dist_add = random.randrange(4, 11) * 2

        print "-------------------------------------------------------------------------------"
        print "No later than you close your eyes, it seems, that"
        print "you hear the back window to the car shatter. Panicked,"
        print "you turn the car on as fast as you can and put the car"
        print "in high gear and speed down the road."
        print
        print "You get no sleep but you gain some distance from those"
        print "ugly bastards."
        print "-------------------------------------------------------------------------------"
        print
        time.sleep(4)
        return time_add, zombie_dist_add, hunger_add, thirst_add, tiredness_add, your_dist_add

    else:

        tiredness -=9
        hunger_add = 4
        thirst_add = 3
        time_add = 9

        if tiredness < 0:
            tiredness = 0

        for i in range(9):
            zombie_dist_add += random.randrange(4, 11)

        print
        print "You sleep without incident, this time...bitch...you little fuckin' bitch..."
        print "-------------------------------------------------------------------------------"

        time.sleep(3)

        return time_add, zombie_dist_add, hunger_add, thirst_add, tiredness, your_dist_add
