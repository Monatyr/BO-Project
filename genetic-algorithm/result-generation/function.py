from consts import *

value = {}

value[(NOTHING, NOTHING)] = (0, 0)
value[(NOTHING, CENTRE)] = (0, 0)
value[(NOTHING, HOUSE)] = (0, 0)
value[(NOTHING, FUN)] = (0, 0)
value[(NOTHING, WORK)] = (0, 0)

value[(CENTRE, NOTHING)] = (0, 0)
value[(CENTRE, CENTRE)] = (0, 0)
value[(CENTRE, HOUSE)] = (0, 0)
value[(CENTRE, FUN)] = (0, 1)
value[(CENTRE, WORK)] = (1, 0)

value[(HOUSE, NOTHING)] = (0, 0)
value[(HOUSE, CENTRE)] = (0, 0)
value[(HOUSE, HOUSE)] = (0, 0)
value[(HOUSE, FUN)] = (0, 1)
value[(HOUSE, WORK)] = (1, 0)

value[(FUN, NOTHING)] = (0, 0)
value[(FUN, CENTRE)] = (0, 1)
value[(FUN, HOUSE)] = (0, 1)
value[(FUN, FUN)] = (0, 0)
value[(FUN, WORK)] = (0, -1)

value[(WORK, NOTHING)] = (0, 0)
value[(WORK, CENTRE)] = (1, 0)
value[(WORK, HOUSE)] = (1, 0)
value[(WORK, FUN)] = (0, -1)
value[(WORK, WORK)] = (0, 0)


def data(solution, city):
    money = 0
    happiness = 0
    cost = 0
    buildings = 0
    for building in solution:
        if building == NOTHING:
            pass
        elif building == CENTRE:
            pass
        elif building == HOUSE:
            cost += HOUSE_COST
            buildings += 1
        elif building == FUN:
            happiness += 1
            cost += FUN_COST
            buildings += 1
        elif building == WORK:
            happiness -= 1
            cost += WORK_COST
            buildings += 1
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

    return (money, happiness, buildings, cost)


def f(money, happiness, buildings, cost):
    if happiness < 0:
        real_money = (1 + HAPPINESS_TIME * happiness) * money - HAPPINESS_TIME * happiness * money / 2
    elif happiness > 0:
        real_money = (1 - HAPPINESS_TIME * happiness) * money + HAPPINESS_TIME * happiness * money * 2
    else:
        real_money = money
    return real_money