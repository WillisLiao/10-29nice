def ez(v1):
    a=0
    b=0
    while a<=100000:
        b+=1
        a=v1**(b)
    print(b)

ez(int(input()))
    
    