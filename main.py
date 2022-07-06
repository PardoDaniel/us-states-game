import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_is_on = True
misses = 0
hits = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
xmiss = 150
ymiss = -280

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(xmiss, ymiss)
t.write("Misses: ")

while game_is_on:
    answer_state = screen.textinput(title=f"{hits}/50 Guess the State", prompt="Whats another states name?").title()
    if answer_state in all_states:
        hits += 1
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    else:
        misses += 1
        xmiss = xmiss + 50
        t.goto(xmiss, ymiss)
        t.write("X")
    if misses >= 3:
        game_is_on = False
    if hits == 50:
        t.goto(0, 0)
        t.write("CONGRATULATIONS YOU WIN")
        game_is_on = False




screen.exitonclick()