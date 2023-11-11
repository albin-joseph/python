
import time
from turtle import Screen
from player import Player
from car_manger import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()
    
    # Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            
    # Detect car turtle reaches finished line
        if player.is_at_finish_line():
            scoreboard.increase_score()
            scoreboard.update_scoreboard()
            car_manager.level_up()
            player.go_starting_position()
            




screen.exitonclick()