class Person:
    a = 12 # class attribute

    def __init__(self, name):
        self.name = name # instance attribute

    def hello(self):
        print(f"How are you? My name is {self.name}")


obj = Person("Prakritish")
obj.hello()