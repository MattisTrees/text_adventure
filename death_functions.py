import time

# **** CHECKS TO SEE IF ZOMBIES HAVE CAUGHT UP TO YOU ****
def zombiesOvertake(dead, zombie_dist, your_dist):
    if zombie_dist >= your_dist:
        print
        print "-------------------------------------------------------------------------------"
        print "You have been overtaken by the slobbery hoards of weird things..."
        print "-------------------------------------------------------------------------------"

        dead = True
        return dead



# **** CHECK TO SEE HOW THIRSTY YOU ARE ****
def thirstStatus (dead, thirst):
    if 8 < thirst <= 12:
        print "-------------------------------------------------------------------------------"
        print "You feel your lips start to crack and it becomes hard to swallow."
        print"-------------------------------------------------------------------------------"

    elif thirst == 13 or thirst == 14:
        print "-------------------------------------------------------------------------------"
        print "You are extremely thirsty, time to find some water."
        print "-------------------------------------------------------------------------------"

    elif thirst >= 15:
        print "-------------------------------------------------------------------------------"
        print "Suddenly your muscles all give out and you fall to the ground"
        print "convulsing. The lack of water in your body has disabled your"
        print "motor skills. All you can do now is pray for a quick death..."
        print "-------------------------------------------------------------------------------"

        dead = True
        return dead



# **** CHECK TO SEE HOW HUNGRY YOU ARE ****
def hungerStatus (dead, hunger):

    if 8 < hunger < 13:
        print "-------------------------------------------------------------------------------"
        print "Your stomach grumbles."
        print "-------------------------------------------------------------------------------"
    elif hunger == 13 or hunger == 14:
        print "-------------------------------------------------------------------------------"
        print "It's time to find some food, and soon.."
        print "-------------------------------------------------------------------------------"
    elif hunger >= 15:
        print "-------------------------------------------------------------------------------"
        print "You are too weak to move, your energy levels have plummeted."
        print "After not having eaten for several days malnutrition has gotten"
        print "the best of you and you fall to the floor out of exhaustion and hunger..."
        print "-------------------------------------------------------------------------------"
        dead = True
    return dead



# **** CHECK TO SEE IF YOU DIE FROM EXHAUSTION ****
def exhaustionStatus(dead, tiredness):
    if tiredness >= 15:
        print "-------------------------------------------------------------------------------"
        print "You are too weak to move, your energy levels have plummeted."
        print "After not having slept for several days your sleepiness has gotten"
        print "the best of you and you fall to the floor out of exhaustion..."
        print "-------------------------------------------------------------------------------"
        dead = True
        time.sleep(4)
    if tiredness < 0:
        tiredness = 0
    return dead, tiredness

# **** CHECK TO SEE IF YOU DIE FROM LOW HEALTH ****
def healthStatus(health):
    #THIS FUNCTION CHECKS HEALTH AMOUNT AND RETURNS DEAD IF HEALTH IS BELOW 1

    if 60 < health < 90:
        print "You are bleeding a bit"
        death = False
        return death

    elif 30 < health < 60:
        death = False
        print "You're not doing so well, look for something to patch you up."
        return death

    elif 1 < health < 30:
        death = False
        print "You are near death, get some help."
        return death

    elif health < 1:
        death = True
        return death

