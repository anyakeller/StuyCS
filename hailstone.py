def hail(n):
    t = 0
    x = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else: 
            n = 3*n + 1
        t += 1
        print (n)
        if n > x:
            x = n
    return "step is " + str(t) + " highest is " + str(x)
    

        
