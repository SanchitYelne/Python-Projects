from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("US State Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_states = open("Guess_State.csv", "a")

guess = 0
guess_state = []

while guess != 50:
    user_answer = screen.textinput(title=f"Guss the State {guess}/50", prompt="What's the another state's name?").title()

    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in all_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if user_answer in all_states:
        guess += 1
        t = Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data["state"] == user_answer]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        t.goto(x=x_cor, y=y_cor)
        t.write(user_answer)
        guess_state.append(user_answer)

if guess == 50:
    t = Turtle()
    t.goto(0, 0)
    t.write("You Guess All States in US")



