from story_functions import *
from variables import *

def option_d_day(at_town, searched_town, rand_chance, car_gas, time_now, zombie_dist, your_dist, thirst, hunger,
             tiredness, canteen, food, health, car_heat, have_car, dead):
    """This function take almost all of the global variableS and decides what happens based on rand_chance"""

    TOWN_COUNT = 5

    if at_town is True:

        if searched_town >= TOWN_COUNT:

            searched_too_much()

        elif rand_chance == 1:  # *** DONE - +2-4Gas/+Car ***

            chance1 = random.randrange(1, 5)
            
            
            if have_car == True:
                more_gas = random.randrange(2, 5)
                car_gas += more_gas
                time_now += 2
                zombie_dist += zombieMovement(2)
                thirst += 2
                hunger += 2
                searched_town += 1
    
                print "-------------------------------------------------------------------------------"
                print "After rummaging around a derelict gas station for a couple hours you managed"
                print "to pump", more_gas, "gallons of gas from the tanks. You immediately walk back"
                print "to the car to put it in."
                print "-------------------------------------------------------------------------------"
                print
                raw_input("Press any key to continue...")
    
                return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                    hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town
            else:
                if chance1 == 1:

                    have_car = True
                    car_gas = random.randrange(5, 10)

                    print "Walking around you come across a large parking lot full of cars."
                    print "After searching like ten of them you find one with a key in it"
                    print "and a decent amount of gas. You drive back to the highway and weigh"
                    print "Your options."
                    print "-------------------------------------------------------------------------------"

        elif rand_chance == 2:  # *** DONE - option 1 +4 canteen, option 2 +4 food ***

            print "-------------------------------------------------------------------------------"
            print "You walk down the street and find two useful looking buildings. One is a coffee"
            print "shop with broken windows, the other is a hardware store which is boarded up."
            print
            print "Do you:"
            print "-------------------------------------------------------------------------------"
            print
            print "1. Take a look in the coffee shop or..."
            print "2. Try to break into the corner store?"
            print
            searched_town += 1
            chance2 = raw_input("...? ")
            print

            while chance2 != "1" or chance2 != "2":

                if chance2 == "1":

                    car_heat -= 1
                    canteen += 4
                    tiredness += 2
                    thirst += 2
                    hunger += 2
                    time_now += 2
                    zombie_dist += zombieMovement(2)

                    print "-------------------------------------------------------------------------------"
                    print "After rummaging through every nook and cranny of the"
                    print "coffee shop, you can't find anything worth a damn..."
                    print "-------------------------------------------------------------------------------"
                    print
                    time.sleep(5)
                    print"-------------------------------------------------------------------------------"
                    print "But just when you go to leave you find two"
                    print "gallons of water on the ground. Better than nothing!"
                    print "-------------------------------------------------------------------------------"
                    print
                    raw_input("Press any key to continue...")

                    return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                        hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

                elif chance2 == "2":

                    another_chance2 = random.randrange(1, 11)

                    if another_chance2 <= 8:

                        if tiredness > 0:
                            tiredness -= 3
                        if tiredness < 0:
                            tiredness = 0
                        food += 4
                        car_heat -= 1
                        thirst += 2
                        time_now += 1
                        hunger += 1

                        zombie_dist += zombieMovement(1)
                        print "-------------------------------------------------------------------------------"
                        print "The front of the corner store looks boarded up, so"
                        print "you walk around the alley and find the back door"
                        print "wedged open and you step inside."
                        print
                        print "Inside you find nothing useful but a warm pot of coffee"
                        print "and pile of energy bars. You quickly drink as much as you"
                        print "can, grab a few energy bars and get out of there,"
                        print "you have no interest in meeting the person who owned them."
                        print "-------------------------------------------------------------------------------"
                        print
                        raw_input("Press any key to continue...")

                        return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                            hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

                    elif another_chance2 >= 9:

                        print "-------------------------------------------------------------------------------"
                        print "You approach the hardware store and take a look"
                        print "at the board job. It looks like too much for you to"
                        print "pry open to get inside. Somebody kills yo ass."
                        print "whatever ill make something up later."
                        print "-------------------------------------------------------------------------------"
                        print
                        dead = True
                        health = 0

                        return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                            hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

                else:
                    chance2 = raw_input("Please enter '1' or '2' please...")

        elif rand_chance == 3:  # DONE - DEDICATED +5 FOOD ***

            print "You walk down the street and see an old grocery store. There's little chance"
            print "that there's something useful in there but you decide to give it a shot."
            print "You wind up finding a pack of canned food, good shit."
            print "-------------------------------------------------------------------------------"
            print

            time_now += 2
            thirst += 2
            hunger += 2
            tiredness += 2
            food += 5
            searched_town += 1
            zombie_dist += zombieMovement(2)

            time.sleep(6)

            return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

        elif rand_chance == 4:  # *** DONE - WRITE BETTER STORY ELEMENTS + 3food, or

                                # *** +3 gas/add car

            searched_town += 1

            print "You walk down the road a while and notice a strip mall with a"
            print "Used car dealership across the street. You don't have time to visit"
            print "Both. You decide to:"
            print
            print "1. Visit the car dealership and try to find something you can use."
            print "2. Visit the strip mall and try to find some food and water."
            chance4 = raw_input ("...?")

            while chance4 != "1" or chance4 != "2":

                if chance4 == "2":

                    car_heat -= 1
                    food += 3
                    tiredness += 2
                    thirst += 2
                    hunger += 2
                    time_now += 2
                    zombie_dist += zombieMovement(2)

                    print "-------------------------------------------------------------------------------"
                    print "After several hours rummaging through the stores you walk away with a few"
                    print "slim-jims. Not exactly a meal but its better"
                    print "that finding nothing."
                    print "-------------------------------------------------------------------------------"
                    print
                    raw_input("Press any key to continue...")

                    return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                        hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

                elif chance4 == "1":

                    another_chance4 = random.randrange(1, 11)

                    if another_chance4 <= 5:

                        if have_car == False:

                            car_heat = 0
                            thirst += 2
                            time_now += 2
                            hunger += 2
                            thirst += 2
                            have_car = True
                            car_gas = random.randrange(3,9)

                            zombie_dist += zombieMovement(2)
                            print
                            print "You find a fucking car. Whatever I'll someone that can actually write tell you"
                            print "how that happens. For now this works."
                            print "-------------------------------------------------------------------------------"
                            print
                            raw_input("Press any key to continue...")

                            return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                                hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

                        elif have_car == True:

                            car_heat -= 1
                            thirst += 1
                            time_now += 1
                            hunger += 1
                            car_gas += 3
                            zombie_dist += zombieMovement(1)

                            print"You find a few containers fill with gas, yay."
                            print "-------------------------------------------------------------------------------"

                            return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                                hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town


                    elif another_chance4 >= 9:

                        print
                        print "Unfortunately, you can't find anything useful."
                        print "-------------------------------------------------------------------------------"
                        print

                        return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                            hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

                else:
                    chance4 = raw_input ("Please enter a '1' or a '2' please... ")

        elif rand_chance == 5:  # *** DONE - DEDICATED: +5 CANTEEN ***

            time_now += 1
            thirst += 1
            hunger += 1
            canteen += 3
            tiredness += 1
            searched_town += 1
            zombie_dist += zombieMovement(1)

            print "You take a walk around the town to see supplies you might be able to find."
            print "After looking around for an hour you head into a small office that looks"
            print "mostly intact. Amongst the scattered papers and office supplies you find"
            print "an bottles of water in a desk drawer. Good find. You haul it back to"
            print "the car and assess your situation."
            print "-------------------------------------------------------------------------------"
            print
            raw_input("Press any key to continue...")

            return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

        elif rand_chance == 6:  # *** NOT DONE ***

            time_now += 1
            thirst += 1
            hunger += 1
            tiredness += 1
            searched_town += 1
            zombie_dist += zombieMovement(1)

            print "Dumb-shit scenario. We'll make this one with a couple of choices and it's own"
            print "random number generator or something."












            raw_input("Press any key to continue...")

            return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

        elif rand_chance == 7:  # *** NOT DONE - DEDICATED: FIND HEALTH PACK ***

            time_now += 1
            thirst += 1
            hunger += 1
            tiredness += 1
            searched_town += 1
            health += 35

            if health > 100:
                health = 100

            zombie_dist += zombieMovement(1)

            print "You find a first aid kit. You quickly patch up all your boo-boo's"
            print
            raw_input("Press any key to continue...")
            print

            return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

        elif rand_chance == 8:  # *** NOT DONE ***

            time_now += 1
            thirst += 1
            hunger += 1
            tiredness += 1
            searched_town += 1
            zombie_dist += zombieMovement(1)

            print "THIS IS ANOTHER SCENARIO WHERE SOME KINDA CRAZY SHIT HAPPENS. I SHOULD PROBABLY MAKE"
            print "TWENTY SCENARIOS INSTEAD OF TEN FOR MORE VARIETY, HUH? MAN, THAT'S GONNA BE A LOT"
            print "OF WRITING..."
            raw_input("Press any key to continue...")

            return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town


        elif rand_chance == 9 or rand_chance == 10:  # *** NOT DONE ***

            time_now += 4
            thirst += 3
            tiredness += 3
            hunger += 3
            searched_town += 3
            zombie_dist += zombieMovement(1)

            for i in range(4):
                zombie_spd = random.randrange(4, 11)
                zombie_dist += zombie_spd

            print "-------------------------------------------------------------------------------"
            print "You look around the town for hours, painstakenly"
            print "rummaging through every building you come across."
            print "Unfortunately you found nothing but some exhaustion"
            print "and a huge waste of time."
            print "-------------------------------------------------------------------------------"
            print
            raw_input("Press any key to continue...")

            return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

        else:
            print "This is the placeholder text, if you see this then there are too many random"
            print "chance numbers and i need to write more content."
            time.sleep(4)


            return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

    elif at_town is False:  # *** DONE ***
        print "-------------------------------------------------------------------------------"
        print "You have broken down on the highway. There are many broken down cars but"
        print "few buildings in sight."
        print "-------------------------------------------------------------------------------"
        print
        time.sleep(3)

        if night == True:  # *** MAYBE PUT A 'GO ANYWAY'? ***

            print "It's probably best to stick to the road, night time is dangerous."
            print "-------------------------------------------------------------------------------"

            return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
            hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

        if night == False:

            if rand_chance <= 3:

                print "You head towards a building that looks a bit useful."
                time.sleep(4)

                if rand_chance == 1:

                    time_now += 2

                    food += 2
                    health += 15
                    if health > 100:
                        health = 100
                    zombie_dist += zombieMovement(2)

                    print "You head towards a gas station. After rummaging around for a while"
                    print "you find an ounce or two of well preserved trail mix and a simple first"
                    print "aid kit, you patch up a bit and head back to the road."
                    print "-------------------------------------------------------------------------------"

                    return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                    hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

                if rand_chance == 2:

                    time_now += 1
                    health -= 20
                    zombie_dist += zombieMovement(1)

                    print "You approached the house and begin looking around. Finding nothing"
                    print "Downstairs you climb the stairs to the second floor. About halfway"
                    print "up you hit a particularly rotted out plank and you fall through the"
                    print "stair back down to the first floor. With a sprained ankle and a few"
                    print "minor scrapes and bruises you limp back to the road and start"
                    print "heading toward the next town."
                    print "-------------------------------------------------------------------------------"


                    return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                    hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town

                if rand_chance == 3:

                    print "You begin to approach a small concrete building. About half way there"
                    print "you hear a gunshot go off. You quickly drop to the ground and you see"
                    print "the dust in the air where the bullet hit the ground about three feet"
                    print "away from you. Obviously somebody doesnt want you around so you sprint"
                    print "back to the highway and start heading north to the next town."
                    print "-------------------------------------------------------------------------------"

                    time.sleep(6)

                    return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                    hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town


            elif rand_chance > 3:

                print "You look around at the few buildings that you can see and decide that"
                print "none of them are worth looking through. Either they are derelict to"
                print "the point that they seem dangerous just to enter, or they look like"
                print "they've been looted many times before, or both."
                print "-------------------------------------------------------------------------------"

                time.sleep(6)

                return at_town, car_gas, time_now, zombie_dist, your_dist, thirst, \
                    hunger, tiredness, canteen, food, health, car_heat, have_car, dead, searched_town




def searched_too_much():
    """This is if you searched the town too much"""

    print "-------------------------------------------------------------------------------"
    print "You've wasted enough time here. Time to get some rest or move on."
    print "-------------------------------------------------------------------------------"
    print
    time.sleep(3)

def option_d_night(at_town, searched_town, rand_chance, car_gas, time_now, zombie_dist, your_dist, thirst, hunger,
             tiredness, canteen, food, health, car_heat, have_car, dead):

    print "write a few dangerous things that couLd happen at night here."
    print "With an equal amount of things that wind up beneficial."
    print "And some that add to and take away from some variables."

    return at_town, searched_town, rand_chance, car_gas, time_now, zombie_dist, your_dist, thirst, hunger,\
             tiredness, canteen, food, health, car_heat, have_car, dead

