import math

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,2,200)
y1 = []
y2 = []
for i in x:
    y1.append(-math.sin(i)-i)
    y2.append(-math.sin(i-2)-(i-2))
fig, ax = plt.subplots()

m = (y1[-1]+y2[-1])/2

ax.plot(x,y1,'r-')
ax.plot(x,y2,'b-')
ax.plot(2,m,'ko')
plt.show()