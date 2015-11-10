from story_functions import *

def option_B(rand_chance, hunger, food, time_now, zombie_dist):
    """This function plays when the user chooses option 'B. Eat some food.'"""

    # *** RANDOM CHANCE NUMBERS TAKEN: 3 ***

    if rand_chance == 3:

        print "SOMETHING HAPPENS HERE TO INTERRUPT YOUR MEAL (JUST AS YOU GO TO GRAB YOUR BAG)"
        print "I'LL WRITE IT IN LATER"
        print
        raw_input("Press any key to continue...")
        print
        time.sleep(1)

        return hunger, food, time_now, zombie_dist

    elif food == 0:

        print "You have no food."
        raw_input("Press any key to continue...")
        print
        time.sleep(1)

        return hunger, food, time_now, zombie_dist

    elif hunger == 0:

        print "You're not hungry."
        raw_input("Press any key to continue...")
        print
        time.sleep(1)

        return hunger, food, time_now, zombie_dist

    else:

        print "-------------------------------------------------------------------------------"
        print "You decide to sit down, relax and eat some food."
        print "It's no picnic, but It'll get you by."
        print "-------------------------------------------------------------------------------"
        print
        hunger -= 4
        food -= 2
        time_now += 2

        zombie_dist += zombieMovement(2)

        raw_input ("Press any key to continue...")
        print
        time.sleep(1)

        return hunger, food, time_now, zombie_dist
