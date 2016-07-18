
#General Syntax on a simple example
def fizzbuzz(x):
    #Solves the fizzbuzz problem
    s=''
    if x%3==0:
        s='fizz'
    if x%5==0:
        s+='buzz'
    return s

print fizzbuzz(30)


#Optional Argument


def hello(name,loud =False):
    if loud:
        print 'HELLO %s ! WASSUP' % name.upper()
    else:
        print 'Hello %s !' %name



hello('Yassine')
hello ('Yassine',True)


#Iterative Function
def iterativefacto(n):
    res=1
    for i in range(2,n+1):
        res*=i
    return res


#Recursion Function

def recurentfacto(n):
    if n==0:
        return 1
    else:
        return n*recurentfacto(n-1)


print iterativefacto(5)
print recurentfacto(5)






