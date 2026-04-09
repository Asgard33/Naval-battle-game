import webbrowser
import pyinputplus as pyip
from time import sleep
import os
import random
import csv




#####################################




def check_coord(grid, i, j):
    ''' Grid*int*int -> Bool
    Takes a tuple (i,j) representing the cell at row i and column j
    returns True if all surrounding cells are empty, False otherwise '''

    adjacent = [(i - 1 - 1, j - 1 - 1), (i - 1 - 1, j - 1), (i - 1 - 1, j), (i, j - 1 - 1), (i - 1, j),
                  (i - 1, j - 1 - 1), (i, j - 1), (i, j)]  # coordinates of adjacent cells
    for (x, y) in adjacent:
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
            if grid[x][y] != '..':  # the adjacent cell is not empty
                return False
    return True


def print_game_board(L):
    # print('current board')
    print('   ', '     '.join(str(i) for i in range(1, 11)))  # first line with numbers
    for i, row in enumerate(L):
        print(chr(i + 65), (row))  # row indices as letters



all_boats = ['AC', 'SM', 'T ', 'C ', 'D ']


def ships():
    Carrier = ['AC', 'AC', 'AC', 'AC', 'AC']  # list representing the aircraft carrier 
    Cruiser = ['C ', 'C ', 'C ', 'C ']  # list representing the cruiser
    Destroyer = ['D ', 'D ', 'D ']  # list representing the destroyer
    Submarine = ['SM', 'SM', 'SM']  # list representing the submarine
    Torpedo_boat = ['T ', 'T ']  # list representing the torpedo

    ships_variables = locals()  # Gets a dictionary of local variables

    return ships_variables


Dic = ships()  # Calls the ships() function and stores the result in the variable Dic


# print(Dic)


