# ZOMBIE HORDE RUNNER GAME THING IDK YOURE RUNNING FROM ZOMBIES WHAT THE FUCK

from death_functions import *
from story_functions import *
from time_counter import *
from variables import *

# *** STORY OPTION IMPORTS ***
from user_choices.option_A import *
from user_choices.option_B import *
from user_choices.option_C import *
from user_choices.option_D import *  # *** THIS MOTHER FUCKER RIGHT HEREEEE... SO MUCH TO WRITE ***
from user_choices.option_E import *
from user_choices.option_F import *
from user_choices.option_Q import *

print
print
print "                                                                WELCOME TO THE ZOMBIE BULLSHIT ADVENTURE!!!"
print "                                                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
#time.sleep(3)

#pretenseText()

# *** START THE STORY ***

# openingText()

# raw_input ("Press any key to continue...")
# time.sleep(0.5)

# ***** MAIN LOOP *** MAIN LOOP *** MAIN LOOP *** MAIN LOOP *** MAIN LOOP *** MAIN LOOP *****

while not done:

    time_correction_index = time_correction(time_now, day)
    time_now = time_correction_index[0]
    day = time_correction_index[1]

    hourofday_index = time_of_day(time_now)  # INDEX 0 IS THE BOOLEAN FOR VAR night, INDEX 1 IS THE STRING FOR hour_of_day
    night = hourofday_index[0]
    hour_of_day = hourofday_index[1]

    # ***** DEATH FUNCTIONS *** DEATH FUNCTIONS *****
    # ***** DEATH FUNCTIONS *** DEATH FUNCTIONS *****

    if dead is True:
        done = True
        print
        print "You are dead."
        time.sleep(3)
        continue

    # *** CHECKING FOR ZOMBIE DISTANCE ***
    dead = zombiesOvertake(dead, zombie_dist, your_dist)

    # *** CHECKING THIRST STATUS ***
    if dead == False:
        dead = thirstStatus(dead, thirst)

    # *** CHECKING HUNGER STATUS ***
    if dead == False:
        dead = hungerStatus(dead, hunger)

    # *** CHECKING EXHAUSTION STATUS ***
    if dead == False:
        exhaustion_index = exhaustionStatus(dead, tiredness)
        dead = exhaustion_index[0]
        tiredness = exhaustion_index[1]

    # *** CHECKING HEALTH STATUS ***
    if dead == False:
        dead =  healthStatus(health)

    if dead is True:
        done = True
        print
        print "You are now dead."  # MAKE A FUNCTION THAT DETECTS HOW YOU DIED AND PRINTS THE APPROPRIATE ENDING
        time.sleep(3)
        continue  # AND PUT THAT FUNCTION INSIDE OF story_functions.py

    # *** CHECKING FOR CAR DISTANCE GOES HERE *** / ***** COMING SOON *****

