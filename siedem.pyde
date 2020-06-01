from abc import ABCMeta, abstractmethod 
class Pet():
    __metaclass__=ABCMeta 
    @abstractmethod 
    def speak(self): 
        super().__init__()
        return 'no sound'
    
class Cat(Pet): 
    def __init__(self, name):
        self.name = name
    def speak(self): 
        text('purr', random(50, width-70), random(50, height-50))
        return 'purr'
    
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('szczek', random(50, width-70), random(50, height-50))
        return 'szczek'
    
    def __add__(self, other): 
        return self.name[0]+ ' i ' + other.name[0]
    
        
        
        
def setup():
    size(600, 600)
    textSize(20)
    

    burek = Dog('Burek') 
    kitku = Cat('Kitku')
    global list_of_pets
    list_of_pets = [burek, kitku] 

    


    
def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak() 
        
