import numpy as np
from numpy import *
pocet_strel = 100
suma1 = 0
suma3 = 0
def f(x,y):
    return x*x + y*y

def g(X, parameters=(1, 100)):
    x, y = X
    a, b = parameters
    return (a - x)**2 + b * (y - x * x)**2

def h(X):
    """ 4D test function """
    s, t, u, v = X
    sum2 = s*s + t*t + u*u + v*v
    if sum2 > 2:
        return float("inf")
    return 0.25 * sum2 - 0.5 * ((s*s + t*t) * (2 - sum2) + (s*u - t*v)**2) + 0.5 * s * np.sqrt(2 - sum2)


def r(X, parameters=(1,)):
    x, y = X
    a, = parameters
    return x**4 - 2 * x*x + a * x + y*y

def l(x):
    return np.exp(-x)*np.sin(x)

def s(x):
    return np.sin(x**2)/np.sqrt(1+x**4)


def proc(f):
    for i in range(pocet_strel):
        x = np.random.uniform(0,2*np.pi)
        #y = np.random.uniform(0,1)
        suma1 += l(x)



    for i in range(pocet_strel):
        x = np.random.uniform(0,np.sqrt(10*np.pi))
        #y = np.random.uniform(0,1)
        suma3 += s(x)
    #vypocet
    a = suma1/(pocet_strel*2*np.pi)
    b = suma3/(pocet_strel*np.sqrt(10*np.pi))
    return a
    print(a,b)