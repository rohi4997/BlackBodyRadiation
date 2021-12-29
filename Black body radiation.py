import matplotlib.pyplot as plt
import math
from array import *

x = array('f', [])
y = array('f', [])
x1 = array('f',[])
y1 = array('f',[])

h = 6.62e-34

k = 1.38e-23
c = 3e8
T = 2000
ld = 2e-7
h1= 6.62e-34

k1= 1.38e-23
c1 = 3e8
T1 = 2500
ld1= 2e-7

for i in range(300):
    r = ((8*math.pi*h*c)/math.pow(ld, 5))*(1/(math.exp((h*c)/(ld*k*T)) -1))
    x.append(ld)
    y.append(r)
    ld += 0.2e-7
    r1 = ((8*math.pi*h1*c1)/math.pow(ld1, 5))*(1/(math.exp((h1*c1)/(ld1*k1*T1)) -1))
    x1.append(ld1)
    y1.append(r1)
    ld1 += 0.2e-7



plt.plot(x, y,'--')
plt.plot(x1, y1)
plt.text(0.000001699, 15000, "T=2500K")
plt.text(0.000001599, 5500, "T=2000K")
plt.xlabel('Wavelength (in meter)')
plt.ylabel('Spectral energy density (in Joule/m^3)')
plt.title('Blackbody Radiation')
plt.show()


