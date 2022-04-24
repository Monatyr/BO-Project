NOTHING = -1
CENTRE = 0
HOUSE = 1
FUN = 2
WORK = 3

HOUSE_COST = 25600
FUN_COST = 12800
WORK_COST = 19200

value = {}
value[(CENTRE, CENTRE)] = (0, 0)
value[(CENTRE, HOUSE)] = (0, 0)
value[(CENTRE, FUN)] = (0, 1)
value[(CENTRE, WORK)] = (1, 0)
value[(HOUSE, CENTRE)] = (0, 0)
value[(HOUSE, HOUSE)] = (0, 0)
value[(HOUSE, FUN)] = (0, 1)
value[(HOUSE, WORK)] = (1, 0)
value[(FUN, CENTRE)] = (0, 1)
value[(FUN, HOUSE)] = (0, 1)
value[(FUN, FUN)] = (0, 0)
value[(FUN, WORK)] = (0, -1)
value[(WORK, CENTRE)] = (1, 0)
value[(WORK, HOUSE)] = (1, 0)
value[(WORK, FUN)] = (0, -1)
value[(WORK, WORK)] = (0, 0)


def f(solution, city):
    money = 0
    happiness = 0
    cost = 0
    for building in solution:
        if building == CENTRE:
            pass
        elif building == HOUSE:
            cost += HOUSE_COST
        elif building == FUN:
            happiness += 1
            cost += FUN_COST
        elif building == WORK:
            happiness -= 1
            cost += WORK_COST
        else:
            print("Wrong building!")

    for (x, y) in city:
        (m, h) = value[(solution[x], solution[y])]
        money += m
        happiness += h

    if happiness < -5:
        happiness = -5
    elif happiness > 5:
        happiness = 5

    return (money, happiness, cost)

