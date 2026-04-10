def recurse_random(list1, list2):
    '''list*list --> tuple 
    takes two lists list1 and list2 and returns a random element from list1 that is not in list2'''
    

    if list1==[]:
        return None  #safety case, but never verified in normal time
    
    t = random.choice(list1)
    
    if t in list2:
        list1.remove(t)
        return recurse_random(list1, list2)
    else:
        return t
        
        
        
        
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
