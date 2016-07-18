
#Serie Manipulation with Panda
import numpy as np
import pandas as pd

print('====== Series======')
s=pd.Series(([1, 2, 5, 7]))
print s
print type(s)
s=pd.Series([1.3, 2, 5.3, 7])
print(s)
print type(s)
s = pd.Categorical(['a', 'b', 'a', 'b', 'b'], categories = ['a', 'b'])
print type(s)
print s

#Exemple score of players

score=pd.Series(['15','16','13','12'],index=['Antoine','Daniel','Mathieu','Sommet'])
print score

print score.values #outputs numpay array
print s.unique() # outputs unique values in Serie

#Boolean test

s1=pd.Series([1,2,3])
s2=pd.Series([1,4,3])
print (s1==s2) #returns boolean Serie stating equality
print (s1==s2).all() #test if all values are equal
print (s1==s2).any() #test if there is at least one equal value
print s2.argmax() #index corresponding to maximum
print s2.apply(lambda x:2*x+1) #returns the series after applying function