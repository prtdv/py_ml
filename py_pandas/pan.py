import pandas as pd
 
"""#series
#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.

s=(34,68,"gello",[12,[34]])

x=pd.Series(s) #putting an index argument here would change the default ints indexes to the given ones.

print(x) #can use indexes here to get the element

k={
    "d1":"monday",
    "d2":"tuesday",
    "d3":"wednesday"
}
#in key value pair, the key becomes the index
y=pd.Series(k, index=["d1","d3"]) #selective series
print(y)
"""

"""#dataframes
#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
#Series is like a column, a DataFrame is the whole table.

data={
    "data1":[1243,45,67,57],
    "data2":["hello",12.5,[5,4],35]
}

df=pd.DataFrame(data)
print(df)
print(df.loc[[1,2,3]]) #retruns series with key as index, can use [custom index] to get the val from the series."""

"""read_csv and read_json
file=pd.read_csv('data.csv')
pd.options.display.max_rows=2000
print(pd.options.display.max_rows)

dihta = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

xy=pd.DataFrame(dihta)

#if this was json, use pd.read_json(filepath to do the same)
print(xy)"""

"""#head tail stuff
file=pd.read_csv('data.csv')
#print(file.head(15))
print(file.tail(10))

print(file.info())"""

df=pd.read_csv('data.csv')

""" dropna, fillna and fixing format.
#df=df.dropna() #drop null rows.
x=df["Calories"].mean()
print(x)
df=df.fillna({"Calories":x}) #can put a bigger json, and the corresponding val will be inplaced of null. everything stays the same, null goes.
print(df.to_string())

print(df.to_string(), "\n")
df["Date"] = pd.to_datetime(df["Date"], format='mixed') #format='mixed' automatically fixes the data, use this mostly.
print(df.to_string())

print("\n")
df=df.dropna(subset=["Date","Calories"])
print("lol this is the final drop and fixing format data")
print(df.to_string())"""

"""#wrong data cleaning
df.loc[[8,22],'Duration']=18
print(df.to_string())

for x in df.index:
  if df.loc[x, 'Duration'] < 30 or df.loc[x, 'Duration'] > 60:
    print("anomaly in df duration is at",x,"is",df.loc[x,'Duration'])
    df.loc[[x],'Duration']=45
  elif df.loc[x,'Pulse']<100:
    print("anomaly in df pulse is at",x,"is",df.loc[x,'Pulse'])
    df.drop(x, inplace=True)

print(df.to_string())"""

print(df.to_string())
#print(df.duplicated())

df=df.drop_duplicates() 
#or df.drop_duplicates(inplace=True) 
#all and only drop methods have the inplace argument, use it as necessary (for loops, use inplace, otherwise df=df.drop_blablah()
print("\n",df.to_string())

