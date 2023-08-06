# Tested on Mac Ventura
# Python 3.11
# programmer-666

import pyglet
import random


WIDTH, HEIGHT = 800, 600 # for frame
shapes: list = [] # holds circles

window: pyglet.window.cocoa.CocoaWindow = pyglet.window.Window(
    width=WIDTH,
    height=HEIGHT,
    caption="Circles",
    vsync=False,
    style=pyglet.window.Window.WINDOW_STYLE_DEFAULT)
# CocoaWindow type for mac

radius: float = 100.0
def draw_circle(x: int, y: int) -> None:
    global radius
    if radius > 0:
        circle = pyglet.shapes.Circle(x=x,
        y=y,
        radius=radius,
        color=(random.randint(0, 256),
        random.randint(0, 256),
        random.randint(0, 256)))

        shapes.append(circle)
        radius -= .6
    else:
        radius += (10 + random.random() * 10)

# changes windows width and height
click_flag: bool = True
@window.event
def on_mouse_press(x, y, button, modifiers) -> None:
    global click_flag
    if click_flag:
        window.set_size(WIDTH / 2, HEIGHT / 2)
        click_flag = False
    else:
        window.set_size(WIDTH, HEIGHT)
        click_flag = True

@window.event
def on_draw() -> None:
    window.clear()
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)

    draw_circle(x, y)
    for shape in shapes:
        shape.draw()

pyglet.app.run()
