
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0, 2*np.pi, num=1000)
y=5.5*np.sin(2*x)+5.5
z=0.02*np.exp(x)
w=0.25*x**2 + 0.1*np.sin(10*x)

def graph_function(a,b,c,d):
    plt.plot(a,b)
    plt.plot(a,c)
    plt.plot(a,d)
    plt.xlim([0,2*np.pi])
    plt.ylim([-1,10])
    plt.xlabel("Time in ASTR 119")
    plt.ylabel("Measure of Awesomeness")
    plt.show()
graph_function(x,y,z,w)