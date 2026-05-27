# class2.py

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"Person[id={self.id}, name={self.name}]")


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"Manager[id={self.id}, name={self.name}, title={self.title}]")


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"Employee[id={self.id}, name={self.name}, skill={self.skill}]")


if __name__ == "__main__":
    people = [
        Manager(1, "Lee", "HR Manager"),
        Manager(2, "Choi", "Sales Manager"),
        Manager(3, "Park", "IT Manager"),
        Manager(4, "Kim", "Finance Manager"),
        Employee(5, "Jung", "Python"),
        Employee(6, "Yoo", "Java"),
        Employee(7, "Han", "JavaScript"),
        Employee(8, "Seo", "Data Analysis"),
        Employee(9, "Kang", "DevOps"),
        Employee(10, "Moon", "UI/UX Design"),
    ]

    for person in people:
        person.printInfo()