import numpy 

np= numpy.array([1,2,4,56,78,9,6,7])
np2=numpy.array([[1,2,4],[5,0,6],[7,9,56],[0,0,0],[56,67,24]], dtype='i2')
np3=numpy.array(['arr','hello','world'])
arr = numpy.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

""" dims and slicing 
print(np.ndim)
print(np[1:-2])
print(np2[1,0:-1])
"""

""" types
print('fr? ', np2.dtype)

newnp=np2.astype('f')
print(newnp)
print(newnp.dtype)

newnp=np2.astype('?')
print(newnp)
print(newnp.dtype)
"""

""" copy v view
npc=np.copy()
print('copy check')
print(np)
print(npc[2])
npc[2]=7
print(npc)
print(np)

print('view here')
x=np.view()
print(x)
print(np)

x[1]=0
print(x)
print(np)

print('npc base check', npc.base) #returns None cause it owns the array, no base
print('x base check', x.base) #returns the base array"""

""" shape and reshape
print(np2.shape)
n2=np.reshape(4,1,-1)
print(n2)

n1=np2.reshape(-1)
print(n1)"""

""" iteration w/o nditer

for i in arr:
    print(f"in {i}")
    for x in i:
        print(f"there's {x} of {i}")
        for y in x:
            print(f"here's {y} of {x}")
        print("\n")

for n, i in numpy.ndenumerate(arr): #indexing and printing as a 1d arr
    print(n, i)"""

"""concatenate and stacking
ar1=numpy.array([[1,23,4],[6,7,8],[712,5,7]])
ar2=numpy.array([[4,65,7],[67,6,1],[45,7,1]])
ar3=numpy.array([[5,5,7],[6,69,10],[458,789,100]])


a=numpy.concatenate((ar1,ar2,ar3),axis=1) #change axis, 0 for along x axis, 1 for along y axis. no change in dimensions.
print(ar1.shape, ar2.shape, ar3.shape)
print(a)
print(a.shape)

b=numpy.stack((ar1,ar2,ar3),axis=1) #creates a b.ndim=3 array, (n,arx.shape) array where n= no. of elements in each one of arrays being stacked. axis 0 for simple x axis stacking, one array elements and then next. axis=1 for new row to have elements from the next array (y axis stacking) (fuck it, just run and test)
print(ar1.shape, ar2.shape,ar3.shape) 
print(b)
print(b.shape)"""

"""split
y=numpy.array_split(np2,2 #how many splits to do, axis=1) #axis changes how the array would be split, ndim remains the same, no idea about shape, can never really.
print(y)"""

rr = numpy.array([1, 2, 3, 4, 5, 4, 4])

"""where
xp=numpy.where(np2==0) #returns 2 arrays, 1 for row index, 1 for column index
print(xp)"""

print(numpy.__version__ )
