

# ***** DISTANCE VARIABLES *** DISTANCE VARIABLES *****
zombie_dist = 0 # When these two numbers meet, the hoard is on your ass
your_dist = 300 # and you pretty much die#.
walk_speed = 6
drive_speed = 16

# In case you have to leave your car behind and you want to go back for it (coming soon)
car_dist = 0

# ***** HEALTH METRICS *** HEALTH METRICS *****
thirst = 0 # MAX: 15
tiredness = 0 # MAX: 15
hunger = 0 # MAX 15

# ***** STOCKS *** STOCKS *** STOCKS *****

canteen = 5 # Water supply max of 10?
food = 5 #
first_aid = 0
inventory_size = canteen + food # ***** COMING SOON *****
INVENTORY_MAX =  15 # ***** COMING SOON *****


# *** (needs a function that checks health over 100) ***
health = 100 # MIN: 0 and you bleed to death or get eaten ***** COMING SOON *****


poison = 0 # MAX: 3   ***** COMING SOON *****
is_poisoned = False # Boolean to check if youre gonna turn into a zommbiiieeee ***** COMING SOON *****


# ***** CAR METRICS *** CAR METRICS *****
at_town = True # boolean to know if you in a town/city or in the middle of nowhere on a road
searched_town = 0
have_car = True
car_broken = False
car_heat = 0 # MAX 11
car_gas = 5 # MAX 9 - DON'T FORGET ABOUT THIS VARIABLE'S MAX WHEN ADDING GAS!!!!

# ***** UNITS OF TIME *** UNITS OF TIME *****
day = 13
time_now = 12
night = False
hour_of_day = "whatever"





done = False
dead = False # THE GAME CAN BE OVER AND THE CHARACTER CAN BE ALIVE... ya know (COMING SOON)
