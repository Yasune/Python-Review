#Lists
print ('===============Lists====================')
l=[1,2,3]
print l #prints list
print l[0]  #prints first element of the list
print l[-1] # prints last element of the list
l[2]='Python' #Lists are polymorph in python
print l
l.append('isPolymorph') #appends an elements to a list
print l
x=l.pop() #pops l like a stack
print x
print l
print l,x

print('   ======Slicing/Sublisting==========')

nums=range(5) #creates list [0,1,2,..,n]
print nums
print nums[2:4] #Gets slice from 2 to 4(exclusive)
print nums[2:]  #Gets slice from 2 upwards
print nums[:2]  #Gets slice from first to seocnd element
print nums[:-1] #Slice indices can be negative
nums[2:4]=[8,9] #Replaces a slice by another
print nums

print('  ======= Looping======== ')
#Looping over the elements of a list

for number in nums:
    print number

print('=========Comprehensive lists===========')

#List comprehensions

#This method can be useful when creating a list from a previous one

#Example : Squarring a list

#Normal method

squarrel=[]
for x in nums:
    squarrel.append(x**2)
print squarrel

#Comprehensive list methods

squarrel2= [x**2 for x in nums]
print squarrel2

#Comprehensive list with conditions

countTen=range(10)
print len(countTen) #Lenght of list
evenSquares=[x**2 for x in countTen if x%2==0]
print evenSquares

print ('=============Dictionnaries/Hash Table==============')

employers={'Jhanzeeb':'Intern','Hugo':'Cofounder','Charles':'Cofounder','Yassine':'Intern'} #Creates dictionary
print employers['Jhanzeeb'] #Gets an entry from dictionary
print 'Yassine' in employers #Check if dictionary has given value
employers['Paul']='Technical Advisor'
print employers['Paul']

#Getting an element with a default
print employers.get('Yassine','Not existent')
print employers.get('Martin','Not existent')
print len(employers) #Length of dictionary

print('   ========Loops==========')
#Iterating over the keys of a hash table
for employer in employers:
    position=employers[employer] #getting the value of the key
    print '%s\'s postion at SkillCorner is: %s' %(employer,position)

#Getting keys and associatiated values
print ('    ================')
for employer,position in employers.iteritems():
    print '%s\'s position at SkillCorner is :%s' %(employer,position)

print (' ====Dictionnary Comprehension====')

#Easily Construct a Dictionnary

numberlist=range(4)
squares= {x:x**2 for x in numberlist}
print squares


print('==================== Sets=====================')
#Implements Set Data Structure


fruits ={'apple','banana','orange','strawberry'}
print type(fruits)
print 'apple' in fruits #returns booleance about existence of elt
print 'Potato' in fruits
fruits.add('kiwi') #adds elt to set
print fruits
print len(fruits)
fruits.remove('banana')
print fruits

print ('  =========== Loops===========')

for index,fruit in enumerate(fruits):
    print '#%d: %s' %(index+1,fruit)

print (' ========Set Comprehension====')

numberSet={x**2 for x in numberlist}
print numberSet

print('====================== Tuples==================')

t=(1,3)
print t
print type(t)