import subprocess
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt

path=r'C:\Users\Administrator\Desktop\guess_windows.exe'
rc=subprocess.Popen(path,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
x=np.linspace(0,1,10001)
for i in x:
    rc.stdin.writelines(str(i))

a=rc.communicate()[0].split('\n')
a=a[:len(a)-1]
y=list(map(float,a))
f2=interp1d(x[::2],y[::2],kind='cubic')
y2=f2(x[1::2])
print(y2-np.array(y[1::2]))
plt.plot(x[1::2],y2,'b--',label='cubic')
plt.show()





'''

'''
