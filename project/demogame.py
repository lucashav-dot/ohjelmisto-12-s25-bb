import random
import tarinaesim
from geopy import distance

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='demogame',
    user='root',
    password='1q2w3e',
    autocommit=True
)



# FUNCTIONS

# removed continent and used brazil as game base, with medium airports
# select 30 airports for the game
def get_airports():
    sql = """SELECT ident, name, type, latitude_deg, longitude_deg
FROM airport
WHERE iso_country = 'BR' 
AND type='medium_airport'
ORDER by RAND()
LIMIT 35;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# get all goals
def get_goals():
    sql = "SELECT * FROM goal;"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# create new game
def create_game(start_money, p_range, cur_airport, p_name, a_ports):
    sql = "INSERT INTO game (money, player_range, location, screen_name) VALUES (%s, %s, %s, %s);"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (start_money, p_range, cur_airport, p_name))
    g_id = cursor.lastrowid

    # add goals / loot boxes
    goals = get_goals()
    goal_list = []
    for goal in goals:
        for i in range(0, goal['probability'], 1):
            goal_list.append(goal['id'])

    # exclude starting airport
    g_ports = a_ports[1:].copy()
    random.shuffle(g_ports)

    for i, goal_id in enumerate(goal_list):
        sql = "INSERT INTO ports (game, airport, goal) VALUES (%s, %s, %s);"
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, (g_id, g_ports[i]['ident'], goal_id))

    return g_id


# get airport info
def get_airport_info(icao):
    sql = f'''SELECT ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


# check if airport has a goal
def check_goal(g_id, cur_airport):
    sql = f'''SELECT ports.id, goal, goal.id as goal_id, name, money 
    FROM ports 
    JOIN goal ON goal.id = ports.goal 
    WHERE game = %s 
    AND airport = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (g_id, cur_airport))
    result = cursor.fetchone()
    if result is None:
        return False
    return result


# calculate distance between two airports
def calculate_distance(current, target):
    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km


# get airports in range
def airports_in_range(icao, a_ports, p_range):
    in_range = []
    for a_port in a_ports:
        dist = calculate_distance(icao, a_port['ident'])
        if dist <= p_range and not dist == 0:
            in_range.append(a_port)
    return in_range


# set loot box opened

# update location
def update_location(icao, p_range, u_money, g_id):
    sql = f'''UPDATE game SET location = %s, player_range = %s, money = %s WHERE id = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (icao, p_range, u_money, g_id))



# game starts
# ask to show the story
storyDialog = input('Do you want to read the background story? (Y/N): ').upper()
if storyDialog == 'Y':
    # print wrapped string line by line
    for line in tarinaesim.haetarina():
        print(line)



# GAME SETTINGS
print('When you are ready to start, ')
player = input('type player name: ')
# boolean for game over and win
game_over = False
win = False

# start money = 1000
money = 10000
# start range in km = 2000
player_range = 20000

# golden ball = 0
golden_ball = 0

# score = 0
score = 0

# snail that chases you, beginning value 0
snail = 0

# boolean for diamond found
diamond_found = False

# all airports
all_airports = get_airports()
# start_airport ident
start_airport = all_airports[0]['ident']

# current airport
current_airport = start_airport

# game id
game_id = create_game(money, player_range, start_airport, player, all_airports)

# GAME LOOP
while not game_over:
    # get current airport info
    airport = get_airport_info(current_airport)
    # show game status
    print(f'''You are at {airport['name']}.''')
    print(f"\033[93mYou have {golden_ball} golden balls\033[0m")
    # pause
    input('\033[32mPress Enter to continue...\033[0m')
    # if airport has goal ask if player wants to open it
    # check goal type and add/subtract money accordingly
    goal = check_goal(game_id, current_airport)
    snail += 1 # add + 1 on each loop
    if snail == 5: # snail "catches" you after reaching value "5"
        print('Snail Got you, Game over!')
        game_over = True

    if goal:
        snail -= 1  # subtract 1 when finding treasure, snail "slows down" for one turn
        question = input(
            f'''Do you want to open lootbox (Y/N): ''')
        if not question == 'N':

            if goal['money'] > 0:
                money += goal['money']
                print(f'''Congratulations! You found {goal['name']}. That is worth {goal['money']}$.''')
                print(f'''You have now {money:.0f}$''')
            elif goal['money'] == 0:
                golden_ball += 1
                print(f'''Congratulations! You found A Golden Ball.''')
                input("\033[32mPress Enter to continue...\033[0m")
            else:
                money = 0
                print(f'''Oh no! You have been robbed. You lost all your money''')
                input("\033[32mPress Enter to continue...\033[0m")


    # ask to buy fuel/range

    # show airports in range. if none, game over
    airports = all_airports

    if len(airports) == 0:
        print('You are out of range.')
        game_over = True
    else:

        r = random.randint(1, 6)
        print(f"\033[32mThe golden dice gave you {r} new airports.\033[0m")
        random_list = random.sample(airports, r)
        for n, item in enumerate(random_list):
            ap_distance = calculate_distance(current_airport, item['ident'])
            print(f"{n + 1}. {item['name']}, {item['ident']}")

        # ask for destination
        ask = int(input("\033[32mSelect one of the following airports:\033[0m"))
        dest = random_list[ask - 1]  # no nested indexing
        icao=dest['ident']
        selected_distance = calculate_distance(current_airport, icao)






        update_location(icao, player_range, money, game_id)
        current_airport = icao
        if player_range < 0:
            game_over = True





    # if 5 Golden balls, game is won
    if golden_ball == 100:
        game_over = True


# if game is over loop stops
# show game result
print(f'''{'You won!' if golden_ball == 1 else 'You lost!'}''')
print(f"You Found {golden_ball} Golden Balls")
