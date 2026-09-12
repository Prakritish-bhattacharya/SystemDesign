from abc import ABC, abstractmethod

class Great(ABC):
    @abstractmethod
    def say_hello(self):
        # pass
        print("Hello from Abstract class...")
    
class English(Great):
    def say_hello(self):
        return "Hello !!"
    
obj = English()
print(obj.say_hello())

