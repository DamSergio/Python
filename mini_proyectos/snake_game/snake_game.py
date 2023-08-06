from random import randrange
import pygame as pg

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and snake_dir != (0, TILE_SIZE):
                snake_dir = (0, -TILE_SIZE)
            
            if event.key == pg.K_s and snake_dir != (0, -TILE_SIZE):
                snake_dir = (0, TILE_SIZE)
            
            if event.key == pg.K_a and snake_dir != (TILE_SIZE, 0):
                snake_dir = (-TILE_SIZE, 0)
            
            if event.key == pg.K_d and snake_dir != (-TILE_SIZE, 0):
                snake_dir = (TILE_SIZE, 0)

    screen.fill("black")

    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1

    if snake.left <= -TILE_SIZE:
        snake.center = (WINDOW + TILE_SIZE // 2, snake.centery)
    
    elif snake.right > WINDOW + TILE_SIZE:
        snake.center = (-(TILE_SIZE // 2), snake.centery)
    
    if snake.top < -TILE_SIZE:
        snake.center = (snake.centerx, WINDOW + TILE_SIZE // 2,)
    
    elif snake.bottom > WINDOW + TILE_SIZE:
        snake.center = (snake.centerx, -(TILE_SIZE // 2))
    
    if self_eating:
        snake.center = get_random_position()
        food.center = get_random_position()
        length = 1
        snake_dir = (0, 0)
        segments = [snake.copy()]

    if food.center == snake.center:
        food.center = get_random_position()
        length += 1

    pg.draw.rect(screen, "red", food)
    [pg.draw.rect(screen, "green", segment) for segment in segments] #Dibujar la serpiente

    time_now = pg.time.get_ticks()

    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    pg.display.flip()
    clock.tick(60)