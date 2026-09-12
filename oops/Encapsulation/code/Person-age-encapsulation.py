class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if 0 <= new_age <= 120:
            self.__age = new_age
        else:
            print("Invalid age value. Age must be between 0 and 120")
    
    def display_info(self):
        print(f"{self.name} is {self.__age} years old.")
    

#  Instance creation
person = Person("Piku", 23)
person.name = "Sohini"
# person.__age = 34   # This line not affect Encapsulated age 

current_age = person.get_age()
print(f"Current age: {current_age}")


person.set_age(22)
person.display_info()