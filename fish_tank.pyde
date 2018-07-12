def setup():
    size(500,500)
    background (0)
    x = 0
    while x < 500 :
        y = 0
        while y < 500:
            if x % 200 == 0:
                fish (400, 205)
            else: 
                fish (300, 100)
                fish (100, 300)
            if y % 200 == 0:
                 fish (150, 400)
            y = y + 100
            x = x + 100
    
def fish(xCoordinate, yCoordinate):
    fill(random (255), random (255), random(255))
    ellipse(xCoordinate,yCoordinate, 101, 50) #fish body
    triangle(xCoordinate + 50 ,yCoordinate, xCoordinate + 100, yCoordinate - 50, xCoordinate + 100, yCoordinate + 50) #fish tail
