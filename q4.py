n=int(input())

def fun(x):
    if x>1:
        return fun(x-1) + fun(x//2)
    else:
        return x+1
print(fun(n))