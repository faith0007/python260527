
names="Tom"

class Person:
    def __init__(self,name=""):
        self.__name="default name"
        if len(name)>0 :
            self.__name=name
    def print(self):
        print ("my name {0}",self.__name)
    def change(self) :
        names="XXXXXXX"
        print(names)



p1=Person()
p1.name='Kate'
p2=Person(name="Nana")



p1.print()
p2.print()

print("-------",p1.name)

p1.__name='Anna'
p1.print()

p1.change()



#print(dir(p1))