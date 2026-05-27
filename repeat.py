
value=5

print("while loop")
while value > 0:
    print(value)
    value =value-1



print("for in loop")
for i in [1,2,3]:
    print(i)



#dictionary

d={"name":"Brandan","ages":{"a":10,"b":20},"addr":"SF,CA"}
for i in d.items():
    print(i)


print("---------range()-----------")
qqq=list(range(2000,2027))
print(qqq)
print(list(range(1,11,2)))


print("------list comprehension-------")
lst=list(range(1,11))
print([i**2 for i in lst if i>8])
tp =("apple","kiwi")
print(tuple([len(i) for i in tp]))
d={100:"apple",200:"grape"}
print([v.upper() for v in d.values()])



print("------filter function-------")

lst = [10,25,30]
itemL =filter(None,lst)
for item in itemL:
    print(item)



print("------to use filter function-------")
def getBiggerThan20(i):
    return i>20

lst = [10,25,30]
itemL =filter(getBiggerThan20,lst)
for item in itemL:
    print(item)


print("------to use filter lambda function-------")

lst = (10,25,30)
itemL =filter(lambda x:x>20,lst)
for item in itemL:
    print(item)
