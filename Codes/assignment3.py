
import numpy as np
import matplotlib.pyplot as plt
x1=np.linspace(-2,0,2)
y1=np.linspace(0,0,2)
x2=np.linspace(0,1,1000)
y2=x2 ** 2
x3=np.linspace(1,2,2)
y3=np.linspace(1,1,2)
plt.plot(x1,y1,color="green")
plt.plot(x2,y2,color="green")
plt.plot(x3,y3,color="green")
plt.xlabel("value of x")
plt.ylabel("$F_{X}(x)$=CDF")
plt.xticks(np.arange(-2,2,0.5))
plt.title("Plot of CDF of random variable X")
plt.show()