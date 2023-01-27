import turtle
import pandas

screen = turtle.Screen()
screen.title("United States quiz game")
# Setting background from the file, located in the same directory
cursor = "./blank_states_img.gif"
screen.addshape(cursor)
turtle.shape(cursor)

# Reading data from csv file (State names and coordinated on the map
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()  # Converting data to the list with pandas lib
guess_states = []

# .title() function converts first letter of the entered answer to Capital leter in order to match with the list
while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 Name the State",
                                    prompt="Name the State").title()
    # Creating "hidden" command to stop the game and creating list of the states, that user "forgot"
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in quessed_states]
        # missing_states = []
        # for state in all_states:
        #     missing_states.append(state)
        # converting list to the dataframe and saving to csv file
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

