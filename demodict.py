# demodict.py

#dict
colors={"watermelon":"green","strawberry":"red"}
print(len(colors))

colors["lemon"]="yellow"

colors["watermelon"]="red"

print(colors)

del colors["strawberry"]

for i in colors.items():
 print(i)

print(colors["lemon"])


