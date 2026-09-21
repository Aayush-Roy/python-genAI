class Person:
    name = "Aayush"
    occupation = "Developer"
    age = 22

    def info(self):
        print(f"My name is {self.name}, and I'm a {self.occupation}")


a = Person()
a.name = "Aman"
b = Person()
b.name = "Manisha"
b.occupation = "Accountant"
a.info()
b.info()