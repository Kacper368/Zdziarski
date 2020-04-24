add_library('pdf')



def setup():
    global img
    global img1
    global img2
    size(492, 633)
    img = loadImage("zdjecie.png")
    img1 = loadImage("wasy.png")
    img2 = loadImage("bagieta.png")
        
def draw():
    global img
    global img1
    global img2
    
    if keyPressed:
        if key=='1':
            beginRecord(PDF, "out.pdf")
            image(img, 0,0,width, height)
            image(img1, 250,-140, width, height)

            endRecord()
        elif key=='2':
            beginRecord(PDF, "out.pdf")
            image(img, 0,0,width, height)
            image(img2, 250, 380,width, height)
            image(img1, 250, -140,width, height)

            endRecord()

                
def mousePressed():
    exit()
