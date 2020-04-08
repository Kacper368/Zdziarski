
def setup():
    size(400,400)
    frameRate(60)  
    global slownik_kolorow, x, y, xruch, yruch # możliwy jest też taki zapis     
                                      
    slownik_kolorow = {"czerwony":(255,0,0, 80), "niebieski":(0,0,255,80)} 
    x = 200 
    y = 0
    xruch = 5
    yruch = 5

    
def draw():

    global x, y, xruch, yruch
    x += xruch
    y += yruch
    
    if x > width or x < 0:
        xruch*=-1
        fill(*slownik_kolorow["czerwony"])
        
    if y > width or y < 0:
        yruch*=-1
        fill(*slownik_kolorow["niebieski"])
            
    ellipse(x,y,66,66)

    if mousePressed:
        exit()
        
# 2 pkt
        
