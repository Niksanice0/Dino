import pygame
import random

pygame.init()

display_width = 800
display_height = 600

dispay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Run Dino, run!!!")

# icon = pygame.image.load("icon.png")
# pygame.display.set_icon(icon)

user_width = 60
user_height = 100
user_x = display_width // 3
user_y = display_height - 100 - user_height

cactus_width = 20
cactus_height = 70
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 100

clock = pygame.time.Clock()

make_jump = False
jump_counter = 30


class Cactus:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            pygame.draw.rect(dispay, (224, 121, 31), (self.x, self.y, self.width, self.height))
            self.x -= 4
            return True
        else:
            return False
            # self.x = display_width + 50 + random.randrange(-80,60)

    def return_self(self, radius):
        self.x = radius


def jump():
    global user_y, jump_counter, make_jump
    if jump_counter >= -30:
        user_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def run_game():
    global make_jump
    game = True
    cactuses = []
    create_cactuses(cactuses)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            make_jump = True
        if keys[pygame.K_q]:
            pygame.quit()

        if make_jump:
            jump()

        dispay.fill((255, 255, 255))
        draw_array(cactuses)
        pygame.draw.rect(dispay, (247, 240, 22), (user_x, user_y, user_width, user_height))

        pygame.display.update()
        clock.tick(80)


def create_cactuses(array):
    array.append(Cactus(display_width + 20, display_height - 170, 20, 70, 4))
    array.append(Cactus(display_width + 300, display_height - 150, 30, 50, 4))
    array.append(Cactus(display_width + 600, display_height - 180, 25, 80, 4))


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(30, 45)
    else:
        radius += random.randrange(200, 350)
    return radius


def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            radius = find_radius(array)
            cactus.return_self(radius)


run_game()
