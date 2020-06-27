

class Doggo():
    
    def obrazek(self, img):
        self.img = img
        image(loadImage(self.img), 60, 60, 240, 240)
        

              
    def ramka(self, v1, v2, v3): # jaki sens ma metoda, która robi jedną rzecz, przyjmuje i przekazuje do niej argumenty bez zmiany?
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        rect(self.v1, self.v2, self.v3, self.v3)
    
        
    def kwadrat(self, a1, a2, a3): # do tego ta metodarobi dokładnie to samo co poprzednia... po co dublowanie?
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        rect(self.a1, self.a2, self.a3, self.a3)
        
    def ramka_fill(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        fill(c1, c2, c3)
        
def setup():
    background(255, 255, 255)
    textSize(20)
    size(500, 400)
    global doggo, x
    x = "doggo.png"
    doggo = Doggo()
   
        
    try: 
        doggo.obrazek(x) # tylko to jest newralgicznym fragmentem
    
    except:
        
        doggo.ramka_fill(255, 0, 4)
        text("nazwa obrazka jest nieprawidlowa \n lub obrazka nie ma w folderze", width - 430, height -40)
        doggo.ramka(45, 45, 270)
        doggo.ramka_fill(255, 255, 255)
        doggo.kwadrat(65, 65, 230)
        
    else:
        
        doggo.obrazek(x)
        doggo.ramka_fill(15, 41, 255)
        text("obrazek wyswietlil sie prawidlowo", width - 450, height -10)
        
    finally:
        noFill()
        doggo.ramka(45, 45, 270)
        
# za podobne absurdy do kodu u kolegi Dmytra, by uznać za przypadkowe...
# 1,5pkt
