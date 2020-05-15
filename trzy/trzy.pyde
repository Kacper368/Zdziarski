def setup():
    size(400,400)
    textSize(70)
    global kolorX, kolorK, kolorZ # tylko jeśli będą zadeklarowane w setupie, można mieć pewność, że wykona się przed wywołaniem kodu z draw
    kolorX = color(255, 255, 255)
    kolorK = color(255, 0, 0)
    kolorZ = color(240, 255, 0)
def draw():
    clear() # jeżeli wykonujesz to na początku każdej klatki, to nie ma sensu powtarzać też na początku każdego warunku
    text("K", width/2-50, height/2)
    text("Z", width/2+20, height/2)
    
    if mouseX>=width/2-50 and mouseX<=width/2+50:
        text("K", width/2-50, height/2)
        fill(kolorX) # nie do końca rozumiem zamierzenie, ale najpierw powinno się ustawiać kolor a później pisać to co ma być w tym kolorze, więc nie do końca widzę sens kolejności tutaj
        text("Z", (width/2-50)+70, height/2)
        fill(kolorK)

    
    if keyPressed: # nie ma potrzeby powtarzać, działa jeżeli kolejny warunek jest odpowiednio wytabowany
        if key=="z" or key=="Z":
            text("K", width/2-50, height/2)
            fill(kolorZ)
            text("Z", (width/2-50)+70, height/2)
            fill(kolorX)
        if key=="k" or key=="K":
            text("Z", width/2+20, height/2)
            fill(kolorK)
            text("K", (width/2+20)-70, height/2)
            fill(kolorX)
    
    if key == CODED:
        if keyCode == LEFT:
            text("K", width/2-50, height/2)
            fill(kolorX)
            text("Z", (width/2-50)+70, height/2)
            fill(kolorZ)
        if keyCode == RIGHT:
            text("K", width/2-50, height/2)
            fill(kolorK)
            text("Z", (width/2-50)+70, height/2)
            fill(kolorX)
        # przez przerzucanie koloru z warunku w popzedniej klatce zaznaczenie dziwnie działa, zostają pewne artefakty z wcześniejszego wykonania kodu
        # o wiele prościej, czytelniej i logiczniej byłoby ustawiać kolor dla elementu w tej samej klatce, w której go rysujemy, nawet i bezpośrednio przed narysowaniem    
    s = createShape()
    s.beginShape() 
    s.fill(250,0,50,237) 
    s.stroke(250,250,50,255)
    s.vertex(4, height/3*2) 
    s.vertex(4, height/3*2-20)
    s.vertex(width/2+10, height/3*2)
    s.vertex(width-4, height/3*2-20)
    s.vertex(width-4, height/3*2)
    s.endShape(CLOSE) 
    shape(s, 0, -55)
    
# 1,25p
