from variables import *
import time, random

# ***** ALL FUNCTIONS RELEVANT TO OPTION 'F' - CHECK STATUS *****

# MAIN FUNCTION:

def option_F(your_dist, have_car, canteen, food, health, thirst, hunger, tiredness, poison, car_gas):
    print "-------------------------------------------------------------------------------"
    print "You have traveled about", your_dist, "miles since day 1"
    supplyCheck(food, canteen, have_car, car_gas)
    print
    print
    poisonHealth(health, poison)
    hungerThirstTiredness(hunger, thirst, tiredness)
    print "-------------------------------------------------------------------------------"
    print

    raw_input("Press any key to continue...")
    time.sleep(1)


# *** CHECKS YOUR HEALTH AND ZOMBIE LEVEL ***

def poisonHealth(health, poison):
    if poison <= 1:
        if health >= 90:
            print "You feel fine and aren't injured too bad"
        elif 90 > health >= 60:
            print "You feel alright, just a couple scrapes and bruises, nothing major"
        elif 60 > health >= 30:
            print "Your body hurts. Time to get patched up"
            print "A splint and some stitches ought to help"
        elif 1 <= health < 30:
            print "You desperately need medical attention"
    elif poison == 2:
        if health >= 90:
            print "You feel a little weird but aren't injured too bad"
        elif 90 > health >= 60:
            print "You feel strange and could use a few band-aids but you'll be fine"
        elif 60 > health >= 30:
            print "Your body hurts, time to get patched up"
            print "The weird feeling in your gut isn't helping anything"
        elif 30 > health >= 1:
            print "You desperately need medical attention"
    elif poison == 3:
        if health >= 90:
            print "You aren't injured too bad but you're hungry and not for food"
            print "Hopefully this goes away soon"
        elif 90 > health >= 60:
            print "You're not feeling well. Other than that it's just a couple minor injuries"
        elif 60 > health >= 30:
            print "It doesn't hurt anymore, suddenly you have a lot of energy"
        elif 30 > health >= 1:
            print "You are not yourself. You feel... hungry..."

# *** TELLS YOU YOUR STATS ***

def hungerThirstTiredness(hunger, thirst, tiredness):
    if thirst > 10:
        print "You are very thirsty"
    elif 10 >= thirst >= 6:
        print "You're a little thirsty"
    elif thirst < 6:
        print "You feel pretty quenched"

    if hunger > 10:
        print "You need to eat"
    elif 10 >= hunger >= 6:
        print "You're a bit hungry"
    elif hunger < 6:
        print "You're not hungry"

    if tiredness > 10:
        print "You're very tired, it's time to sleep"
    elif 10 >= tiredness >= 6:
        print "You're a little weary, some rest sounds nice"
    elif tiredness < 6:
        print "You have plenty of energy"


# *** CHECKS YOUR WATER, FOOD, CAR STATUS (POSSIBLY WEAPONS EVENTUALLY)

def supplyCheck(food, canteen, have_car, car_gas):

    if have_car is True:
        print "You still have your car"
        if car_gas == 0:
            print "But you're out of gas"
        elif 0 < car_gas <= 3:
            print "But the gas is very low"
        elif 3 < car_gas <= 6:
            print "And you have a moderate amount of gas"
        elif 6 < car_gas <=8:
            print "You have plenty of gas"
        elif car_gas == 9:
            print "And the gas is reading full"

    elif have_car is False and car_dist < 40:
        print "Your car is", car_dist, "miles away"
    elif have_car is False and car_dist >= 40:
        print "Your car is too far away to get"
        print "You should find another car"

    print "You have", canteen, "Gallons of water"

    if food >= 5:
        print "You have plenty of food"
    elif 5 > food > 2:
        print "You have some food, but it'd probably be"
        print "a good idea to find some more"
    elif food <= 2:
        print "You have little food, time to find some"
    elif food == 0:
        print "You have no food"
