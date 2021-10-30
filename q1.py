
def monkey(a,b):
    while a<=10:
        a+=1
        bear(a)

def bear(n): 
    var = False
    bool = False       
    for i in range(1,n):
        sum=0
        for j in range(i,n):
            sum+=j
            if(sum==n):
                bool=True
                for k in range(i,j):
                    print('{}+'.format(k),end="")
                print(j)
    if bool==var:
            print("NO")

monkey(a=int(input()),b=int(input()))