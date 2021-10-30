def fun(n,b):
    list1=[]
    while True:
        n,remider = divmod(n,b)
        list1.append(str(remider))
        if n==0:
            return"".join(list1[::-1])

c = int(input())
