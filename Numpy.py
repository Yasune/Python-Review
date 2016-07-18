import numpy as np

print('======Arrays=========')
t=np.array([1,2,3]) #Creates a rank 1 array
print type(t) # We get numpy.ndarray"
print t.shape
print t[0],t[1],t[2]
t[0]=5 #change array element
print t

#Creake a two rank array

b=np.array([[1,2,3],[4,5,6]])
print b.shape
print b
print b[0,0],b[0,1],b[1,1]

#Function to create arrays

Z=np.zeros((2,2)) #Array full of zeros
print Z
print ('=======')
O=np.ones((3,3))
print O
print ('======')
#C=np.full((2,2),7) #Constant Matrix
#print C
print('=======')
I=np.eye(2) #Identity Matrix
print  I
print('=======')

E=np.random.random((3,3))
print E

print('===== Array indexing=====')
A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print A

B=A[:2,1:3] #B is an extracted matrix of A
print B

print A[0,1]
B[0,0]=77
print A[0,1] #B[0,0] is the same piece of data as A[0,1]


print('===========Accessing Column/Row ==========')
A= np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1=A[1,:]
row_r2=A[1:2,:]
print row_r1,row_r1.shape
print row_r2,row_r2.shape

col_r1 = A[:, 1]
col_r2 = A[:, 1:2]
print col_r1, col_r1.shape
print col_r2, col_r2.shape
print('===Integer indexing=======')

C=np.array([[1,2],[3,4],[5,6]])
print C
print('=======')
print C [[0,1,2],[0,1,0]]
#Equivalent to
print np.array([C[0,0],C[1,1],C[2,0]])

D=C [[0,1,2],[0,1,0]]
D=+17
print C #D elements are different than C ones as opposed to array indexing
print('=====Mutation trick=======')

A=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print A
R=np.array([0,2,0,1])#Row index
C=np.arange(4) #Column index
print A[C,R]

A[C,R]+=10
print A

print('===== Boolean Array Indexing=====')
A=np.array([[1,2],[3,4],[5,6]])
print A
bool_index=(A>2)
print bool_index
print A[bool_index]
#equivalent to
print A[A>2]

print('=========Datatypes==========')
x=np.array([1,2])
print x.dtype
y=np.array([1.,2.])
print y.dtype
z=np.array([1,2],dtype=np.int64) #force datatype
print z.dtype

print(' ======Math Operator=======')

x=np.array([[1,2],[3,4]],dtype=np.float64)
print 'X matrix is: ',x
y=np.array([[5,6],[7,8]],dtype=np.float64)

print(' ===Element wise operations=====')
print x+y
#print np.add(x,y)
print x-y
#print np.subtract(x,y)
print x*y
#print np.multiply(x,y)
print x/y
#print np.divide(x,y)
print np.sqrt(x)

print('====Algebric operations')
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11, 12])
#Dot product
print v.dot(w)
#print np.dot(v,w)

#Matrix/Vector product
print x.dot(v)
#print np.dot(x,v)

#Matrix product
print x.dot(y)
#print np.dot(x,y)

print("=====Useful operations====")
x = np.array([[1,2],[3,4]])
print x
print np.sum(x)
print np.sum(x,axis=0)
print np.sum(x,axis=1)

print x.T #Transposition
v = np.array([1,2,3])
print v    # Prints "[1 2 3]"
print v.T  # Prints "[1 2 3]" #Transposing a rank 1 array does nothing

print("=====Broadcasting=====")
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x) #Empty Matrix with same rank as x
print x
print v
print('===')

#Method 1 : Loop
for i in range(4):
    y[i,:]=x[i,:]+v
print y
print('===')
#Method 2 : Stacking

vv=np.tile(v,(4,1))
print vv
y=x+vv
print y
print('===')

#Method3: Broadcasting
y=x+v
print y
w=np.array([[1],[0],[1],[6]])
z=x+w
print z

print('== Application of broadcasting & Reshaping==')
v = np.array([1,2,3])
u= np.reshape(v, (3, 1))
w=np.array([4,5])
print u
print w
print u*w
print('== Adding vector to each row=')
x = np.array([[1,2,3], [4,5,6]])
print x
print v
print x+v

print('== Adding vector to each column=')
x = np.array([[1,2,3], [4,5,6]])
#Method 1
print (x.T+w).T
#Method 2
print x+np.reshape(w,(2,1))

#Multiplying by a constant
print x*2


