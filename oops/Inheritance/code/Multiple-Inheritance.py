class Camera:
    def take_photo(self):
        print("Taking a Photo")

class Phone:
    def make_call(self):
        print("Making a Call")

class SmartPhone(Camera, Phone): # Multiple Inheritance
    def browse_internet(self):
        print("Browsing the Internet")
    
Smart_phone_Obj = SmartPhone() # create an Instance of SmartPhone class
Smart_phone_Obj.take_photo() # Calling method of Camera class (Parent class)
Smart_phone_Obj.make_call() # Calling method of Phone class (Parent class)
Smart_phone_Obj.browse_internet() # Calling method of SmartPhone class (Child class)