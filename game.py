import pygame
import random
import sys
pygame.init()
width=800
height=600
red=(255,0,0)
blue=(0,0,255)
black=(0,0,0)
background_color=(0,0,0)
player_size=50
player_pos=[width/2,height-2*player_size]
enemy_size=50
enemy_pos=[random.randint(0,width-enemy_size),0]
enemy_list=[enemy_pos]
block=10
speed=10
screen=pygame.display.set_mode((width,height))
game_over=False
score= 0
clock=pygame.time.Clock()
myFont=pygame.font.SysFont("cursive", 35)

def cool_color(background_color,score):
    if score < 10:
        background_color=(235, 97, 87)
    elif score < 20:
        background_color=(255, 158, 3)
    elif score < 30:
        background_color=(255, 226, 3)
    elif score < 40:
        background_color=(0, 255, 85)
    elif score < 50:
        background_color=(0, 187, 255)
    elif score < 60:
        background_color=(179, 0, 255)
    else:
        background_color=(255, 0, 191)
    return background_color



def blocks_drop(block,score):
    if score < 20:
        block=70
    elif score < 40:
        block=90
    elif score < 60:
        block=100
    else:
        block=150
    return block

def set_level(score, speed):
    if score < 20:
        speed=10
        
    elif score < 40:
        speed=15
    elif score < 60:
        speed=20  
    else:
        speed=25
    return speed


def drop_enemies(enemy_list):
    delay=random.random()
    if len(enemy_list)<block and delay < 0.1:
        x_pos=random.randint(0,width-enemy_size)    
        y_pos=0
        enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen,blue,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))
        
        
def update_enemy_positions(enemy_list,score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1]<height:
            enemy_pos[1] += speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score


def collision_check(enemy_list,player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos,player_pos):
            return True
    return False

        
       

def detect_collision(player_pos,enemy_pos):
    p_x=player_pos[0]
    p_y=player_pos[1]

    e_x=enemy_pos[0]
    e_y=enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x+player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
        if ( e_y >= p_y and e_y < (p_y+player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
             return True
    return False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type== pygame.KEYDOWN:
            x=player_pos[0]
            y=player_pos[1]
            if event.key==pygame.K_LEFT and x > 0:
                x -= player_size
            elif event.key==pygame.K_RIGHT and x < (width-player_size):
                x += player_size

            player_pos=[x,y]
    
    screen.fill(background_color)
    
    
    background_color=cool_color(background_color,score)
    block=blocks_drop(block,score)
    drop_enemies(enemy_list)
    score=update_enemy_positions(enemy_list,score)
    speed=set_level(score,speed)


    text="Score:"+ str(score)
    label=myFont.render(text,1,black)
    screen.blit(label, (width-200, height-40))

    if collision_check(enemy_list,player_pos):
        game_over=True
        break
    draw_enemies(enemy_list)    

    pygame.draw.rect(screen,red,(player_pos[0],player_pos[1],player_size,player_size))

    clock.tick(30)

    pygame.display.update()
            
        
            
