import numpy
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns

"""#random
x=random.randint(10, size=4)
y=random.rand(5,3)
c=random.choice(x, p=[0.2,0.1,0.2,0.5] ,size=(2,4)) #random distribution, p here defines probability of each element. in 4 size array.
print(x)
print(c)

for i in c:
    random.shuffle(i) #otherwise it doesn't change inside each row, just reorders the same row.
print(c)

a=[12,34,6,8,9]
b=random.permutation(a) #same as shuffle but not inplace=True
print(a)
"""

"""s=[12,34,5,7,9,0, -100,-101,-102,-103,-200,-105]
sns.displot(s, kind="kde") #shows distribution of elements along the array."""

"""#histogram
uni=numpy.random.normal(100,200,1000) #low,high,size
nor=random.normal(100,0.5,10000) #mean,std,size.
plt.hist(nor,100) #data, no of bars in histogram.
plt.show()"""

#testing

x=random.normal(5,2,1000)
y=random.normal(100,10,1000)

plt.scatter(x,y)
plt.xlabel("x axis (maybe age of car)")
plt.ylabel("y axis (maybe speed of car)")
plt.show()