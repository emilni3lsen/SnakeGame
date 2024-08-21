from turtle import Screen
from snake import Snake, MOVE_DISTANCE
from food import Food
from scoreboard import Scoreboard
import time


SPEED = 0.1  #The lower, the faster


def snake_game():
    
    screen = Screen()
    screen.clear()
    screen.setup(width=605, height=615)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up)
    screen.onkeypress(key="Left", fun=snake.left) 
    screen.onkeypress(key="Down", fun=snake.down)
    screen.onkeypress(key="Right", fun=snake.right)

    game_on = True
    while game_on:
        screen.update()
        time.sleep(SPEED)
        snake.move()
        
        # Detects when snake eats food
        if snake.front.distance(food) < MOVE_DISTANCE * 0.75:
            scoreboard.add_score()
            food.refresh()
            snake.extend()
            
        # Detects when snake hits wall
        if snake.front.xcor() > 290 or snake.front.xcor() < -290 or snake.front.ycor() > 290 or snake.front.ycor() < -290:
            game_on = False
            
        # Detects when snake hits its tail
        for segment in snake.snake[1:]:
            if snake.front.distance(segment) < MOVE_DISTANCE / 2:
                game_on = False

    scoreboard.game_over()
    screen.onkeypress(key="r", fun=snake_game)

    screen.exitonclick()
    
snake_game()