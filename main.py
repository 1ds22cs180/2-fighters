import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()
FPS = 60

#defne colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
# define font
font = pygame.font.Font(None, 36)

Warr_Size = 162
Warr_Data = [Warr_Size]
Wiz_Size = 250
Wiz_Data = [Wiz_Size]

bg_image = pygame.image.load("assets/background/bg.png").convert_alpha()

warrior_sheet = pygame.image.load("assets/warriors/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/wizard/sprites/wizard.png").convert_alpha()

Warr_Anim_Steps = [10, 8, 1, 7, 7, 3, 7]
Wiz_Anim_Steps = [8, 8, 1, 8, 8, 3, 7]

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

def draw_health_bar(health,x,y):
    ratio = health/100
    pygame.draw.rect(screen, WHITE, (x-2,y-2,404,34))
    pygame.draw.rect(screen, RED, (x,y,400,30))
    pygame.draw.rect(screen, YELLOW, (x,y,400 * ratio,30))

f1 = Fighter(100, 310, Warr_Data,warrior_sheet, Warr_Anim_Steps)
f2 = Fighter(700, 310, Wiz_Data,wizard_sheet, Wiz_Anim_Steps)

run = True
while run:

    clock.tick(FPS)

    draw_bg()
    draw_health_bar(f1.health, 20, 20)
    draw_health_bar(f2.health, 580, 20)
    
    f1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen, f2)
    #f2.move()

    f1.draw(screen)
    f2.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()