
import random

print(random.random())
print(random.random())

print(random.uniform(2.0,5.0))
print(random.uniform(2.0,5.0))


items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(random.choice(items))
print(random.choice(items))

print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])



print(sorted(random.sample(range(1,46),5))) #powe



import os.path
#filename = "c:\\python313\\python.exe"
filename = r"c:\python313\python.exe" 
print(os.path.abspath(filename))

if os.path.exists(filename):
    print(f"file size: {os.path.getsize(filename)} bytes")
else:
    print("file does not exist")

import os

print(os.process_cpu_count())

import glob


for item in glob.glob(r"c:/work/*.py"):
    print(item)