def placement():

    
    global player   # player is a boolean variable that is True if a human player is running the command
    

    board = [['..'] * 10 for i in range(10)]

    if player:

        placed = []  # list that will contain already placed ships to raise an error if the chosen ship is already placed

        while len(placed) != len(Dic.keys()):

            print('current board')
            print_game_board(board)

            while True:
                
                ship = pyip.inputMenu(
                    ['Carrier(5cells)', 'Cruiser(4cells)', 'Destroyer(3cells)', 'Submarine(3cells)',
                     'Torpedo_boat(2cells)'],
                    'Which ship do you want to place? \n', numbered=True)
                ship = ship.split('(')[0]
                if ship not in Dic.keys():
                    print("This ship does not exist")
                    break

                if ship in placed:
                    print('\n')
                    print('This ship has already been placed')
                    break

                print('In which direction do you want to place your ship? ')
                print('1.Horizontal')
                print('2.Vertical')
                direction = str(input(':'))
                direction = direction.lower()
                choices = 'h', 'v', 'horizontal', 'vertical', 'H', 'V', 'Horizontal', 'Vertical', '1', '2'
                while direction not in choices:
                    print('In which direction do you want to place your ship? ')
                    print('1.Horizontal')
                    print('2.Vertical')
                    direction = str(input(':'))

                direction = direction.lower()
                print_game_board(board)

                if direction == 'horizontal' or direction == 'h' or direction == '1':

                    count = 0

                    l = str(pyip.inputStr(
                        'Choose the highest coordinate (top right) to place your ship. \n'))
                    l = l.upper()
                    l = l.replace('', ',').split(',')
                    if l[2] == '1' and l[3] == '0':
                        coordinate = (ord(l[1]) - 64, 10)

                    elif len(l) == 4:
                        coordinate = (ord(l[1]) - 64, int(l[2]))

                    row = coordinate[0]

                    min_col = coordinate[1]

                    if min_col + len(Dic[ship]) - 1 > 10:
                        print('This placement is impossible')
                        break

                    for k in range(len(Dic[ship])):

                        if check_coord(board, row, min_col + k):
                            count += 1

                    if count == len(Dic[ship]):

                        for k in range(len(Dic[ship])):
                            board[row - 1][min_col + k - 1] = Dic[ship][0]

                        placed.append(ship)

                    else:
                        print('This placement is impossible')
                        break



                elif direction == 'vertical' or direction == 'v' or direction == '2':

                    count = 0
                    l = str(pyip.inputStr(
                        'Choose the first coordinate (top left) to place your ship. \n'))
                    l = l.upper()
                    l = l.replace('', ',').split(',')
                    if l[2] == '1' and l[3] == '0':
                        coordinate = (ord(l[1]) - 64, 10)
                    elif len(l) == 4:
                        coordinate = (ord(l[1]) - 64, int(l[2]))
                    else:
                        None
                    col = coordinate[1]

                    min_row = coordinate[0]

                    if min_row + len(Dic[ship]) - 1 > 10:
                        print('This placement is impossible')
                        break

                    for k in range(len(Dic[ship])):

                        if check_coord(board, min_row + k, col):
                            count += 1

                    if count == len(Dic[ship]):

                        for k in range(len(Dic[ship])):
                            board[min_row + k - 1][col - 1] = Dic[ship][0]

                        placed.append(ship)

                    else:
                        print('This placement is impossible')
                        break

                else:
                    print("This direction does not exist")
                    break

                break

        print('All your ships have been placed')
        print_game_board(board)

        return board

    else:

        remaining = [k for k in Dic.keys()]

        while remaining != []:

            while True:

                ship = random.choice(remaining)

                direction = random.choice(['horizontal', 'vertical'])

                if direction == 'horizontal':

                    count = 0

                    row, min_col = random.randint(1, 10), random.randint(1, 10 - len(Dic[ship]) + 1)

                    for k in range(len(Dic[ship])):

                        if check_coord(board, row, min_col + k):
                            count += 1

                    if count == len(Dic[ship]):

                        for k in range(len(Dic[ship])):
                            board[row - 1][min_col + k - 1] = Dic[ship][0]

                        remaining.remove(ship)

                    else:
                        break



                elif direction == 'vertical':

                    count = 0

                    col, min_row = random.randint(1, 10), random.randint(1, 10 - len(Dic[ship]) + 1)

                    for k in range(len(Dic[ship])):

                        if check_coord(board, min_row + k, col):
                            count += 1

                    if count == len(Dic[ship]):

                        for k in range(len(Dic[ship])):
                            board[min_row + k - 1][col - 1] = Dic[ship][0]

                        remaining.remove(ship)

                    else:
                        break

                break

        return board


# board update function


def update_board(player_board, i, j, boolean):  # This function updates the public shot boards of players 1 and 2
    
    global player1_board
    global player2_board

    if turn % 2 == 1:
        if boolean:
            if player2_board[i][j] != '..':
                player_board[i][j] = 'X '
        else:
            player_board[i][j] ='O '

    else:
        if boolean:
            if player1_board[i][j] != '..':
                player_board[i][j] = 'X '
        else:
            player_board[i][j] = 'O '
    
    return player_board



def shoot(ship_grid, shot_grid):
    global player1_shots
    global player2_shots
    global player1_board
    global player2_board
    global a
    '''Grid -> Bool
    asks the player for their shot, checks validity, updates the grid then returns a boolean'''
    # alphabet = 'ABCDEFGHIJ'

    # Update the grid with the shot result (hit or miss)
    if ship_grid[a[0]][a[1]] == '..':
        # print('Miss!')
        shot_grid[a[0]][a[1]] = 'O '
        return False
    elif ship_grid[a[0]][a[1]] != '..':
        # print('Hit!')
        shot_grid[a[0]][a[1]] = 'X '
        return True


def sink(grid):
    '''Grid --> int
    Displays all sunk ships and returns their count '''
    AC = 0
    C = 0
    D = 0
    SM = 0
    T = 0
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] in all_boats:
                for k in all_boats:
                    if grid[i][j] == k:
                        if k == 'AC':
                            AC += 1
                        elif k == 'C ':
                            C += 1
                        elif k == 'D ':
                            D += 1
                        elif k == 'SM':
                            SM += 1
                        elif k == 'T ':
                            T += 1
    if AC == 0:
        if player :
            print('The Aircraft Carrier is sunk')
        res += 1
    if C == 0:
        if player :
            print('The Cruiser is sunk')
        res += 1
    if D == 0:
        if player :
            print('The Destroyer is sunk')
        res += 1
    if SM == 0:
        if player:
            print('The Submarine is sunk')
        res += 1
    if T == 0:
        if player:
            print('The Torpedo Boat is sunk')
        res += 1
    return res


