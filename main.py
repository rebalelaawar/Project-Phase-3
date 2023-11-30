import pygame 
import sys
from game import Game
from bottom_boxes import draw_bottom_boxes
from arrow import Arrow
import random


pygame.init()

print("START")
# Get the user's display info
info_object = pygame.display.Info()
screen_width = info_object.current_w
screen_height = info_object.current_h

# Define the relative screen size percentages
relative_width_percentage = 1
relative_height_percentage = 1

# Calculate the relative screen size
relative_width = int(screen_width * relative_width_percentage)
relative_height = int(screen_height * relative_height_percentage)

# Set up the screen
screen = pygame.display.set_mode((relative_width, relative_height))
pygame.display.set_caption('Code Code Revolution Hero')

# Create clock and font objects
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

#IMPORT SONG 
pygame.mixer.music.load('Sandstorm2.mp3')
pygame.mixer.music.set_volume(0.1)


# Create a background surface and load images
background_surface = pygame.Surface((relative_width, relative_height))

left_arrow = pygame.image.load("arrowLeft.png").convert_alpha()
up_arrow = pygame.image.load('arrowUp.png').convert_alpha()
right_arrow = pygame.image.load("arrowRight.png").convert_alpha()
down_arrow = pygame.image.load("arrowDown.png").convert_alpha()

left_rect = left_arrow.get_rect()
up_rect = up_arrow.get_rect()


monkey = pygame.image.load('monkeywin.png').convert_alpha

background_image = pygame.image.load('DDDR.png').convert()
background_image = pygame.transform.scale(background_image, (relative_width, relative_height))

background_surface.blit(background_image, (0, 0))

text_surface = test_font.render("Code Code Revolution Hero",False, "black")


text_rect = text_surface.get_rect(center = (700,50))

left_arrow_position = 0
up_arrow_position = 0
down_arrow_position = 0
right_arrow_position = 0

# BOTTOM BOXES

#START BUTTON 
start_button = pygame.Rect(relative_width // 2 - 100, relative_height // 2 - 50, 200, 100)
game_started = False

score = 0
running = True


while running:


            
    screen.blit(background_surface,(0,0))

    #SPEED IN WHICH ARROWS FALL
    up_arrow_position += 4
    down_arrow_position += 4
    left_arrow_position += 4
    right_arrow_position += 4


    #DRAWING START BUTTON
    if not game_started:
        
        pygame.draw.rect(screen, 'black', start_button)
        start_text = test_font.render("Start", True, 'blue')
        screen.blit(start_text, (start_button.x + 50, start_button.y + 30))


    #position of top arrows on screen
    if left_arrow_position > screen_height:
        left_arrow_position = -100

    if up_arrow_position > screen_height:
        up_arrow_position = -100

    if right_arrow_position > screen_height:
        right_arrow_position = -100

    if down_arrow_position > screen_height:
        down_arrow_position = -100




    screen.blit(left_arrow, (150, left_arrow_position))
    screen.blit(up_arrow, (500, up_arrow_position))
    screen.blit(down_arrow, (850, down_arrow_position))
    screen.blit(right_arrow, (1200, right_arrow_position))


    

   
    screen.blit(text_surface,text_rect) 
    pygame.draw.rect(screen, 'Pink', text_rect)
    pygame.draw.rect(screen, 'Pink', text_rect,10)
    screen.blit(text_surface,text_rect)

    
    BOTTOM_ARROW_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    rectangles = draw_bottom_boxes(screen, screen_width, screen_height, BOTTOM_ARROW_COLORS, 8)
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


    
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: {}".format(score), True, 'black')
    screen.blit(score_text, (10, 10))

    difficulty = 1 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and game_started:

            # if event.key==pygame.K_UP and any([rectangles[i].collidepoint((500, up_arrow_position)) for i in range(0,4)]):
            if event.key==pygame.K_UP and rectangles[1].collidepoint((500, up_arrow_position)):
                score += 1
                

            elif event.key==pygame.K_RIGHT and rectangles[3].collidepoint((1200, right_arrow_position)):
             score += 1 
             
            elif event.key==pygame.K_DOWN and rectangles[2].collidepoint((850, down_arrow_position)):
             score += 1 
                
            elif event.key==pygame.K_LEFT and rectangles[0].collidepoint((150, left_arrow_position)):
             score += 1

        elif event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
            game_started = True
            pygame.mixer.music.play()
    
    
    pygame.display.update()
    clock.tick(60)




pygame.quit()


