import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
pygame.display.set_caption("Maze Game")

WIDTH, HEIGHT = screen.get_size()
WIDTH = min(WIDTH,HEIGHT)
HEIGHT = min(WIDTH,HEIGHT)
N = 20
STEP_SIZE = WIDTH/N

## Buttons
button_1 = pygame.Rect(1100,50,200,100)
button_2 = pygame.Rect(1100,200,200,100)

## Text
font = pygame.font.SysFont(None, 24)
font_2 = pygame.font.SysFont(None,36)
Generate = font.render("Generate New Maze",True,(0,0,0))
Solve = font.render("Solve",True,(0,0,0))
user_score = 0;
Score = font_2.render(f"Score: {user_score} ",True,(255,255,255));
clock = pygame.time.Clock()


grid = [[0 for x in range(N)] for x in range(N)]

## 

def 



for i in range(N):
    for j in range(N):
        grid[i][j]=pygame.Rect(i*STEP_SIZE,j*STEP_SIZE,STEP_SIZE,STEP_SIZE)


# pprint.pprint(grid)

# 0,1,2,3,4,5
# 0,1,2,3,4,5.      0,0; 0,16; 0, 32; 0, 48; 0, 64; 0, 250; 0, 350; 0,400; 0, 450; 0,500; 0,550; 0,600; 0,650; 0,700; 0,750; 0,800

start_ticks = pygame.time.get_ticks()
FPS = 60

while True:



    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if button_1.collidepoint(mouse) or button_2.collidepoint(mouse):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_1.collidepoint(mouse):
                pass
            
            elif button_2.collidepoint(mouse):
                pass

       

    screen.fill((0, 0, 0))
    for i in range(N):
        for j in range(N):
            pygame.draw.rect(screen,(255,255,0),grid[i][j],4)

    pygame.draw.rect(screen,(0,255,0),button_1,border_radius = 10)
    screen.blit(Generate,(1115,100))
    pygame.draw.rect(screen,(0,255,0),button_2,border_radius = 10)
    screen.blit(Solve,(1175,250))
    screen.blit(Score,(1150,400))

    elapsed_ms = pygame.time.get_ticks() - start_ticks
    seconds = elapsed_ms // 1000
    milliseconds = elapsed_ms % 1000

    # Format text
    time_text = f"{seconds}.{milliseconds:03d} s"
    Time = font_2.render(time_text,True,(255,255,255))
    screen.blit(Time,(1150,600))

  

    pygame.display.flip()
    clock.tick(FPS)
    clock= pygame.time.Clock()