#    dateCall(day, hour_of_day)
    
    print "Day:", day
    print "Time:", time_now
    print "Hour of day:", hour_of_day
    print
    print "Zombie Distance:", zombie_dist
    print "Your Distance:", your_dist
    print
    print "Hunger:", hunger
    print "Thirst:", thirst
    print "Tiredness:", tiredness
    print "Canteen:", canteen
    print "Food:", food
    print "Health:", health                        # ***** ALL OF THIS WILL BE DELETED WHEN GAME IS READY *****
    print
    print "at_town:", at_town
    print "searched_town:", searched_town
    print "have_car:", have_car
    print "car_gas:", car_gas
    print "car_dist:", car_dist
    print
    print
    print "You have few options:"
    print
    print
    print
    print
    print "A. Drink from your canteen."

    print "B. Eat some food."
    if have_car is True:
        print "C. Get back into the car and drive to the next town."
    else:
        print "C. Walk down the highway to the next town."

    print "D. Explore the town to look for supplies."

    print "E. Lock the doors to the car and get some real rest."

    print "F. Assess your situation."

    print "Q. Quit the game."

    print

    # *** PICKING RANDOM EVENT THAT MIGHT HAPPEN WITHIN EACH DECISION ***
    # *** PERHAPS CHANGE THE CODE SO EACH OPTION HAS IT'S OWN RANDOM NUMBER GENERATOR ***
    rand_chance =  random.randrange(1, 11)
    print "Random Chance is:", rand_chance

    choice = raw_input("What do you do...? ")
    print

    # ***** CHOICE "Q" *** CHOICE "Q" *** CHOICE "Q" *** CHOICE "Q" *****

    if choice.lower() == "q":
        done = option_Q()
        continue

    # ***** CHOICE "A" *** CHOICE "A" *** CHOICE "A" *** CHOICE "A" ***** DRINK FROM CANTEEN

    elif choice.lower() == "a":

        a_index = option_a(thirst, canteen)

        thirst = a_index[0]
        canteen = a_index[1]

    # ***** CHOICE "B" *** CHOICE "B" *** CHOICE "B" *** CHOICE "B" *****  EAT SOME FOOD

    elif choice.lower() == "b":

        option_B_index = option_B(rand_chance, hunger, food, time_now, zombie_dist)

        hunger = option_B_index[0]
        food = option_B_index[1]
        time_now = option_B_index[2]
        zombie_dist = option_B_index[3]

    # ***** CHOICE "C" *** CHOICE "C" *** CHOICE "C" *** CHOICE "C" ***** DRIVE TO NEXT TOWN

    elif choice.lower() == "c":

        option_C_index = option_c(time_now, at_town, have_car, car_gas, rand_chance, car_heat, your_dist, zombie_dist, thirst, hunger,
                                  tiredness, done)

        time_now = option_C_index[0]
        at_town = option_C_index[1]
        have_car = option_C_index[2]
        car_gas = option_C_index[3]
        car_heat = option_C_index[4]
        your_dist = option_C_index[5]
        zombie_dist = option_C_index[6]
        thirst = option_C_index[7]
        hunger = option_C_index[8]
        tiredness = option_C_index[9]
        done = option_C_index[10]

    # ***** CHOICE "D" *** CHOICE "D" *** CHOICE "D" ***** SEARCH TOWN FOR STUFF
    # rand_chance numbers taken is 1, 3, 7, 8, 10

    elif choice.lower() == "d":

        if 5 <= time_now <= 19:
            option_D_index = option_d_day(at_town, searched_town, rand_chance, car_gas, time_now, zombie_dist, your_dist, thirst, hunger,
                                      tiredness, canteen, food, health, car_heat, have_car, done)
        else:
            option_D_index = option_d_night(at_town, searched_town, rand_chance, car_gas, time_now, zombie_dist, your_dist, thirst, hunger,
                                      tiredness, canteen, food, health, car_heat, have_car, done)


        at_town = option_D_index[0]
        car_gas = option_D_index[1]
        time_now = option_D_index[2]
        zombie_dist = option_D_index[3]
        your_dist = option_D_index[4]
        thirst = option_D_index[5]
        hunger = option_D_index[6]
        tiredness = option_D_index[7]
        canteen = option_D_index[8]
        food = option_D_index[9]
        health = option_D_index[10]
        car_heat = option_D_index[11]
        have_car = option_D_index[12]
        dead = option_D_index[13]
        searched_town = option_D_index[14]

    # ***** CHOICE "E" *** CHOICE "E" *** CHOICE "E" ***** REST FOR THE NIGHT

    elif choice.lower() == "e":

        # *** e_index CONTAINS VALUES TO BE ADDED TO: time_now, zombie_dist, hunger, thirst, tiredness, your_dist RESPECTIVELY ***
        e_index = option_E(rand_chance, drive_speed, tiredness)
        print "Before:", time_now, zombie_dist, hunger, thirst, tiredness, your_dist
        time_now += e_index[0]
        zombie_dist += e_index[1]
        hunger += e_index[2]
        thirst += e_index[3]
        tiredness = e_index[4]
        your_dist += e_index[5]

    # ***** CHOICE "F" *** CHOICE "F" *** CHOICE "F" ***** CHECK STATUS/INVENTORY

    elif choice.lower() == "f":

        option_F(your_dist, have_car, canteen, food, health, thirst, hunger, tiredness, poison, car_gas)

    else:
        print
        print "Nah son, A through E, or smash your head with a rock wit Q..."
        print
        time.sleep(3)

print
print "END"
