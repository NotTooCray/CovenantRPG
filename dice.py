import random
dice = random.randint(1, 6)
y = dice
re = input('Press Y to roll again')
if dice == 1:
    print("[-----]")
    print("[     ]")
    print("[  0  ]")
    print("[     ]")
    print("[-----]")
if dice == 2:
    print("[-----]")
    print("[ 0   ]")
    print("[     ]")
    print("[   0 ]")
    print("[-----]")
if dice == 4:
    print("[-----]")
    print("[0   0]")
    print("[     ]")
    print("[0   0]")
    print("[-----]")
if dice == 5:
    print("[-----]")
    print("[0   0]")
    print("[  0  ]")
    print("[0   0]")
    print("[-----]")
if dice == 6:
    print("[-----]")
    print("[0 0 0]")
    print("[     ]")
    print("[0 0 0]")
    print("[-----]")
