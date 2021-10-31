import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

def fun1(x):
    return 12-5*x

def fun2(x):
    return 3-0.5*x

def fun3(x):
    return 1/4*28-7/4*x

def fun4(x):
    return 1/4*22-7/4*x
x = Symbol('x')
x1,= solve(fun1(x)-fun2(x))     # ask ,
y1= fun1(x1)

plt.plot(x1, fun1(x1), 'go', markersize = 10)   #'go' green and circle dot
plt.plot(0, 0, 'go', markersize = 10)
plt.plot(12/5, 0, 'go', markersize=10)
plt.plot(0, 3, 'go', markersize = 10)

plt.fill([x1, 12/5, 0, 0], [y1, 0, 0, 3], 'red', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
xr = np.linspace(0, 12, 100)
y1r = fun1(xr)
y2r = fun2(xr)
y3r = fun3(xr)
y4r = fun4(xr)
plt.plot(xr,y1r,'b-')   #b是blue , -是實線
plt.plot(xr,y2r,'g-')
plt.plot(xr,y3r, 'r-')
plt.plot(xr,y4r, 'm-')    # m magenta
plt.text(1,8,'y=12-5x', fontsize= 12,color='blue')
plt.text(5,1,'y=3-0.5x',fontsize=12, color='green')
plt.text(2.2, 3.5, 'y=1/4*28-7/4*x', fontsize= 12, color='red')
plt.text(0.5, 5.2,'y=1/4*22-7/4*x',fontsize=12,color='purple')
str1 = '({:.1f},{:.1f})'.format(x1, y1)
plt.text(2.2, 2.2, str1, fontsize=12, color= 'green')
plt.xlim(0,12)
plt.ylim(0,12)

plt.show()