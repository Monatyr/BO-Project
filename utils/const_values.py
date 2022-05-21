NOTHING = -1
CENTRE = 0
HOUSE = 1
FUN = 2
WORK = 3

HAPPINESS_TIME = 0.1  # [0, 0.2]

HOUSE_COST = 25600
FUN_COST = 12800
WORK_COST = 19200
COSTS = [0, HOUSE_COST, FUN_COST, WORK_COST]

value = dict()

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


city_kos = [
    (1, 2),
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
    (0, 10)
]
