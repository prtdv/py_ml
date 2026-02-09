#check out np.mean np.median and stats.mode, easy. also, checkout, np.percentile(arr,%ile) #returns the arr value at that %ile
#check out np.random.normal(mean,std,size) distribution and plt.hist(arr,no.of.bars). also you alr know plt.scatter(x,y)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

#prereq (using random.normal and scatter)
"""x=np.random.normal(5,2,1000) #np.random.normal(mean,std,size)
y=np.random.normal(100,10,1000)

plt.scatter(x,y)
plt.xlabel("x axis (maybe age of car)")
plt.ylabel("y axis (maybe speed of car)")
plt.show()
"""

"""#linear regression (relation between data points)
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope,intercept,r,p,stdErr=stats.linregress(x,y) 
#r is the coefficient of correlation. r range: (-1,1), 0 means no relation (chopped), 1/-1 means 100% related.
print(r) #here, -0.76, there is a relation but not strong. can be used for linregress tho.

def regPoints(x):
    return slope*x+intercept

regressionLine=list(map(regPoints,x))

#prediction test
print("speed of a car 10yo as predicted is: ",regPoints(7))

plt.scatter(x,y)
plt.plot(x,regressionLine)
plt.xlabel("age")
plt.ylabel("speed")
plt.grid()
plt.show()"""

#polynomial regression (ahhhh we curving polynomially now)
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(x, y)
plt.show()
