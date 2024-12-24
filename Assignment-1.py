import numpy as np 
import matplotlib.pyplot as plt 

#y = wx + b; where 'w' and 'b' are constants

x_values = np.arange(-10,10,0.1)

def func_1(w,x,b):
    return w*x+b

w = 1
b = 2

plt.figure(figsize=(12,10))

Function1 = func_1(w,x_values,b)
plt.subplot(3,3,1)
plt.plot(x_values,Function1,label = "y = wx+b")
plt.title("y = wx+b")
plt.legend()
plt.grid()
plt.tight_layout()
#plt.show()


#y = x^2

def func_2(x):
    return x*x

Function2 = func_2(x_values)
plt.subplot(3,3,2)
plt.plot(x_values,Function2,label = "y = x^2")
plt.title("y = x^2")
plt.legend()
plt.grid()
plt.tight_layout()
#plt.show()


#y = 1/ (1 + e^(-x)); where ^ means 'to the power'.

def func_3(x):
    return 1 / (1 + np.exp(-x))

Function3 = func_3(x_values)
plt.subplot(3,3,3)
plt.plot(x_values,Function3,label = "y = 1/(1+exp(-x))")
plt.title("y = 1/(1+exp(-x))")
plt.legend()
plt.grid()
plt.tight_layout()
#plt.show()


#y = (e^x - e^(-x)) / (e^x - e^(-x))

def func_4(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) - np.exp(-x))

Function4 = func_4(x_values)
plt.subplot(3,3,4)
plt.plot(x_values,Function4,label = "y = e^x - e^-x / e^x - e^-x")
plt.title("y = y = e^x - e^-x / e^x - e^-x")
plt.legend()
plt.grid()
plt.tight_layout()
#plt.show()

#y = g(f(x)) where u = f(x) = wx + b and y = g(u) = 1/ (1 + e^(-u))

def func_5(x_values,w,b):
    return (1 / (1 + np.exp(-(x_values*w+b))))

Function5 = func_5(x_values,w,b)
plt.subplot(3,3,5)
plt.plot(x_values,Function5,label = "g(u) = 1/(1+e^(-u))")
plt.title("g(u) = 1/(1+e^(-u))")
plt.legend()
plt.grid()
plt.tight_layout()
#plt.show()

#y = g(f(x)) where f(x) = wx + b, u = f(x), and g(u) = (e^u - e^(-u)) / (e^u + e^(-u))

def func_6(x_values,w,b):
    u = w*x_values+b
    return (np.exp(u) - np.exp(-u)) / (np.exp(u) + np.exp(-u))

Function6 = func_6(x_values,w,b)
plt.subplot(3,3,6)
plt.plot(x_values,Function6,label = "g(u) = e^u - e^(-u)) / (e^u + e^(-u)")
plt.title("g(u) = e^u - e^(-u)) / (e^u + e^(-u)")
plt.legend()
plt.grid()
plt.tight_layout()
#plt.show()


def func_7(x_values,b):
    w1 = 1
    w2 = 2
    w3 = 3
    w4 = 4
    b1 = 1
    b2 = 2

    u1 = w1 * x_values + b1
    y1 = 1 / (1 + np.exp(-u1))

    u2 = w2 * x_values + b2
    y2 = 1 / (1 + np.exp(-u2))

    y = w3 * y1 + w4 * y2 + b

    return (1 / (1 + np.exp(-y)))

Function7 = func_7(x_values,b)
plt.subplot(3,3,7)
plt.plot(x_values,Function7,label = "g(u) =  1/ (1 + e^(-w)")
plt.title("g(u) =  1/ (1 + e^(-w)")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()


