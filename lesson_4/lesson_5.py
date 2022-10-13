import graphics as gr

SIZE_X = 800
SIZE_Y = 800

G = 2000

def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_coords(coords, velocity):
    return add(coords, velocity)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)
    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)

def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                      point_1.y + point_2.y)
    return new_point


def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point


def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')
    circle.draw(window)
    return circle


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)

    sun = gr.Circle(gr.Point(400, 400), 50)
    sun.setFill('yellow')
    sun.draw(window)


def check_coords(coords, velocity):
    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y
    if coords.x < 0 or coords.x > SIZE_Y:
        velocity.x = -velocity.x



window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
clear_window()

coords = gr.Point(200, 200)
velocity = gr.Point(1, -2)
acceleration = gr.Point(0, 0.1)
ball = draw_ball(coords)

while True:

    acceleration = update_acceleration(coords, gr.Point(400, 400))
    n = update_coords(coords, velocity)

    ball.move(n.x - coords.x, n.y - coords.y)
    coords = n

    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)

    gr.time.sleep(0.02)
