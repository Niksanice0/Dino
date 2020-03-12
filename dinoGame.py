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

cactus_img = [pygame.image.load('img/Cactus0.png'), pygame.image.load('img/Cactus1.png'),
              pygame.image.load('img/Cactus2.png')]
cactus_options = [69, 449, 37, 410, 40, 420]

stone_img = [pygame.image.load('img/Stone0.png'), pygame.image.load('img/Stone1.png')]
cloud_img = [pygame.image.load('img/Cloud0.png'), pygame.image.load('img/Cloud1.png')]


class Object:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            dispay.blit(self.image, (self.x, self.y))
            # pygame.draw.rect(dispay, (224, 121, 31), (self.x, self.y, self.width, self.height))
            self.x -= 4
            return True
        else:
            return False
            # self.x = display_width + 50 + random.randrange(-80,60)

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        dispay.blit(self.image, (self.x, self.y))


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
    land = pygame.image.load('img/land.jpg')

    stone, cloud = open_random_onjects()

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

        dispay.blit(land, (0, 0))
        draw_array(cactuses)
        move_objects(stone,cloud)

        pygame.draw.rect(dispay, (247, 240, 22), (user_x, user_y, user_width, user_height))

        pygame.display.update()
        clock.tick(80)


def create_cactuses(array):
    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 20, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 20, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 20, height, width, img, 4))

    # array.append(Cactus(display_width + 300, display_height - 150, 30, 50, 4))
    # array.append(Cactus(display_width + 600, display_height - 180, 25, 80, 4))


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

            choice = random.randrange(0, 3)
            img = cactus_img[choice]
            width = cactus_options[choice * 2]
            height = cactus_options[choice * 2 + 1]
            cactus.return_self(radius, height, width, img)


def open_random_onjects():
    choice = random.randrange(0, 2)
    img_of_stone = stone_img[choice]

    choice = random.randrange(0, 2)
    img_of_cloud = cloud_img[choice]

    stone = Object(display_width, display_height - 80, 10, img_of_stone, 4)
    cloud = Object(display_width, 80, 70, img_of_cloud, 1)

    return stone, cloud

def move_objects(stone,cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0,2)
        img_of_stone = stone_img[choice]
        stone.return_self(display_width,500+random.randrange(10,80),stone.width,img_of_stone)

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_width, random.randrange(10, 200), stone.width, img_of_cloud)

run_game()
