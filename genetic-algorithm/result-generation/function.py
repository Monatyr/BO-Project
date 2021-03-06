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
    for building in solution:
        if building == NOTHING:
            pass
        elif building == CENTRE:
            pass
        elif building == HOUSE:
            pass
        elif building == FUN:
            happiness += 1
        elif building == WORK:
            happiness -= 1
        else:
            print("Wrong building!")

    for (x, y) in city:
        (m, h) = value[(solution[x], solution[y])]
        money += m
        happiness += h

    """if happiness < -5:
        happiness = -5
    elif happiness > 5:
        happiness = 5
"""
    return (money, happiness)


def cost(solution):
    c = 0
    for building in solution:
        if building == NOTHING:
            pass
        elif building == CENTRE:
            pass
        elif building == HOUSE:
            c += HOUSE_COST
        elif building == FUN:
            c += FUN_COST
        elif building == WORK:
            c += WORK_COST
        else:
            print("Wrong building!")
    return c


def buildings(solution):
    n = 0
    for building in solution:
        if building == NOTHING:
            pass
        elif building == CENTRE:
            pass
        elif building == HOUSE:
            n += 1
        elif building == FUN:
            n += 1
        elif building == WORK:
            n += 1
        else:
            print("Wrong building!")
    return n


def f(money, happiness):
    if happiness < -5:
        happiness = -5
    elif happiness > 5:
        happiness = 5
    if happiness < 0:
        real_money = (1 + HAPPINESS_TIME * happiness) * money - HAPPINESS_TIME * happiness * money / 2
    elif happiness > 0:
        real_money = (1 - HAPPINESS_TIME * happiness) * money + HAPPINESS_TIME * happiness * money * 2
    else:
        real_money = money
    return real_money