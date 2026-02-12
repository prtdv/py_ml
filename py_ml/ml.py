#check out np.mean np.median and stats.mode, easy. also, checkout, np.percentile(arr,%ile) #returns the arr value at that %ile
#check out np.random.normal(mean,std,size) distribution and plt.hist(arr,no.of.bars). also you alr know plt.scatter(x,y)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import sklearn
from sklearn.metrics import r2_score

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

"""#polynomial regression (ahhhh we curving polynomially now)
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

#slope,intercept,r,p,stdErr=stats.linregress(x,y). here r=0.42, chopped for linregress, trying polyregress here.

mymodel = np.poly1d(np.polyfit(x, y, 3)) #we took a 3rd degree as it bends twice and we kinda guessed it to be that on seeing the scatter plot.
#np.polyfit(x, y, 3) here 3 is the degree of curve we're expecting. returns [a,b,c,d] coefficients array of that curve.
#np.poly1d([coeff. array]) wraps those coefficient into a callable func f(x) = ax³ + bx² + cx + d. that's why later we did mymodel(input)
##poly1d means polynomial in 1 dependent var. here it's x.
# mymodel is same as mymodel([pointArray]) which returns y=ax**3 + bx**2 + cx + d for each point in array.

#https://chatgpt.com/s/t_698a351bdf3c8191a72de24abbbe60a4, only this can save me.

#check r2
print(r2_score(y,mymodel(x))) #used to evaluate regression quality. range =[0,1], 1 is perfect fit, 0 is hell no.

myline = np.linspace(x[0], x[-1], 100) #smooth x-values for plotting, as in it creates 100 evenly spaced x values

#prediction test
print("my predicted value at 25 is: ", mymodel(25))

plt.scatter(x, y)
plt.plot(myline, mymodel(myline)) #mymodel(myline) returns y for each x in myline in 1 array.
plt.grid()
plt.show()"""

"""#multiple regression.
df = pd.read_csv("data.csv")

X = df[['Weight', 'Volume']] #independent vars
y = df['CO2'] #dependent var.

 #model fitting = model learning and regression function extraction
regr = sklearn.linear_model.LinearRegression()
regr.fit(X, y)
print(regr.coef_) #y=a.x + b, gets a and b.

#prediction test
predictedCO2 = regr.predict([[3300, 1300]]) #get predicted y for x's

print(predictedCO2)"""

#feature scaling
df=pd.read_csv("data.csv")
df["Volume"]=df["Volume"]/1000 #now our fuel is cm3, 1 instead of 1000
from sklearn.preprocessing import StandardScaler

scale=StandardScaler()

X=df[["Weight","Volume"]]
y=df["CO2"]

scaledX=scale.fit_transform(X) #.fit_transform is combination of .fit (learns mean and std of all inps) and .transform (does the transformation)
print(scaledX)

myModel=sklearn.linear_model.LinearRegression()
myModel.fit(scaledX,y) #the model is trained on scaled features, not raw df
#also now the model expects inputs in the form of [scaled_weight, scaled_volume] and not raw [2300, 1.3] in our df

weight_kg=2300
vol_cm3=1.3
#to predict, we now need scaled inps to our model trained on scaled values.
scaledinput = scale.transform([[weight_kg, vol_cm3]]) 
#.transform only because we dont need to relearn scaling from one new sample.

predictedCO2=myModel.predict(scaledinput) #regr.predict([[2300, 1.3]])  ❌ WRONG, it needs scaled inputs 
print("predicted CO2 at scaled weight",weight_kg,"and scaled volume",vol_cm3,"is: ",predictedCO2)

