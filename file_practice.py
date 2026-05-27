# file_practice.py

# file object creation

# file writing
f = open("test.txt", "wt",encoding="utf-8")  
f.write("Hello, World!\n")
f.close()


# file reading
f = open("test.txt", "rt",encoding="utf-8") 
content = f.read()
print(content)
f.close()



