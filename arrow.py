class Arrow:
    

    def __init__(self, x_position, y_position, image, speed):
        self.x_position = x_position
        self.y_position = y_position
        self.image = image
        self.speed = speed 

        


up_arrow = Arrow(0, 0, 'arrowUp.png', 4)
down_arrow = Arrow(400, 0, 'arrowDown.png', 4)
left_arrow = Arrow(800, 0, 'arrowLeft.png', 4)
right_arrow = Arrow(1200, 0, 'arrowRight.png', 4)
arrows = [up_arrow,down_arrow,left_arrow,right_arrow]













        

    