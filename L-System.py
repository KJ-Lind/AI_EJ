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
t.goto(-100, 0)
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
    'F': ['F', '+', 'F', '-', 'F']
}

axiom = ['F']
iterations = 5


for i in range(iterations):
    axiom = lindenmayer_translation(rules, axiom)


angle = 60
step = 4

for symbol in axiom:
    if symbol == 'F':
        t.forward(step)
    elif symbol == '+':
        t.left(angle)
    elif symbol == '-':
        t.right(angle)

w.exitonclick()


