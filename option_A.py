from variables import *

import time, random

def option_a(thirst, canteen):

    if thirst > 0 and canteen > 0:
        thirst -= 3
        canteen -= 1
        print "-------------------------------------------------------------------------------"
        print "You relax for a second, sipping on your water."
        print "-------------------------------------------------------------------------------"
        print
        time.sleep(4)
        if thirst < 0:
            thirst = 0
            return thirst, canteen
        return thirst, canteen

    elif thirst == 0 and canteen > 0:
        canteen -= 1
        print "-------------------------------------------------------------------------------"
        print "You just wasted water, you take a leak and continue."
        print "-------------------------------------------------------------------------------"
        thirst = 0
        time.sleep(4)
        return thirst, canteen
    elif canteen == 0:
        print "-------------------------------------------------------------------------------"
        print "Feeling the brutal sun beat harshly down, you"
        print "wipe the sweat from your forehead and reach down"
        print "for your canteen only to notice that it is empty."
        print "-------------------------------------------------------------------------------"
        time.sleep(4)
        return thirst, canteen
