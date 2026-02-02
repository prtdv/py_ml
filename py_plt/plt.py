from turtle import title
import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,6,9])
y=np.array([100,150,-10])

"""#lines
plt.plot([23,54,67,8,88,9,9], '-r' )
plt.plot(x,y,'*--k')
plt.title("your mom period intensity", loc='left')
plt.xlabel("days")
plt.ylabel("period intensity")
plt.grid(axis='y')
plt.show()
"""
"""#pie
pie=np.array([45,68,89,10])
myLabels=np.array(["H","B","c","d"])
mExplode=[0.5,0,1,0]
plt.pie(pie, labels=myLabels, shadow=False, colors=["r","k","b","y"], explode=mExplode)
plt.legend(title="your mom")
plt.show()
"""

"""#bar
bar=np.array([10,20,30,5])
x=["monday","tuesday","wednesday","thursday"]

plt.bar(x,bar, color=["r"])
plt.show()"""

#scatter
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y,c=y,cmap="inferno", s=15*(y**1/2))
plt.xlabel("trials")
plt.ylabel("hotness")
plt.colorbar()
plt.title("test")
plt.show()