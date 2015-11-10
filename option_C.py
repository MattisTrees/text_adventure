from story_functions import *
from variables import *

def option_c(time_now, at_town, have_car, car_gas, rand_chance, car_heat, your_dist, zombie_dist, thirst, hunger,
             tiredness, done):
    """This function decides what happens when the user chooses option C - get in the car and drive\
    and it needs to return every variable that it takes in"""

    if have_car is True and car_gas > 0:
        print "-------------------------------------------------------------------------------"
        print "You get in and drive off, hopefully this drive is uneventful."
        print
        time.sleep(1)
        print

    # drive_time IS THE DISTANCE TO THE NEXT DOWN AND HOW LONG IT TAKES YOU TO DRIVE THERE
        drive_time = random.randrange(1, 5)

        for i in range(drive_time, 0, -1):

            if car_gas > 0 and car_heat < 12:

                time_now += 1
                car_gas -= 1
                car_heat += 1
                your_dist += drive_speed
                zombie_dist += zombieMovement(1)
                if car_heat >= 10:
                    print "The hood is steaming, but you press on anyway"
                    print "You need to get the next town."
                    print "-------------------------------------------------------------------------------"
                    time.sleep(1)
                    print

                if i == 1:

                    print "After driving for", drive_time, " hours you come upon another town and"
                    print "roll to a stop."
                    time.sleep(2)

                    if car_gas == 0:
                        print
                        print "Good thing, too. Cause you're out of gas."

                    hunger += 2
                    thirst += 2
                    tiredness += 2
                    at_town = True
                    done = False
                    print "-------------------------------------------------------------------------------"
                    print
                    raw_input("Press any key to continue...")
                    print
                    time.sleep(1)

                    return time_now, at_town, have_car, car_gas, car_heat, your_dist, zombie_dist, thirst,\
                        hunger, tiredness, done

            elif car_gas <= 0:

                print "You feel the engine gasp and putter as soon as you realize where"
                print "the gas meter is. After driving for", drive_time - i, "hours, the car"
                print "slowly rolls to a stop. You put it in park and step out. You are"
                print "on foot from here on out unless can find some gas and SOON."
                print "-------------------------------------------------------------------------------"
                print
                have_car = False
                at_town = False
                done = False
                hunger += 2
                thirst += 2
                tiredness += 2
                car_gas = 0
                raw_input("Press any key to continue...")
                time.sleep(1)

                return time_now, at_town, have_car, car_gas, car_heat, your_dist, zombie_dist, thirst,\
                    hunger, tiredness, done

            elif car_heat >= 12:

                print "After steaming for several hours your car has finally given up."
                print "Despite you furiously pressing the gas pedal your car slowly"
                print "rolls to a stop. you get out and check under the hood..."
                print
                time.sleep(4)
                print
                print "After looking under the hood for a while you notice a crack"
                print "in the radiator leaking the fluid. This car is useless and"
                print "you have wasted two more hours."
                print "-------------------------------------------------------------------------------"
                print

                have_car = False
                at_town = False
                time_now += 1
                thirst += 2
                hunger += 2
                tiredness += 2
                raw_input("Press any key to continue...")
                print
                time.sleep(1)

                return time_now, at_town, have_car, car_gas, car_heat, your_dist, zombie_dist, thirst,\
                    hunger, tiredness, done

    elif car_gas == 0 and have_car is True:

        print "-------------------------------------------------------------------------------"
        print "You get in the car and turn the keys in a hurry to get out of here."
        print "But to your dismay the car is out of gas. You grab your bag, step"
        print "out and prepare for the trek ahead, praying you find gas soon."
        print "-------------------------------------------------------------------------------"
        print
        have_car = False
        raw_input("Press any key to continue...")
        print
        time.sleep(1)

        return time_now, at_town, have_car, car_gas, car_heat, your_dist, zombie_dist, thirst,\
            hunger, tiredness, done

    # *** IF YOUR CAR HAS BROKEN DOWN ON THE HIGHWAY ***
    elif have_car is False and at_town is False:
        walk_time = random.randrange(2, 7)
        dist_walked = walk_time * walk_speed
        your_dist += dist_walked
        time_now += walk_time
        zombie_dist += zombieMovement(walk_time)
        at_town = True

        print "-------------------------------------------------------------------------------"
        print "You walk", dist_walked, "miles to the next town."
        print "-------------------------------------------------------------------------------"
        print
        raw_input("Press any key to continue...")
        print
        time.sleep(1)

        return time_now, at_town, have_car, car_gas, car_heat, your_dist, zombie_dist, thirst,\
            hunger, tiredness, done

    # *** IF YOUR CAR IS BROKEN DOWN AND YOU CAN'T FIND A NEW ONE IN THE CURRENT TOWN ***
    elif have_car is False and at_town is True:

        walk_time = random.randrange(3, 9)
        dist_walked = walk_time * walk_speed
        your_dist += dist_walked
        time_now += walk_time
        zombie_dist += zombieMovement(walk_time)
        at_town = True

        print "-------------------------------------------------------------------------------"
        print "You walked", dist_walked, "miles to the next town."
        print "-------------------------------------------------------------------------------"
        raw_input("Press any key to continue...")

        return time_now, at_town, have_car, car_gas, car_heat, your_dist, zombie_dist, thirst,\
            hunger, tiredness, done
