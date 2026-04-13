import pygame
import sys
import time
import random
from mazeGeneration import algorithm
from mazeSolver import A_star

pygame.init()

icon = pygame.image.load('MAZE.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
pygame.display.set_caption("Maze Game")

WIDTH, HEIGHT = screen.get_size()
WIDTH = min(WIDTH,HEIGHT)
HEIGHT = min(WIDTH,HEIGHT)
N = 20
STEP_SIZE = WIDTH//N

## Buttons
button_1 = pygame.Rect(1100,50,200,100)
button_2 = pygame.Rect(1100,200,200,100)

## Text
font = pygame.font.SysFont(None, 24)
font_2 = pygame.font.SysFont(None,36)
Generate = font.render("Generate New Maze",True,(0,0,0))
Solve = font.render("Hint",True,(0,0,0))
user_score = 0;
clock = pygame.time.Clock()


grid = [[0 for x in range(N)] for x in range(N)]

generated_maze = algorithm(N,N)


for i in range(N):
    for j in range(N):
        grid[i][j]=pygame.Rect(i*STEP_SIZE,j*STEP_SIZE,STEP_SIZE,STEP_SIZE)



start_ticks = pygame.time.get_ticks()
FPS = 60
prev = []
starting_index = (random.randrange(0,N),random.randrange(0,N))
user_movement = [[False for i in range(N)] for i in range(N)]
user_x_position = starting_index[0]
user_y_position = starting_index[1]
user_movement[user_x_position][user_y_position] = True

goal = (random.randrange(0,N),random.randrange(0,N))

user_movement[starting_index[0]][starting_index[1]]=True
while True:
    Score = font_2.render(f"Score: {user_score} ",True,(255,255,255));

    screen.fill((0, 0, 0))
    for i in range(N):
        for j in range(N):
            pygame.draw.rect(screen,(144, 238, 144),grid[i][j])

    if user_x_position==goal[0] and user_y_position==goal[1]:
        user_score+=100
        generated_maze = algorithm(N,N)
        starting_index = (random.randrange(0,N),random.randrange(0,N))
        user_movement = [[False for i in range(N)] for i in range(N)]
        user_movement[starting_index[0]][starting_index[1]]=True
        user_x_position = starting_index[0]
        user_y_position = starting_index[1]
        goal = (random.randrange(0,N),random.randrange(0,N))



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
                starter = pygame.Rect(starting_index[0]*STEP_SIZE,starting_index[1]*STEP_SIZE,STEP_SIZE,STEP_SIZE)
                generated_maze = algorithm(N,N)
                starting_index = (random.randrange(0,N),random.randrange(0,N))
                user_movement = [[False for i in range(N)] for i in range(N)]
                user_x_position = starting_index[0]
                user_y_position = starting_index[1]
                user_movement[starting_index[0]][starting_index[1]]=True
                goal = (random.randrange(0,N),random.randrange(0,N))

            
            elif button_2.collidepoint(mouse):
                result = A_star(starting_index,goal,generated_maze,N,N)

                if not result:
                    starter = pygame.Rect(starting_index[0]*STEP_SIZE,starting_index[1]*STEP_SIZE,STEP_SIZE,STEP_SIZE)
                    generated_maze = algorithm(N,N)
                    starting_index = (random.randrange(0,N),random.randrange(0,N))
                    user_movement = [[False for i in range(N)] for i in range(N)]
                    user_x_position = starting_index[0]
                    user_y_position = starting_index[1]
                    user_movement[starting_index[0]][starting_index[1]]=True
                    goal = (random.randrange(0,N),random.randrange(0,N))
                    continue

                else:
                    #print(result)
                    current_rect_content = []
                    for i in range(len(result)):
                        x,y = result[i]
                        rect_temp = pygame.Rect(x*STEP_SIZE,y*STEP_SIZE,STEP_SIZE,STEP_SIZE)
                        current_rect_content.append(rect_temp)

                    
                    for rect_temp in current_rect_content:
                        pygame.draw.rect(screen,(255,255,255),rect_temp)
                  
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if user_y_position-1 >=0 and not generated_maze[user_y_position-1][user_x_position].bottom_wall:
                    user_y_position-=1

                    if prev and prev[-1]=="s":
                        user_movement[user_x_position][user_y_position+1]=False
                        
                        prev.pop()
                        continue
                 
                    user_movement[user_x_position][user_y_position]=True   

                    prev.append("w")

            elif event.key == pygame.K_s:

                if user_y_position+1 <N and not generated_maze[user_y_position][user_x_position].bottom_wall:
                    user_y_position+=1

                    if prev and prev[-1]=="w":
                        user_movement[user_x_position][user_y_position-1]=False
                        prev.pop()
                        continue

                    else:
                        user_movement[user_x_position][user_y_position]=True 

                    prev.append("s")
            elif event.key == pygame.K_a:
                if user_x_position-1 >= 0 and not generated_maze[user_y_position][user_x_position-1].right_wall:
                    user_x_position-=1

                    if prev and prev[-1]=="d":
                        user_movement[user_x_position+1][user_y_position]=False
                        prev.pop()
                        continue
               
                    user_movement[user_x_position][user_y_position]=True 
                    prev.append("a")

            elif event.key == pygame.K_d:
                if user_x_position+1 <N and not generated_maze[user_y_position][user_x_position].right_wall:
                    user_x_position+=1

                    if prev and prev[-1]=="a":
                        user_movement[user_x_position-1][user_y_position]=False
                        prev.pop()
                        continue

                    user_movement[user_x_position][user_y_position]=True 

                    prev.append("d")

    
            

    pygame.draw.rect(screen,(144, 0, 144),(goal[0]*STEP_SIZE,goal[1]*STEP_SIZE,STEP_SIZE,STEP_SIZE))
    

    for i in range(N):
        for j in range(N):
            if user_movement[i][j]:
                pygame.draw.rect(screen,(255,255,0),((i)*STEP_SIZE,j*STEP_SIZE,STEP_SIZE,STEP_SIZE))
            
           

    for i in range(N):
        for j in range(N):
            if(generated_maze[i][j].right_wall):

                pygame.draw.line(screen,(255,0,0),(j*STEP_SIZE+STEP_SIZE,i*STEP_SIZE),(j*STEP_SIZE+STEP_SIZE,i*STEP_SIZE+STEP_SIZE),4)
            
            if(generated_maze[i][j].bottom_wall):
                pygame.draw.line(screen,(255,0,0),(j*STEP_SIZE,i*STEP_SIZE+STEP_SIZE),(j*STEP_SIZE+STEP_SIZE,i*STEP_SIZE+STEP_SIZE),4)
    



    for i in range(N):
        pygame.draw.line(screen,(255,0,0),(i*STEP_SIZE,0),((i+1)*STEP_SIZE,0),4)

    for i in range(N):
        pygame.draw.line(screen,(255,0,0),(0,i*STEP_SIZE),(0,(i+1)*STEP_SIZE),4)

    



    ## Text ##
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
