# Learnings
'''
    1. Class variable gets applied to all its objects but is not part of instance because python stores only 1 instance of class variable so it recides in class dict and not object's dict list.
    2. Class variable can't be overriden from object access, if you try to do so, python creates new instance variable with same name and only assigns to that particular object instance and class variable remains same for all other objects.
'''

class Processors:
    category = "Dimensity"

    
    def __init__(self, name, architecture):
        self.name = name
        self.architecture = architecture

    def get_info(self):
        print("Name: {0}\nArchitecture: {1}\nCategory: {2}".format(self.name,self.architecture,self.category))

## Crete 2 objects and print their info
Helio95 = Processors("Helio95","8nm")
Dimensity1200 = Processors("Dimensity1200","6nm")

Helio95.get_info()
print(60*"-")
Dimensity1200.get_info()
print(60*"-")
print("Helio95 orig. dict", Helio95.__dict__)
print("Dimensity1200 orig. dict", Dimensity1200.__dict__)
print(60*"-")
Helio95.categoty = "Helio"		# tried to change class variable from object
Helio95.get_info()
print(60*"-")
print("Helio95 new. dict", Helio95.__dict__)
print(Helio95.category)
print(60*"-")
print("Dimensity1200 new. dict", Dimensity1200.__dict__)
print(60*"-")

