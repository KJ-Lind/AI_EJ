import turtle

w = turtle.Screen()
w.setup(width=800, height=600)
w.bgcolor("black")
w.title("L-System")


t = turtle.Turtle()
t.speed(0)
t.color("cyan")
t.hideturtle()
t.penup()
t.goto(-300, 200)
t.pendown()


def lindenmayer_translation(rules, axiom):
    translation = []

    for symbol in axiom:
        if symbol in rules:
            translation.extend(rules[symbol])
        else:
            translation.append(symbol)

    return translation



rules = {
    'F': ['F','F'],
    'X': ['F','+','[','[','X',']','-','X',']','-','F','[','-','F','X',']','+','X']
}

axiom = ['-','X']
iterations = 5


for i in range(iterations):
    axiom = lindenmayer_translation(rules, axiom)


angle = 25
step = 10
pos = {0,0}
oldAngle = 0

lastPlace = []

for symbol in axiom:
    if symbol == 'F':
        t.forward(step)
    elif symbol == '+':
        t.left(angle)
    elif symbol == '-':
        t.right(angle)
    elif symbol == '[':
      lastPlace.append((t.pos(),t.heading()))
    elif symbol == ']':
      pos, oldAngle = lastPlace.pop()
      t.penup()
      t.goto(pos)
      t.setheading(oldAngle)
      t.pendown()

w.exitonclick()


