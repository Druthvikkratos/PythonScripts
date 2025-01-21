import numpy as np
from scipy import stats # type: ignore
import matplotlib.pyplot as plt # type: ignore

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope * x + intercept

myModel = list(map(myfunc, x))
#scatter
#x = numpy.random.normal(5.0, 1.0, 1000)
# = numpy.random.normal(10.0, 2.0, 1000)

mean1 = np.mean(speed)
median = np.median(speed)
mode = stats.mode(speed)
std = np.std(speed)
var = np.var(speed)
ages = np.percentile(ages, 75)
random = np.random.uniform(0.0, 5.0, 1000)
random2 = np.random.normal(5.0, 1.0, 100000)
#print(f"mean {mean1}")
#print(f"median {median}")
#print(f"mode {mode}")
#print(f"standard deviation {std}")
#print(f"variance {var}")
#print(f"percentage {ages}")
#print(f"random {random}")
#plt.hist(random, 100)
#plt.hist(random2, 100)
plt.scatter(x, y)
plt.plot(x, myModel)
plt.show()