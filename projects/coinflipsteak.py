import random
num = 10000

def coinFlipper ():
    counter = 0
    numberOfStreaks = 0
    flips = [random.randint(0, 1) for r in range(num)]
    #count, record coin toss
    heads = 0
    tails = 0
    streak = 0
    ledger = []
    #make flips
    for object in flips:
        if object == 0:
            ledger.append('H')
            heads += 1
        elif object ==1:
            ledger.append('T')
            tails += 1

    for i in range (len(flips)):
        if i ==0:
            pass
        elif flips[i] == flips [i-1]:
            streak += 1
        else:
            streak = 0

        if streak == 7:
            numberOfStreaks +=1
    print (ledger)
    print(str(heads) + ' heads and ' +str(tails) +' tails. ')
    print('You performed: '+ str(numberOfStreaks) + ' streaks')
    print('Chance of streak: %s%%' % (numberOfStreaks/100))


coinFlipper()
