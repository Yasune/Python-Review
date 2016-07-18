import numpy as np
import pandas as pd
#Dataframe manipulation with Panda
#Create DataFrame from a numpy array

ar = np.array([[1.1, 2, 3.3, 4], [2.7, 10, 5.4, 7], [5.3, 9, 1.5, 15]])
print ar

df = pd.DataFrame(ar, index = ['a1', 'a2', 'a3'], columns = ['A', 'B', 'C', 'D'])
print df

print('=======')
#Create DataFrame from dictionary

df = pd.DataFrame({'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9], 'C': [3.3, 5.4, 1.5], 'D': [4, 7, 15]},
                      index=['a1', 'a2', 'a3'])
print df

print('=======')
print df.head(2)
print('=======')
print df.tail(2)
print('=======')
print df.columns #outputs dataframe indexes as column indexes
print df.columns.values # outputs column indexes as numpy array
print df.index
print df.index.values #same as above
print df.values #returns corresponding numpy array
# print df.describe() #returns statistics about data

print df.shape # returns the shape of the dataframe
print len(df) #returns number of columns/indexes
print len (df.columns) #returns number of columns
print('======== Dataframe indexation===== ')
print df
print('= Access to Row =')
# print df['A']
#OR
# print ('====')
print df.A #returns a Serie
print('= Access to Column=')
print df.loc['a1'] #returns a Serie

print('==Access to subDataFrame with name of column and row===')
#With names of columns and rows
print df.loc[['a2', 'a3'], ['A', 'C']]

#Access to a value
#Non Recommended Method
print df.loc['a2', 'C']
#Recommended Method
print df.at['a2', 'C']
#Modify Value
df.at['a2','C']=19
print df

print('== Access to subDataFrame with number of column and row ==')
print df.iloc[1] #returns line number 1
#similar to above
df.iloc[1:3,[0,2]]
df.iloc[:,2:4]
df.iloc[1,2]
df.iat[1,2]
print df
print('== Access to subDataFrame with conditions')
print df[(df.A > 2) & (df.B < 11)]
print df[df.A.isin([5.3, 2.7])] #returns lines where the values of A are equal to 5.3 or 2.7