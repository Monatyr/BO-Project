import copy


CENTRE = -1
NOTHING = 0
HOUSE = 1
FUN = 2
WORK = 3
HOUSE_COST = 25600
FUN_COST = 12800
WORK_COST = 19200
HAPPINESS_TIME = 0  # [0, 0.2]


def calculate(city, hapi):
    length = 0
    for (x, y) in city:
        length = max(length, x, y)
    T = [NOTHING] * (length + 1)
    T[0] = CENTRE
    max_money = 0
    max_cost = 1000000
    return_T = None
    return_money = None
    return_happiness = None
    return_real_money = None
    return_cost = None

    def create(i):
        nonlocal max_money
        nonlocal max_cost
        nonlocal return_T
        nonlocal return_money
        nonlocal return_happiness
        nonlocal return_real_money
        nonlocal return_cost
        if i == (length + 1):
            cost = 0
            money = 0
            happiness = 0
            for building in T:
                if building == HOUSE:
                    cost += HOUSE_COST
                if building == FUN:
                    cost += FUN_COST
                    happiness += 1
                elif building == WORK:
                    cost += WORK_COST
                    happiness -= 1
            for (start, end) in city:
                if (T[start], T[end]) == (CENTRE, CENTRE):
                    pass
                elif (T[start], T[end]) == (CENTRE, HOUSE):
                    pass
                elif (T[start], T[end]) == (CENTRE, FUN):
                    happiness += 1
                elif (T[start], T[end]) == (CENTRE, WORK):
                    money += 1
                elif (T[start], T[end]) == (HOUSE, CENTRE):
                    pass
                elif (T[start], T[end]) == (HOUSE, HOUSE):
                    pass
                elif (T[start], T[end]) == (HOUSE, FUN):
                    happiness += 1
                elif (T[start], T[end]) == (HOUSE, WORK):
                    money += 1
                elif (T[start], T[end]) == (FUN, CENTRE):
                    happiness += 1
                elif (T[start], T[end]) == (FUN, HOUSE):
                    happiness += 1
                elif (T[start], T[end]) == (FUN, FUN):
                    pass
                elif (T[start], T[end]) == (FUN, WORK):
                    happiness -= 1
                elif (T[start], T[end]) == (WORK, CENTRE):
                    money += 1
                elif (T[start], T[end]) == (WORK, HOUSE):
                    money += 1
                elif (T[start], T[end]) == (WORK, FUN):
                    happiness -= 1
                elif (T[start], T[end]) == (WORK, WORK):
                    pass
                else:
                    raise Exception("Wrong definition of edges!")
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
            real_money = round(real_money, 2)
            if happiness == hapi:
                if real_money >= max_money:
                    if real_money == max_money and cost < max_cost:
                        max_cost = cost
                        #print(T, (money, happiness), "==", real_money, "with", cost)
                        return_T = copy.deepcopy(T)
                        return_money = money
                        return_happiness = happiness
                        return_real_money = real_money
                        return_cost = cost
                    elif real_money > max_money:
                        max_money = real_money
                        max_cost = cost
                        #print(T, (money, happiness), "==", real_money, "with", cost)
                        return_T = copy.deepcopy(T)
                        return_money = money
                        return_happiness = happiness
                        return_real_money = real_money
                        return_cost = cost
        else:
            T[i] = HOUSE
            create(i + 1)
            T[i] = FUN
            create(i + 1)
            T[i] = WORK
            create(i + 1)

    create(1)
    print(return_T, (return_money, return_happiness), "==", return_real_money, "with", return_cost)


city_gos = [(1, 2),
        (2, 0),
        (2, 3),
        (3, 0),
        (3, 4),
        (3, 5),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 0),
        (0, 8),
        (0, 10),
        (8, 10),
        (8, 9),
        (10, 9),
        (10, 11)]
city_rel = [(1, 2),
            (1, 3),
        (2, 0),
        (2, 3),
        (3, 0),
        (3, 4),
        (4, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (6, 0),
        (7, 8),
        (0, 8),
        (0, 9),
        (8, 9),
        (9, 10),
        (9, 11)]
city_woj = [(1, 2),
            (2, 3),
            (4, 5),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0)]
city_mac =[(1, 2),
           (2, 3),
           (1, 3),
           (3, 0),
           (3, 4),
           (4, 0),
           (4, 5),
           (4, 6),
           (4, 8),
           (5, 6),
           (6, 7),
           (7, 8),
           (8, 9),
           (9, 10),
           (8, 10),
           (0, 10),
           (10, 11)]
city_kos = [(1, 2),
             (2, 3),
             (3, 4),
             (4, 5),
             (4, 6),
             (5, 6),
             (6, 7),
             (7, 8),
             (7, 9),
             (8, 9),
             (9, 10),
             (10, 11),
             (2, 11),
             (0, 2),
             (0, 3),
             (0, 5),
             (0, 8),
             (0, 10)]
city_idk = [(1, 2),
            (2, 3),
            (3, 4),
            (2, 4),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 8),
            (7, 9),
            (6, 10),
            (10, 11),
            (0, 4),
            (0, 5),
            (0, 6),
            (0, 10)]
city_idk2 = [(1, 2),
             (1, 3),
             (1, 4),
             (4, 5),
             (4, 6),
             (5, 6),
             (6, 7),
             (7, 8),
             (7, 9),
             (7, 10),
             (9, 10),
             (10, 11),
             (0, 1),
             (0, 4),
             (0, 6),
             (0, 7),
             (0, 10)]
city_idk3 = [(1, 2),
             (2, 3),
             (1, 3),
             (3, 4),
             (4, 5),
             (4, 6),
             (5, 6),
             (6, 7),
             (4, 8),
             (7, 8),
             (8, 9),
             (8, 10),
             (9, 10),
             (9, 11),
             (0, 3),
             (0, 4),
             (0, 9)]
city_idk4 = [(1, 2),
             (2, 3),
             (3, 4),
             (4, 5),
             (5, 6),
             (6, 7),
             (7, 8),
             (8, 9),
             (7, 9),
             (7, 10),
             (10, 11),
             (0, 3),
             (0, 6),
             (0, 7),
             (0, 10)]



for hap in range(-5, 5+1):
    calculate(city_kos, hap)

