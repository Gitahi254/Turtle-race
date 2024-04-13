import turtle #Provides a graphical user interface and it is an inbuilt module
import time
import random

WIDTH, HEIGHT = 500, 500 #Constant values are usualy in all caps
COLORS = ['red', 'green', 'orange', 'yellow', 'brown', 'cyan', 'pink', 'purple', 'blue', 'black']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit(): #To confirm wheather the user has input a number
            racers = int(racers)
        else:
            print('Input is not a number!!  Please try again')
            continue #returns to the while loop

        if 2 <= racers <= 10:
            return racers
        else:
        #This block makes sure the number input by the users is between 2 and 10
            print('Number not in range, please try again: ')

def race(colors):
    turtles = create_turtles(COLORS)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)  #setting an equal space on the starting point
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90) #Sets the turtle starting point
        racer.penup()
        racer.setpos(- WIDTH//2 + (i + 1) * spacingx, - HEIGHT//2 + 20) #Starting position of the turtles
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen() #Initilize the turtle screen module
    screen.setup(WIDTH, HEIGHT) #Set up the turtle screen
    screen.title('Turtle Racing!') #Change the screen name


#Now lets call the functions
racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
COLORS = COLORS[:racers]

winner = race(COLORS)
print ("The winner is the turtle color: ", winner)
time.sleep(5)