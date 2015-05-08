def Esrever(l):
    x = 0
    for thing, IDK in enumerate(l):
        new =''
        x = len(IDK) - 1
        while x >= 0:
            new += IDK[x]
            x -= 1
        l[thing] = new
    print l
    
Esrever(['swag','yolo','stuypulse'])
