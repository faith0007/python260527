# Demolist.py

list = [6,7,8,9,10]
print(len(list))
list.append(6)
print(list)
list.pop(3)
print(list)




str_a = 'python'
str_b = """다중
라인으로
저장"""

print(str_a[2:3])
print(str_b[2:4])



#set

a={1,2,3,3}
b={3,4,4,5}
print(a)
print(len(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#tuple

tp=(10,20,30)
print(tp.index(30))
print(tp[0])


def calc(ax,bx):
    return ax+bx,ax*bx


def calc2(xx):
    return xx[0]+xx[1]

print(calc(3,4))
print(calc2(tp))


