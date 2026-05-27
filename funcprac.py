def setValue(newValue):
    x=newValue
    print("inside:",x)

retValue=setValue(5)
print(retValue)


def swap(a,b):
    return b,a

retValue=swap(3,4)
print(retValue)

x=5
def func(a):
    return a+x

print(func(1))

def func2(a):
    x=1
    return a+x

print(func2(1))




def times(a=10,b=20):
    return a*b

print(times(3,4))
print(times(3))
print(times(b=4,a=2))

def connectURI(server,port):
    return "https://"+server+":"+port

print(connectURI("yahoo.com","10"))
print(connectURI(port="8080",server="google.com"))



# example for debug
def union(*ar):
    result = []
    for i in ar:
        for x in i:
            if x not in result:
                result.append(x)
    return result

print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))



#lambda
g=lambda x,y:x-y
h=lambda x,y:x+y
print(g(4,3))
print(h(3,4))
print((lambda x:x*x(3)))

print(dir())
print(globals())

