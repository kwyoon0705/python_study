import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
background_img = "blank_states_img.gif"
screen.addshape(background_img)
turtle.shape(background_img)

states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()
x_cor_list = states_data.x.to_list()
y_cor_list = states_data.y.to_list()

guessed_state = []
missing_state = states
is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"Guess the States. {len(guessed_state)}/50", prompt="What's another state's name?").title()
    turtle_name = turtle.Turtle()
    if answer_state == "Exit":
        break
    if answer_state in states:
        turtle_name.penup()
        turtle_name.hideturtle()
        state_data = states_data[states_data.state == answer_state]
        turtle_name.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        turtle_name.write(answer_state)
        guessed_state.append(answer_state.title())
        missing_state.remove(answer_state)


missing_state_dict = {"missing states": missing_state}
pandas.DataFrame(missing_state_dict).to_csv("missing_states.csv")
