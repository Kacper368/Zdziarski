global kolorX, kolorK, kolorZ
kolorX = color(255, 255, 255)
kolorK = color(255, 0, 0)
kolorZ = color(240, 255, 0)

def setup():
    size(400,400)
    textSize(70)
def draw():
    clear()
    text("K", width/2-50, height/2)
    text("Z", width/2+20, height/2)
    if mouseX>=width/2-50 and mouseX<=width/2+50:
        clear()
        text("K", width/2-50, height/2)
        fill(kolorX) 
        text("Z", (width/2-50)+70, height/2)
        fill(kolorK)

    
    if keyPressed:
        if key=="z" or key=="Z":
            clear()
            text("K", width/2-50, height/2)
            fill(kolorZ)
            text("Z", (width/2-50)+70, height/2)
            fill(kolorX)
            
    if keyPressed:
        if key=="k" or key=="K":
            clear()
            text("Z", width/2+20, height/2)
            fill(kolorK)
            text("K", (width/2+20)-70, height/2)
            fill(kolorX)
    
    if key == CODED:
        if keyCode == LEFT:
            clear()
            text("K", width/2-50, height/2)
            fill(kolorX)
            text("Z", (width/2-50)+70, height/2)
            fill(kolorZ)
        if keyCode == RIGHT:
            clear()
            text("K", width/2-50, height/2)
            fill(kolorK)
            text("Z", (width/2-50)+70, height/2)
            fill(kolorX)
            


        
        
    s = createShape()
    s.beginShape() 
    s.fill(250,0,50,237) # nadajemy mu kolory
    s.stroke(250,250,50,255)
    s.vertex(4, height/3*2) # dodajemy punkty, które się połączą tworząc kształt
    s.vertex(4, height/3*2-20)
    s.vertex(width/2+10, height/3*2)
    s.vertex(width-4, height/3*2-20)
    s.vertex(width-4, height/3*2)
    s.endShape(CLOSE) # kończymy definiować kształt i zapisujemy go pod zmienną 's'; opcja Close zamknie kształt, można też go skończyć rysować zostawiając otwartym - nie podając nic w nawiasie
    shape(s, 0, -55) # miejsce w którym kształt ma się narysować w stosunku do naszego okna programu
