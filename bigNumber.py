def bigNumber():
    x=2
    y=2
    while type(x**y) is int:
        print(x)
        x=x**y
    print(x)
    while type(x*y) is int:
        x=x*y
        y+=1
    print(x)
    y=1
    while type(x+y) is int:
        x=x+y
        y+=1
    print(x)
    y=1
    while type(x+1) is int:
        x=x+1
        y+=1
    y=1
    print(x)
    return x
    

    
    
#if:
#   type(number) is int
