import matplotlib.pyplot as plt
import numpy as np
import torch

def amazon():
    plt.figure()
    ax = plt.gca()
    x = np.linspace(-5,20,100)
    a = 35/3
    y = a*np.cosh(x/a) -a
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.text(0,1, '<---------------  d  ----------------->', fontsize=20)
    plt.text(x[-1]+1,y[-1]/2,'y', fontsize=20, withdash=False)
    plt.text(x[70],y[70],'L=40', fontsize=20, withdash=False)

    plt.yticks(())
    plt.bar(x[-1],y[-1],color='k')
    plt.bar(x[-1],-2/5*y[-1],color='k')
    plt.plot(x,y)
    plt.show()

def sigmoid(x):
    return 1 / (1 + np.exp( -x))

def swish():
    plt.figure()
    ax = plt.gca()
    x = np.linspace(-6, 6, 200)

    y1 = x * (np.clip(x,-3,3)/6 + 0.5)
    y2 = x * sigmoid(x)

    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.plot(x, y1,label = 'h-swish')
    plt.plot(x, y2,label = 'swish')
    plt.legend()
    plt.show()

swish()