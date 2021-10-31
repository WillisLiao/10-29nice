def fun(n,b):
    list1=[]
    while True:
        n,remider = divmod(n,b)
        list1.append(str(remider))
        if n==0:
            return"".join(list1[::-1])

v1,v2= map(int,input().split())


print("{:0>13}".format(fun(v1,v2)))