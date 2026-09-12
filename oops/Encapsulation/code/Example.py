class Super:
    publicData = "Public Data Member"
    _protectedData = "Protected Data Member"
    __privateData = "Private Data member"
    
    def accessPrivateMembers(self):
        print("Accessing inside class:", self.__privateData)
        
class Sub(Super):
    def accessProtectedMembers(self):
       print("Accessing inside subclass:",self._protectedData())
       
obj = Sub()

print(obj.publicData)
print(obj._protectedData)

obj.accessPrivateMembers()
# print(obj._Super__privateData)