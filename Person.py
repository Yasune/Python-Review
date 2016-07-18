class Person(object):

    #Constructor
    def __init__(self,name,id):
        self.name=name
        self.id=id

    #Instance method

    def greeting(self):
        print 'Hello Human ! I am %s'%(self.name)

    def getname(self):
        return self.name

    def getid(self):
        return self.id


Jimmy=Person('Jimmy',1768)
Jimmy.greeting()