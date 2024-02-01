import turtle
import pandas

FONT = ("Arial", 12, "normal")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

marker = turtle.Turtle()



def place_on_map(state, x, y):
    marker.penup()
    marker.goto(x, y)
    marker.write(state, align="left", font=FONT)

guess_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

# Read data from csv file
data = pandas.read_csv("blank_states.csv")
state_list = data.state.to_list()
x_cord = data[data.state == "Ohio"]
print(x_cord)
# Find the total amount of states
count = len(data.state)
correct = 0

# Create game loop
game_on = True
# while game_on:
#     # If guess is correct
#     if guess_state in state_list:
#         correct += 1
#
#         place_on_map(guess_state)
#         state_list.pop(guess_state)
#
#     # If all states found.
#     if correct == count:
#         game_on = False

turtle.mainloop()
