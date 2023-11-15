# We are going to  create a data analysis game
import os
import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = f"{os.getcwd()}/025-day/us_state_game/data/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(f"{os.getcwd()}/025-day/us_state_game/data/50_states.csv")
all_states = data.state.to_list()
score = 0

def check_answer(guess_name):
    if guess_name in all_states and not guess_name in guessed_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess_name]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess_name)
        
    else:
        print("missed")
    guessed_state.append(guess_name)


guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    check_answer(answer_state)
    


# def get_mouse_click_coord(x, y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coord)

# turtle.mainloop()

screen.exitonclick()