###################################################
turn = 0  # increment by 1 each time a player shoots (0 at the start of the game)


def compute_score(grid):
    AC = 0
    C = 0
    D = 0
    SM = 0
    T = 0
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] in all_boats:
                for k in all_boats:
                    if grid[i][j] == k:
                        if k == 'AC':
                            AC += 1
                        elif k == 'C ':
                            C += 1
                        elif k == 'D ':
                            D += 1
                        elif k == 'SM':
                            SM += 1
                        elif k == 'T ':
                            T += 1
    total = 17 - AC - C - D - SM - T
    return total


def clear_terminal():
    '''None --> None
    Clears the terminal'''
    global game_mode
    # print('Clearing screen...')

    
    if game_mode == 'player vs player':
        sleep(3)
    elif game_mode == 'AI vs player':
        sleep(1)
    else:
        sleep(0)
    print('\033c\033[3J')



turn_count = 0



def save_data(score_p1, score_p2):
    '''Saves game data to a CSV file.'''

    global turn_count
    global game_mode
    global turn
    
    
    turn_count = turn_count + turn
    
    
    if game_mode == 'AI vs AI+':
        Player1 = 'AI '
        Player2 = 'AI +'
    elif game_mode == 'AI+ vs AI':
        Player1 = 'AI +'
        Player2 = 'AI '
    else:
        Player1 = 'AI_1 +'
        Player2 = 'AI_2 +'
    
    print("Saving data")
    
    with open('ai1VSai2.csv', 'a', newline='') as csvfile:
        fieldnames = ['Current turns', 'Accumulated turns', 'ScoreP1', 'Wins P1', 'ScoreP2', 'Wins P2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=' ', quotechar='|', quoting=csv.QUOTE_ALL)

        # Write header row if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write data to columns by variable name
        writer.writerow({
            'Current turns': turn,
            'Accumulated turns': turn_count,
            'ScoreP1': compute_score(player2_board),
            'Wins P1': wins1,
            'ScoreP2': compute_score(player1_board),
            'Wins P2': wins2
        })
    print("Saving data to:", os.path.abspath('ai1VSai2.csv'))


def reading_coordinates(coordinate):
    '''Str --> Tuple
    Converts coordinates into a tuple of integers'''
    if len(coordinate) == 3 and (coordinate[1] == '1' and coordinate[2] == '0'):
        c = 9
    elif len(coordinate) == 3 and (coordinate[1] == 1 and coordinate[2] == 0):
        c = 9
    elif len(coordinate) == 2:
        c = int(coordinate[1]) - 1
    l = ord(coordinate[0]) - 65
    return (l, c)


def coordinates(t):
    '''Tuple --> Str
    Converts a tuple of integers into a string representing the coordinates'''
    l = chr(t[0] + 65)
    c = str(t[1] + 1)
    if c == '10':
        c = '1' + c[1]
    return l + c


def recurse_random(list1, list2):
    '''list*list --> tuple 
    takes two lists list1 and list2 and returns a random element from list1 that is not in list2'''
    
    if list1 == []:
        return None #safety, but never verified in normal case
        
    t = random.choice(list1)
    
    if t in list2:
        list1.remove(t)
        return recurse_random(list1, list2)
    else:
        return t


wins1 = 0
wins2 = 0


def game_over(score1: int, score2: int):
    '''Int x Int x Str x Int x Int x Boolean--> None
    Ends the game and displays the winner'''
    
    global save

    

    if game_mode == 'player vs player':
        Player1 = 'Player 1'
        Player2 = 'Player 2'
    elif game_mode == 'player vs AI+':
        Player1 = 'Player'
        Player2 = 'AI+'
    elif game_mode == 'AI+ vs player':
        Player1 = 'AI+'
        Player2 = 'Player'
    elif game_mode == 'AI vs AI+':
        Player1 = 'AI '
        Player2 = 'AI +'
    elif game_mode == 'AI+ vs AI':
        Player1 = 'AI +'
        Player2 = 'AI '
    else:
        Player1 = 'AI_1 +'
        Player2 = 'AI_2 +'
    global wins1, wins2
    if score1 == 17:
        print(Player1, ' has won!')
        sleep(0)
        print('Game over')
        sleep(5)  # allow to view the game conclusion on the terminal in the case where both the players are AI
        if save:
            save_data(score1, score2)
        sleep(0)
        os.system('cls||clear')
        wins1 = wins1 + 1
        return True


    elif score2 == 17:
        print(Player2, ' has won!')
        sleep(0)
        print('Game over')
        sleep(5)  # allow to view the game conclusion on the terminal in the case where both the players are AI
        if save:
            save_data(score1, score2)
        sleep(0)
        os.system('cls||clear')
        wins2 = wins2 + 1
        return True


#############################################################


height = False
width = False


def naval_battle():
    
    global game_mode
    global player   # player is a boolean variable that is True if a human player is running the command
    global a
    global player1_shots
    global player2_shots
    global hitco
    global hitco2
    global player1_board
    global player2_board
    global turn
    global scoreP1
    global scoreP2
    global all_shots1
    global all_shots2
    global save
    global simulation

    hitco2 = []
    hitco = []  # list of tuples associated with the coordinates of the targeted ship (already hit, currently focusing on it)
    turn = 0  # variable to count the number of turns
    scoreP1 = 0
    scoreP2 = 0
    shots1 = [str(x) + str(y) for x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] for y in
           range(1, 11)]  # list of possible shots for player 1
    shots2 = [str(x) + str(y) for x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] for y in
            range(1, 11)]  # list of possible shots for player 2
    player1_shots = [['..' for j in range(10)] for i in range(10)]  # lists with player shots
    player2_shots = [['..' for j in range(10)] for i in range(10)]  #
    # start = pyip.inputMenu(['Yes', 'No'], 'Do you want to start playing Battleship? \n', numbered=True)
    

    if simulation==False :
        rules = pyip.inputMenu(['Yes', 'No'], 'Do you want a reminder of the rules? \n', numbered=True)

        if rules == 'Yes':
            webbrowser.open('https://www.regles-de-jeux.com/regle-de-la-bataille-navale/')
        print('Select the game mode you want to play')
        game_mode = pyip.inputMenu(['player vs player', 'AI vs AI+(AI goes first)',
                                      'AI+ vs AI(AI+ goes first)', 'AI+ vs AI+',
                                      'AI+ vs player(AI+ goes first)',
                                      'player vs AI+(player goes first)'], numbered=True)
        game_mode = game_mode.split('(')[0]
    
    if game_mode == 'AI+ vs AI':
        player = False
        print("AI 1 is placing its ships")
        player1_board = placement()
        clear_terminal()
        print("AI 2 is placing its ships")
        player2_board = placement()
        clear_terminal()
        player1_shots = [['..' for j in range(10)] for i in range(10)]
        player2_shots = [['..' for j in range(10)] for i in range(10)]
        all_shots1 = []  # list of tuples corresponding to all shots already fired by AI+
        all_shots2 = []  # list of tuples corresponding to all shots already fired by AI
        sunk = [0, 0]  # list where the j-th element corresponds to the number of ships sunk at turn j
        # initialized this way for the test below
        # clear_terminal()
        while True:
            if sunk[len(sunk) - 2] < sunk[ len(sunk) - 1]:  # this means a ship has just been sunk, so we reset the list
                hitco = []

            if hitco == []:  # if we are not focused on a ship, the shot is random
                a = random.choice(shots1)
                va = a
                shots1.remove(va)
                a = reading_coordinates(a)
            else:  # otherwise we shoot using a more precise algorithm
                a = next_shot(hitco, True)
                va = coordinates(a)
            if va in shots1:
                shots1.remove(va)
            all_shots1.append(a)  # we add the fired shot to the list of all shots
            J1_shot = shoot(player2_board, player1_shots)

            if J1_shot:
                # print('Hit!')
                hitco.append(a)  # we spotted a ship
            turn += 1
            update_board(player2_board, a[0], a[1], J1_shot)
            c = sink(player2_board)  # we check the number of sunk ships at time t
            sunk.append(c)
            # clear_terminal()
            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break
            #print('End of AI+ turn')
            # clear_terminal()
            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break
            a = random.choice(shots2)
            vb = a
            a = reading_coordinates(a)
            J2_shot = shoot(player1_board, player2_shots)
            #if J2_shot:
                #print('Hit!')
            all_shots2.append(a)
            turn += 1

            if vb in shots2:
                shots2.remove(vb)
            update_board(player1_board, a[0], a[1], J2_shot)

            clear_terminal()
            #print('End of AI turn')
            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break

    elif game_mode == 'player vs player':

        

        print('Player 1  places their ships')
        
        choice = pyip.inputMenu(['Yes', 'No'], 'Do you want to place your ships? \n', numbered=True)

        if choice == 'Yes':
            player = True
        else:
            player = False
        player1_board = placement()
        clear_terminal()
        
        print("Player 2's turn to place their ships")
        
        choice = pyip.inputMenu(['Yes', 'No'], 'Do you want to place your ships? \n', numbered=True)

        if choice == 'Yes':
            player = True
        else:
            player = False
        player2_board = placement()
        clear_terminal()
        
        player1_shots = [['..' for j in range(10)] for i in range(10)]
        player2_shots = [['..' for j in range(10)] for i in range(10)]
        clear_terminal()
        while True:
            print('Player 1 ship grid: \n')
            print_game_board(player1_board)
            print('Player 1 shot grid: \n')
            print_game_board(player1_shots)
            print('\n')
            sink(player2_board)

            a = pyip.inputChoice(shots1, 'Where do you want to shoot? ')

            va=a

            if va in shots1:
                shots1.remove(va)

            a = reading_coordinates(a)
            J1_shot = shoot(player2_board, player1_shots)
            if J1_shot:
                print('Hit!')
            turn += 1


            update_board(player2_board, a[0], a[1], J1_shot)

            clear_terminal()

            print('End of player 1 turn')
            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break
            clear_terminal()

            print('Player 2 ship grid: \n')
            print_game_board(player2_board)
            print('Player 2 shot grid: \n')
            print_game_board(player2_shots)
            print('\n')
            sink(player2_board)

            a = pyip.inputChoice(shots2, 'Where do you want to shoot? ')

            va = a

            if va in shots2:
                shots2.remove(va)

            a = reading_coordinates(a)
            J2_shot = shoot(player1_board, player2_shots)
            if J2_shot:
                print('Hit!')
            turn += 1


            update_board(player1_board, a[0], a[1], J2_shot)

            clear_terminal()

            print('End of player 2 turn')
            clear_terminal()
            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break



    elif game_mode == 'AI vs AI+':
        player = False

        #print("AI 1 is placing its ships")
        player1_board = placement()
        clear_terminal()
        #print("AI 2 is placing its ships")
        player2_board = placement()

        player1_shots = [['..' for j in range(10)] for i in range(10)]
        player2_shots = [['..' for j in range(10)] for i in range(10)]
        all_shots1 = []  # list of tuples corresponding to all shots already fired by AI+
        all_shots2 = []  # list of tuples corresponding to all shots already fired by AI
        sunk = [0, 0]  # list where the j-th element corresponds to the number of ships sunk at turn j

        while True:

            a = random.choice(shots1)
            va = a
            a = reading_coordinates(a)

            J1_shot = shoot(player2_board, player1_shots)
            touched = False

            turn += 1

            if va in shots1:
                shots1.remove(va)
            update_board(player2_board, a[0], a[1], J1_shot)

            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break
                
            #print('End of AI turn')

            if sunk[len(sunk) - 2] < sunk[ len(sunk) - 1 ]:  # this means a ship has just been sunk, so we reset the list
                hitco = []

            if hitco == []:  # if we are not focused on a ship, the shot is random
                a = random.choice(shots2)
                va = a
                shots2.remove(va)
                a = reading_coordinates(a)



            else:  # otherwise we shoot using a more precise algorithm
                a = next_shot(hitco, True)
                va = coordinates(a)

            if va in shots2:
                shots2.remove(va)

            all_shots1.append(a)  # we add the fired shot to the list of all shots

            J2_shot = shoot(player1_board, player2_shots)

            if J2_shot:
                # print('Hit!')
                hitco.append(a)  # we spotted a ship

            turn += 1

            update_board(player1_board, a[0], a[1], J2_shot)

            c = sink(player1_board)  # we check the number of sunk ships at time t
            sunk.append(c)

            #print('End of AI+ turn')

            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break

    if game_mode == 'AI+ vs AI+':

        player = False

        #print("AI 1 is placing its ships")
        player1_board = placement()
        clear_terminal()
        #print("AI 2 is placing its ships")
        player2_board = placement()
        clear_terminal()
        player1_shots = [['..' for j in range(10)] for i in range(10)]
        player2_shots = [['..' for j in range(10)] for i in range(10)]
        all_shots1 = []  # list of tuples corresponding to all shots already fired by AI+ 1
        all_shots2 = []  # list of tuples corresponding to all shots already fired by AI
        sunk = [0, 0]  # list where the j-th element corresponds to the number of ships sunk at turn j for AI_1+
        sunk2 = [0, 0]  # list where the j-th element corresponds to the number of ships sunk at turn j for AI_2+
        # initialized this way for the test below
        clear_terminal()
        while True:

            if sunk[len(sunk) - 2] < sunk[ len(sunk) - 1 ]:  # this means a ship has just been sunk, so we reset the list
                hitco = []

            if hitco == []:  # if we are not focused on a ship, the shot is random
                a = random.choice(shots1)
                va = a
                shots1.remove(va)
                a = reading_coordinates(a)



            else:  # otherwise we shoot using a more precise algorithm

                a = next_shot(hitco, True)
                va = coordinates(a)

            if va in shots1:
                shots1.remove(va)

            all_shots1.append(a)  # we add the fired shot to the list of all shots

            J1_shot = shoot(player2_board, player1_shots)

            if J1_shot:
                # print('Hit!')
                hitco.append(a)  # we spotted a ship

            turn += 1

            update_board(player2_board, a[0], a[1], J1_shot)

            c = sink(player2_board)  # we check the number of sunk ships at time t
            sunk.append(c)

            clear_terminal()
            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break
                
            #print('End of AI_1 + turn')

            if sunk2[len(sunk2) - 2] < sunk2[ len(sunk2) - 1]:  # this means a ship has just been sunk, so we reset the list
                hitco2 = []

            if hitco2 == []:  # if we are not focused on a ship, the shot is random
                a = random.choice(shots2)
                va = a
                shots2.remove(va)
                a = reading_coordinates(a)



            else:  # otherwise we shoot using a more precise algorithm
                a = next_shot(hitco2, False)
                va = coordinates(a)

            if va in shots2:
                shots2.remove(va)

            all_shots2.append(a)  # we add the fired shot to the list of all shots

            J2_shot = shoot(player1_board, player2_shots)

            if J2_shot:
                # print('Hit!')
                hitco2.append(a)  # we spotted a ship

            turn += 1

            update_board(player1_board, a[0], a[1], J2_shot)

            c = sink(player1_board)  # we check the number of sunk ships at time t
            sunk2.append(c)

            clear_terminal()
            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break
            #print('End of AI_2 + turn')
            clear_terminal()

    if game_mode == 'AI+ vs player':

        player = False

        print("The AI is placing its ships")
        player1_board = placement()
        clear_terminal()
        
        print('The player is placing their ships')
        
        choice = pyip.inputMenu(['Yes', 'No'], 'Do you want to place your ships? \n', numbered=True)

        if choice == 'Yes':
            player = True
        else:
            player = False
        
        player2_board = placement()
        clear_terminal()
        player1_shots = [['..' for j in range(10)] for i in range(10)]
        player2_shots = [['..' for j in range(10)] for i in range(10)]
        all_shots1 = []  # list of tuples corresponding to all shots already fired by AI+
        sunk = [0, 0]  # list where the j-th element corresponds to the number of ships sunk at turn j
        # initialized this way for the test below

        clear_terminal()
        while True:
            player = False

            print('player  shot grid: \n')
            print_game_board(player1_shots)
            print('\n')

            if sunk[len(sunk) - 2] < sunk[ len(sunk) - 1]:  # this means a ship has just been sunk, so we reset the list
                hitco = []

            if hitco == []:  # if we are not focused on a ship, the shot is random
                a = random.choice(shots1)
                va = a
                shots1.remove(va)
                a = reading_coordinates(a)



            else:  # otherwise we shoot using a more precise algorithm
                a = next_shot(hitco, True)
                va = coordinates(a)

            if va in shots1:
                shots1.remove(va)

            all_shots1.append(a)  # we add the fired shot to the list of all shots

            J1_shot = shoot(player2_board, player1_shots)

            if J1_shot:
                # print('Hit!')
                hitco.append(a)  # we spotted a ship

            turn += 1

            update_board(player2_board, a[0], a[1], J1_shot)

            c = sink(player2_board)  # we check the number of sunk ships at time t
            sunk.append(c)

            clear_terminal()
            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break
            print('End of AI+ turn')

            player = True



            print('player  ship grid: \n')
            print_game_board(player2_board)
            print('player  shot grid: \n')
            print_game_board(player2_shots)
            sink(player1_board)
            print('\n')
            a = pyip.inputChoice(shots2, 'Where do you want to shoot? ')
            sink(player1_board)

            va=a

            if va in shots2:
                shots2.remove(va)

            a = reading_coordinates(a)
            J2_shot = shoot(player1_board, player2_shots)
            if J2_shot:
                print('Hit!')
            turn += 1

            update_board(player1_board, a[0], a[1], J2_shot)

            clear_terminal()

            print('End of player  turn')
            clear_terminal()

            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break

    
    elif game_mode == 'player vs AI+':

        choice = pyip.inputMenu(['Yes', 'No'], 'Do you want to place your ships? \n', numbered=True)

        if choice == 'Yes':
            player = True
        else:
            player = False
        
        print('player places its ships')
        player1_board = placement()
        clear_terminal()
        print("The AI places its ships")
        player = False
        player2_board = placement()
        clear_terminal()
        player1_shots = [['..' for j in range(10)] for i in range(10)]
        player2_shots = [['..' for j in range(10)] for i in range(10)]
        sunk=[0,0]
        all_shots2=[]
        clear_terminal()
        while True:
            player = True
            print('Player 1 ship grid: \n')
            print_game_board(player1_board)
            print('Player 1 shot grid: \n')
            print_game_board(player1_shots)
            print('\n')
            sink(player2_board)

            a = pyip.inputChoice(shots1, 'Where do you want to shoot? ')
            va = a
            a = reading_coordinates(a)
            J1_shot = shoot(player2_board, player1_shots)

            if J1_shot:
                print('Hit!')
            turn += 1

            if va in shots1:
                shots1.remove(va)


            update_board(player2_board, a[0], a[1], J1_shot)

            clear_terminal()

            print('End of player  turn')
            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break
            clear_terminal()
            player = False
            if sunk[len(sunk) - 2] < sunk[len(sunk) - 1]:  # this means a ship has just been sunk, so we reset the list
                hitco2 = []

            if hitco2 == []:  # if we are not focused on a ship, the shot is random
                a = random.choice(shots2)
                va = a
                shots2.remove(va)
                a = reading_coordinates(a)



            else:  # otherwise we shoot using a more precise algorithm
                a = next_shot(hitco2, False)
                va = coordinates(a)

            if va in shots2:
                shots2.remove(va)

            all_shots2.append(a)  # we add the fired shot to the list of all shots

            J2_shot = shoot(player1_board, player2_shots)

            if J2_shot:
                # print('Hit!')
                hitco2.append(a)  # we spotted a ship

            turn += 1

            update_board(player1_board, a[0], a[1], J2_shot)

            c = sink(player1_board)  # we check the number of sunk ships at time t
            sunk.append(c)

            clear_terminal()
            if game_over(compute_score(player2_board), compute_score(player1_board)):
                break
            print('End of AI+ turn')
            clear_terminal()

    


