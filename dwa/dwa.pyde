
def setup():
    size(400,400)
    frameRate(60)  
    global slownik_kolorow            
                                      
    slownik_kolorow = {"czerwony":(255,0,0, 80), "niebieski":(0,0,255,80)} 
      
    global x
    x = 200 
    
    global y 
    y = 0
    
    global xruch
    xruch = 5
    
    global yruch
    yruch = 5

    
def draw():

    global x 
    x=x + xruch

    global y 
    y=y + yruch
    
    if x > width or x < 0:
        global xruch
        xruch*=-1
        fill(*slownik_kolorow["czerwony"])
        
    if y > width or y < 0:
        global yruch
        yruch*=-1
        fill(*slownik_kolorow["niebieski"])
        
        
    ellipse(x,y,66,66)



    
    
    
    
    
    
    
    if mousePressed:
        exit() 
