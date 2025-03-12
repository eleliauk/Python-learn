import pgzrun
from pgzero.rect import Rect

# 设置窗口大小
WIDTH = 400
HEIGHT = 300

# 小球的参数
ball = Rect((30, 30), (20, 20))
speed_x = 3
speed_y = 3

def draw():
    screen.clear()
    screen.draw.filled_circle((ball.x, ball.y), 10, "red")

def update():
    global speed_x, speed_y
    ball.x += speed_x
    ball.y += speed_y

    if ball.left <= 0 or ball.right >= WIDTH:
        speed_x = -speed_x
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        speed_y = -speed_y

pgzrun.go()  # 这个必须在最后