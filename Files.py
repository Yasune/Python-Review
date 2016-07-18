#Opening and writing files with python

#Files are objects form the class _io.TEXTIOWRAPPER

#Opening and reading a file
myfile=open('faketext.txt','r')
#opening options :
#'r' ouverture en lecture
#'w' ouverture en ecriture
#'a' ouverture en mode append
#'b' ouverture en mode binaire

print type(myfile)
content=myfile.read()
print(content)
myfile.close() #close a file

# myfile=open('faketext.txt','a')
# myfile.write('SkillCorner is a badass company ')
# myfile.close()

#the right way to open a file

with open('faketext.txt','r') as dumbtext:
    dumbcontent=dumbtext.read()
    print dumbcontent

print myfile.closed #verify if file named myfile is closed

