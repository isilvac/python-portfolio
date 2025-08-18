import pandas
import turtle


screen = turtle.Screen()
screen.title("US States Game")
image = "./data/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Writer of States
pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor("Black")
pen.penup()
user_score = 0

data = pandas.read_csv("./data/50_states.csv")
guessed_states = []


def get_new_state():
    return screen.textinput(f"{user_score}/50 states correct", "What's the name of a state?").title()


def get_score():
    global user_score
    state_data = data[data["state"] == answer]
    if state_data.size > 0:
        pen.goto(int(state_data["x"]), int(state_data["y"]))
        pen.write(answer, align="center", font=("Arial", 10, "normal"))
        user_score += 1
        guessed_states.append(answer)
    return user_score


def missing_states():
    missed = [state for state in data["state"] if state not in guessed_states]
    pandas.DataFrame(missed).to_csv("./data/states_to_learn.csv")


while len(guessed_states) < 50:
    answer = get_new_state()
    if answer == "Exit":
        missing_states()
        break
    points = get_score()
    print(points)
    screen.update()


screen.exitonclick()
