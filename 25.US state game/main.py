import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 Correct answers",
                                    prompt="What's another state names?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_cor = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_cor.x), int(state_cor.y))
        t.write(answer_state)

# def get_mouse_click_cor(x, y):
#     """to get every state coordination on image"""
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_cor)
