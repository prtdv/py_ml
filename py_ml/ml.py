#check out np.mean np.median and stats.mode, easy. also, checkout, np.percentile(arr,%ile) #returns the arr value at that %ile
#check out np.random.normal(mean,std,size) distribution and plt.hist(arr,no.of.bars). also you alr know plt.scatter(x,y)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import sklearn
from sklearn.metrics import r2_score

"""#prereq (using random.normal and scatter)
x=np.random.normal(5,2,1000) #np.random.normal(mean,std,size)
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
print(r2_score(y,mymodel(x))) #used to evaluate regression quality. range =(-infinity,1], 1 is perfect fit, 0 is just mean, -ve means kill yourself

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

"""#feature scaling

df=pd.read_csv("data.csv")
df["Volume"]=df["Volume"]/1000 #now our fuel is cm3, 1 instead of 1000
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
scale=StandardScaler()

X=df[["Weight","Volume"]]
y=df["CO2"]

scaledX=scale.fit_transform(X) #.fit_transform is combination of .fit (learns mean and std of all inps) and .transform (does the transformation)
print(scaledX)

myModel=LinearRegression()
myModel.fit(scaledX,y) #the model is trained on scaled features, not raw df
#also now the model expects inputs in the form of [scaled_weight, scaled_volume] and not raw [2300, 1.3] in our df

weight_kg=2300
vol_cm3=1.3
#to predict, we now need scaled inps to our model trained on scaled values.
scaledinput = scale.transform([[weight_kg, vol_cm3]]) 
#.transform only because we dont need to relearn scaling from one new sample.

predictedCO2=myModel.predict(scaledinput) #regr.predict([[2300, 1.3]])  ❌ WRONG, it needs scaled inputs 
print("predicted CO2 at scaled weight",weight_kg,"and scaled volume",vol_cm3,"is: ",predictedCO2)"""

"""#train/test
#80% train, 20% test

np.random.seed(2) #makes results reprocable

x=np.random.normal(3,1,100)
y=np.random.normal(150, 40, 100)/x

trainx=x[:80]
trainy=y[:80]

testx=x[80:]
testy=y[80:]

myModel=np.poly1d(np.polyfit(trainx,trainy,4)) #possible overfitting

#remember, r2 checks fitting of data with our regression curve.
print("train r2: ",r2_score(trainy,myModel(trainx))) #train r2:  0.7988645544629797, OK.
print("test r2: ",r2_score(testy,myModel(testx))) #test r2:  0.8086921460343581, good, similar. our model is OK for prediction.

#predicted test
print(myModel(5)) #predicted: 22.8, real: 24. 

myLine=np.linspace(0,6,100) #smoothing x for myModel curve
plt.scatter(trainx,trainy)
plt.plot(myLine,myModel(myLine))
plt.show()
"""

"""#decision tree

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df=pd.read_csv("data_classification.csv")
#print(df['Nationality'].unique()) #returns unique values

#in making a decision tree, we need all columns to be numberic vals
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
    
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

#seperating features columns and target column
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

#dtree model
dtree = DecisionTreeClassifier()
dtree.fit(X, y)

#prediction test
#Example: Should I go see a show starring a 40 years old American comedian, with 10 years of experience, and a comedy ranking of 7?
predictOutcome=dtree.predict([[40, 10, 7, 1]])
#[1] means go, [0] means no go
print(predictOutcome)

tree.plot_tree(dtree, feature_names=features) #youll see that the tree is different each time, it's because dtrees are non deterministic by default.
plt.show()
"""

"""#confusion matrix (evaluating classification models)
from sklearn import metrics

actual = np.random.binomial(1,.9,size = 1000) 
predicted = np.random.binomial(1,.9,size = 1000)
#you already have actual in your dataset, loop through each feature of dataset into our model and get predicted array.

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)

cm_display.plot()
plt.show()

#The Confusion Matrix created has four different quadrants:
#True Negative (Top-Left Quadrant)
#False Positive (Top-Right Quadrant)
#False Negative (Bottom-Left Quadrant)
#True Positive (Bottom-Right Quadrant)
 
#Evaluation metrics 
Accuracy = metrics.accuracy_score(actual, predicted) #(True Positive + True Negative) / Total Predictions
Precision = metrics.precision_score(actual, predicted) #True Positive / (True Positive + False Positive)
Sensitivity_recall = metrics.recall_score(actual, predicted) #True Positive / (True Positive + False Negative)
Specificity = metrics.recall_score(actual, predicted, pos_label=0) #True Negative / (True Negative + False Positive)
F1_score = metrics.f1_score(actual, predicted) #2 * ((Precision * Sensitivity) / (Precision + Sensitivity))

print({"Accuracy":Accuracy,"Precision":Precision,"Sensitivity_recall":Sensitivity_recall,"Specificity":Specificity,"F1_score":F1_score})
"""

"""#hierarchial clustering
from sklearn.cluster import AgglomerativeClustering
#Agglomerative hierarchical clustering is a bottom-up method that starts with each data point as its own cluster and repeatedly merges the closest clusters to form a tree of nested groups.

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data=list(zip(x,y)) #returns a 2d array of format [(x,y)]
print(data)

hierarchial_cluster=AgglomerativeClustering(n_clusters=5, linkage='ward') #n_clusters define the no of clusters, ward linkage minimizes variance within clusters
labels=hierarchial_cluster.fit_predict(data)

plt.scatter(x,y,c=labels)
plt.show()"""

#logistic regression (multinomial classification) #used sigmoid function
from sklearn import linear_model

#X represents the size of a tumor in centimeters.
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
#note: X has to be reshaped into a column from a row for the LogisticRegression() function to work.

#y represents whether or not the tumor is cancerous (0 for "No", 1 for "Yes").
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

#RESHAPE BASICS. -1 means auto configuring the value. here it's auto finding no of rows and the no of columns is 1.
#in 3D reshape, it follows the format (no of 2d array boxes, 2d_row, 2d_column)

logistic_reg=linear_model.LogisticRegression()
logistic_reg.fit(X,y)

#prediction test
predicted=logistic_reg.predict(np.array([3.46]).reshape(-1,1)) #predict if tumor is cancerous where the size is 3.46mm:
#predicted=logistic_reg.predict([[3.46]]) works too
#in sklearn, the .predict() expects a 2D array mostly.

print(predicted) #We have predicted that a tumor with a size of 3.46mm will not be cancerous.

#coefficients
log_odds = logistic_reg.coef_ #this is the weight (w). in logistic regression, log_odds= log( p / (1-p) ) = wX + b
#it represents how strongly X influences y probability.

odds = np.exp(log_odds) #np.exp(log_odds)= e^(log_odds), so odds= p / (1-p)
print(odds) # [4.03541657], it means if the size of a tumor increases by 1mm the odds of it being a cancerous tumor increases by 4x.

#probability, inside maths of logr.predict()
def logit2prob(logistic_reg, X):
  log_odds = logistic_reg.coef_ * X + logistic_reg.intercept_ #log_odds= log(p / (1-p))
  odds = np.exp(log_odds) #removing log, odds= p / (1-p)
  probability = odds / (1 + odds)
  return(probability)

print(logit2prob(logistic_reg, X)) #prints the probabilities of each X being cancerous (y)
#our .predict returns 0 or 1, but this what's happening underneath, if >0.5, it's 1, if less, it's 0.


