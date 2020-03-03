import pygame

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

clock = pygame.time.Clock()

make_jump = False
jump_counter = 30


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

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            make_jump = True

        if make_jump:
            jump()

        dispay.fill((255, 255, 255))

        pygame.draw.rect(dispay, (247, 240, 22), (user_x, user_y, user_width, user_height))
        pygame.display.update()
        clock.tick(60)


run_game()
