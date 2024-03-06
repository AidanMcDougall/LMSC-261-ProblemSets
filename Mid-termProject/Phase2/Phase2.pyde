def setup():
    size(800, 800,) #set size of canvas
    noStroke()

def draw():
    background(0)
    #moon
    fill(80)
    ellipse(400, 400, 600, 600)
    #Tint
    fill(255, 255, 0, 2)
    ellipse(400, 400, 600, 600)
    
    #crater1-4
    fill(40)
    ellipse(600, 500, 75, 75)
    ellipse(290, 280, 150, 150)
    ellipse(340, 510, 105, 105)
    ellipse(558, 220, 50, 50)

    #crater5-7
    fill(75)
    ellipse(499, 315, 110, 110)
    ellipse(490, 550, 135, 135)
    ellipse(180, 400, 60, 60)
    
    #Crater8+9
    fill(100)
    ellipse(400, 400, 40, 40)
    ellipse(215, 480, 73, 73)
    
    #TESTPHASE1 - COMMENT OUT FOR NORMAL DRAWING
    fill(0)
    ellipse(170, 180, 800, 800)