def next_shot(hitco, boolean):
    global all_shots2
    global all_shots1
    all_shots = []
    if boolean:
        all_shots = all_shots1
    else:
        all_shots = all_shots2
    if len(hitco) == 1:  # if we spot a ship for the first time, we shoot around it

        x = hitco[0][0]
        y = hitco[0][1]

        if x not in (0, 9) and y not in (0, 9):
            L = [(x, y - 1), (x, y + 1), (x - 1, y),
                 (x + 1, y)]  # list of the 4 cells around the one at coordinates (x,y)

        # edge cases (board border)
        elif (x, y) == (0, 0):
            L = [(0, 1), (1, 0)]

        elif (x, y) == (9, 0):
            L = [(8, 0), (9, 1)]

        elif (x, y) == (0, 9):
            L = [(0, 8), (1, 9)]

        elif (x, y) == (9, 9):
            L = [(9, 8), (8, 9)]

        # cases with 3 surrounding cells

        elif x == 0 and y not in (0, 9):
            L = [(x, y - 1), (x, y + 1), (x + 1, y)]

        elif x not in (0, 9) and y == 9:
            L = [(x, y - 1), (x - 1, y), (x + 1, y)]

        elif x == 9 and y not in (0, 9):
            L = [(x, y - 1), (x, y + 1), (x - 1, y)]

        elif x not in (0, 9) and y == 0:
            L = [(x - 1, y), (x, y + 1), (x + 1, y)]

        shot = recurse_random(L, all_shots)

        return shot

    elif len(
            hitco) > 1:  # if we already have two coordinates, we know the ship's direction and can narrow the possibilities

        x1 = hitco[0][0]
        y1 = hitco[0][1]

        x2 = hitco[1][0]
        y2 = hitco[1][1]

        if x1 == x2:  # the ship is horizontal

            y_min = min([hitco[x][1] for x in range(len(hitco))])  # we find the min column among hit cells

            y_max = max([hitco[x][1] for x in range(len(hitco))])  # we find the max column among hit cells

            if y_min == 0 and y_max != 9:
                shot = (x1, y_max + 1)
                return shot

            elif y_min != 0 and y_max != 9:
                L = [(x1, y_min - 1), (x1, y_max + 1)]
                shot = recurse_random(L, all_shots)
                return shot

            elif y_min != 0 and y_max == 9:
                shot = (x1, y_min - 1)
                return shot

        elif y1 == y2:  # the ship is vertical

            x_min = min([hitco[x][0] for x in range(len(hitco))])

            x_max = max([hitco[x][0] for x in range(len(hitco))])

            if x_min == 0 and x_max != 9:
                shot = (x_max + 1, y1)
                return shot

            elif x_min != 0 and x_max != 9:
                L = [(x_min - 1, y1), (x_max + 1, y1)]
                shot = recurse_random(L, all_shots)
                return shot

            elif x_min != 0 and x_max == 9:
                shot = (x_min - 1, y1)
                return shot




def run_naval_battle():
    global simulation
    global save
    global game_mode
    
    mode = pyip.inputMenu(['Play', 'Simulate'], 'Do you want to play or run simulations and store the games data ? \n', numbered=True)

    if mode=='Play':
        simulation = False
        save = False
        naval_battle()
        
    else:
        game_mode = pyip.inputMenu([ 'AI vs AI+(AI goes first)',
                                      'AI+ vs AI(AI+ goes first)', 'AI+ vs AI+'], 'Which game mode ? \n', numbered=True)
        game_mode = game_mode.split('(')[0]
        save = True
        simulation = True
        n = int(input('How many simulations do you want to run ? This may take much or less of time... :'))
        for k in range(n):
            naval_battle()
        print("The game data file has been created") 
            
            
            
run_naval_battle()
        

