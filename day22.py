import copy
import math

#        [    0    |  1   |   2    |  3    |  4   |   5  ]
#spell = [spell id | mana | damage | armor | mana | timer]
spells = [(0, 53, 4, 0, 0, 0), (1, 73, 2, 2, 0, 0), (2, 113, 0, 0, 0, 6), (3, 173, 3, 0, 0, 6), (4, 229, 0, 0, 101, 5)]

#2 = Shield

#timer = [spell id, turns left]
bossDamage = 9
Inf = 100000
best = Inf
def minManaToWin(me, boss, mana, manaUsed, timers, myMove):
    #print(me, boss, mana, manaUsed, timers, myMove)
    global spells, bossDamage, Inf, best

    if me > 0 and boss <= 0:
        #win
        print(manaUsed)
        best = min(best, manaUsed)
        return 0

    if me <= 0:
        return Inf

    if manaUsed > best:
        return Inf

    if myMove:
        me -= 1
        if me <= 0:
            return Inf

    #apply timers
    shieldOn = False
    new_timers = []
    for timer in timers:
        if timer[0] == 2:
            shieldOn = True
        spell = spells[timer[0]]
        mana += spell[4]
        me += spell[3]
        boss -= spell[2]
        if timer[1] > 1:
            new_timers += [[timer[0], timer[1] - 1]]

    if me > 0 and boss <= 0:
        #win
        print(manaUsed)
        best = min(best, manaUsed)
        return 0

    res = Inf
    if myMove:
        for spell in spells:
            if spell[1] <= mana:
                if spell[5] == 0:
                    #immediately
                    tmp = minManaToWin(me + spell[3], boss - spell[2], mana - spell[1], manaUsed + spell[1], new_timers, False)
                    res = min(res, tmp + spell[1])
                else:
                    inUse = False
                    for t in new_timers:
                        if t[0] == spell[0]:
                            #already appled spell
                            inUse = True
                            break
                    if inUse:
                        continue
                    #add timer
                    tmp = minManaToWin(me, boss, mana - spell[1], manaUsed + spell[1], new_timers + [[spell[0], spell[5]]], False)
                    res = min(res, tmp + spell[1])
    else:
        #boss' move
        myArmor = 7 if shieldOn else 0
        me -= bossDamage - myArmor
        tmp = minManaToWin(me, boss, mana, manaUsed, new_timers, True)
        res = min(res, tmp)
    return res


result = minManaToWin(50, 51, 500, 0, [], True)
print ('res =', result)
