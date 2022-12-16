import turtle
import pandas

screen = turtle.Screen()
screen.title("United States quiz game")
cursor = "./blank_states_img.gif"
screen.addshape(cursor)
turtle.shape(cursor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 Name the State",
                                    prompt="Name the State").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

