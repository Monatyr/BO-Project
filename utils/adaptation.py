from .const_values import *


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

    return money, happiness


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
