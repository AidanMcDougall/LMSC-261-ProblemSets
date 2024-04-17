
def setup():
    size(600, 600,) #set size of canvas
    noStroke()

def draw():
    background(0)
    translate(100, 100)
    fill(255)
    columnWidth = width/0.9
    rowHeight = height/0.9
    for x in range(0, 3):
       drawObject(columnWidth * x, 0, 0.3, 0)
       for y in range(0, 3):
           drawObject(columnWidth * x, rowHeight * y, 0.3, 0)


def drawObject(x, y, s, r):
    pushMatrix()
    scale(s)
    rotate(r)
    translate(x, y)
    fill(80)
    #MainEllipse
    ellipse(0, 0, 600, 600)
    #Tint
    fill(255, 255, 0, 2)
    ellipse(0, 0, 600, 600)
    #crater1-4
    fill(40)
    ellipse(130, -180, 75, 75)
    ellipse(-150, -140, 150, 150)
    ellipse(-100, 140, 105, 105)
    ellipse(160, 180, 50, 50)
    #crater5-7
    fill(75)
    ellipse(85, -65, 110, 110)
    ellipse(75, 130, 135, 135)
    ellipse(-230, 10, 60, 60)
    #Crater8+9
    fill(100)
    ellipse(-50, 0, 40, 40)
    ellipse(-200, 100, 73, 73)
    #dayornight
    fill(0, 0, 0, frameCount+(x/-20)+(y/-20))
    ellipse(0, 0, 600, 600)
    popMatrix()
    
    #
