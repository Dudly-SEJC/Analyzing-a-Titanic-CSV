#Import required libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#Load the data
titanic = pd.read_csv("titanicA.csv")  # titanic = panda=read the csv file named "titanicA.csv"

#change code to *read_excel* for excel file
print(titanic.head(5)) #print first four rows of data
print(titanic.tail(5)) #gives last 5 rows of data
print(titanic.sample(10)) #gives random 10 rows

#identify variable type
print(titanic.dtypes) #what datatypes we have in the col of our data
print(titanic.describe()) #gives count, mean, std dev, and other info

#Get count of values in a categorical variable
print(titanic.survived.value_counts())

#mean, median, mode, max, min
print(titanic['age'].median())

#scatter plot
x = titanic['age']
y = titanic['fare']
plt.xlabel('age')
plt.ylabel('fare')
plt.scatter(x,y)
plt.show()

#histogram
x = titanic['age']
plt.xlabel('age')
plt.ylabel('frequency')
plt.hist(x)  # for more bins: plt.hist(x, bins=15)
plt.show()

#plot wouldn’t make sense; works best for time series plot
#histogram
x=titanic['fare']
y=titanic['age']
plt.plot(x, y)
plt.show()

#bar diagram
x=titanic['sex']
y=titanic['age']
plt.bar(x, y) # plt.bar(x, y, color = "red", width=0.1) #plt.barh(x, y, color = "red", height = 0.1)
plt.show()
