class Drzwi():
    ile_bylo_klikane_Drzwi = 0 
    def __init__(self, arg_x, arg_y):
        self.x = arg_x 
        self.y = arg_y
    def rysuj(self):
        rect( self.x, self.y,100,300,70)
        
    

        
class Klamka():
    ile_bylo_klikane_Klamka = 0
    def __init__(self, arg_x, arg_y):
        self.wcisniety = False
        self.x = arg_x 
        self.y = arg_y
    def rysuj(self):
        circle( self.x, self.y,30)
    def wcisnij (self):
        Klamka.ile_bylo_klikane_Klamka +=1
        self.wcisniety = not self.wcisniety 
        if self.wcisniety:
            fill(10)
        else:
            fill(100)

        
def setup():
    size(250,250)
    global Drzwi_kordy
    Drzwi_kordy = Drzwi(100,100)
    global Klamka_kordy
    Klamka_kordy = Klamka(200,200)
def mouseClicked():
    Klamka_kordy.wcisnij()
    
    
def draw():
    background(200)
    Drzwi_kordy.rysuj()
    Klamka_kordy.rysuj()
    print(Klamka.ile_bylo_klikane_Klamka)

#1,75p trochę mało twóczo :(
