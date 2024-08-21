from turtle import Turtle


SIZE = 1                     # Size 1 = 20 pixels
MOVE_DISTANCE = 20 * SIZE
SNAKE_LENGTH = 3             # Length at start


class Snake:
    def __init__(self) -> None:
        self.snake = []
        self.make_snake()
        self.front = self.snake[0]
    
    def make_snake(self):
        for i in range(SNAKE_LENGTH):
            pos = (MOVE_DISTANCE * i * -1, 0)
            self.make_segment(pos)
        
    def make_segment(self, pos):
        segment = Turtle("square")
        segment.color("white")
        segment.up()
        segment.shapesize(SIZE, SIZE)
        segment.setpos(pos)
        self.snake.append(segment)
        
    def extend(self):
        self.make_segment(self.snake[-1].pos())
        
    
    def move(self):
        for num in range(len(self.snake) - 1, 0, -1):
            cur_seg = self.snake[num]
            next_seg = self.snake[num - 1]
            cur_seg.setpos(next_seg.pos())
            
        self.front.forward(MOVE_DISTANCE)
    
    def up(self):
        if not self.front.heading() == 270:
            self.front.setheading(90)
    
    def left(self):
        if not self.front.heading() == 0:
            self.front.setheading(180)
            
    def down(self):
        if not self.front.heading() == 90:
            self.front.setheading(270)
            
    def right(self):
        if not self.front.heading() == 180:
            self.front.setheading(0)