from pygame import *


# Создание сцены
RESOLUTION = (1280, 720)
window = display.set_mode(RESOLUTION)
window.fill((255, 255, 255))

# Игровой счётчик
FPS = 60
clock = time.Clock()
clock.tick(FPS)

game = True

while game:

    # Закрытие приложения
    for e in event.get():
        if e.type == QUIT:
            game = False
     
    if not finish:
        window.fill((255, 255, 255))

# Смена кадра
    display.update()
