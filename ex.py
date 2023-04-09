
import math as math
import matplotlib.pyplot as plt


a = 2
y = 2
x = 1
abserr = 1.0E-5
#
# program glowny
#
myx = []
myy = []
iter = 1
while iter <= 10:
    xnew = x/2 + 0.5*a/x
    myx.append(iter)
    myy.append(xnew)
    if abs(xnew-x) < abserr:
        x = xnew
        break
    else:
        x = xnew
        iter += 1
#
print(f"sqrt({a}) = {xnew:.5g} error = {xnew - a**0.5:.5g} iter = {iter}")
import matplotlib.pyplot as plt
plt.plot(myx, myy)
plt.show()