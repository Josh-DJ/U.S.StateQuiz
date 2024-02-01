import turtle
import pandas

FONT = ("Arial", 8, "normal")

# Initializing the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # Adding the image as a shape for turtle to recognize.
turtle.shape(image)

# Turtle object used to write state names on screen
marker = turtle.Turtle()
marker.hideturtle()
marker.penup()


# Function that places the name of the correct state on map.
def place_on_map(state, x, y):
    marker.goto(x, y)
    marker.write(state, align="left", font=FONT)


# Read data from csv file
data = pandas.read_csv("blank_states.csv")
state_list = data.state.to_list()

# Find the total amount of states
count = len(data.state)
correct = 0

# Create game loop
game_on = True
guess_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
while game_on:
    # If guess is correct
    if guess_state in state_list:
        correct += 1
        row_info = data[data.state == guess_state]
        x_cord = row_info["x"][row_info.index[0]]
        y_cord = row_info["y"][row_info.index[0]]
        place_on_map(guess_state, x_cord, y_cord)
        state_list.remove(guess_state)

    # If all states found.
    if correct == count:
        game_on = False

    guess_state = screen.textinput(title=f"Correct states {correct}/{count}",
                                   prompt="What's another state's name?").title()

turtle.mainloop()
