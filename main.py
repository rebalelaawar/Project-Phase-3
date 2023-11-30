import pygame 
import sys
from game import Game
from bottom_boxes import draw_bottom_boxes
from arrow import Arrow
import random


pygame.init()

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



# Create clock and font objects
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

#IMPORT SONG 
pygame.mixer.music.load('Sandstorm2.mp3')
pygame.mixer.music.set_volume(0.1)


# Create a background surface and load images
background_surface = pygame.Surface((relative_width, relative_height))

#START BUTTON 
start_button = pygame.Rect(relative_width // 2 - 100, relative_height // 2 - 50, 200, 100)
game_started = False

score = 0
running = True



left_arrow = pygame.image.load("arrowLeft.png").convert_alpha()
up_arrow = pygame.image.load('arrowUp.png').convert_alpha()
right_arrow = pygame.image.load("arrowRight.png").convert_alpha()
down_arrow = pygame.image.load("arrowDown.png").convert_alpha()

start_button_img = pygame.image.load('start3.png')
button_pos = (screen_width // 2 - start_button_img.get_width() // 2, screen_height // 2 - start_button_img.get_height() // 2)

caption_img = pygame.image.load('codecode.png')
caption_pos = (screen_width // 2 - caption_img.get_width() // 2, 50)



background_image = pygame.image.load('Space_Background3.png').convert()
background_image = pygame.transform.scale(background_image, (relative_width, relative_height))

background_surface.blit(background_image, (0, 0))


left_arrow_position = random.randint(-200, -100)
left_arrow_speed = random.randint(2, 6)

right_arrow_position = random.randint(-200, -100)
right_arrow_speed = random.randint(2, 6)

down_arrow_position = random.randint(-200, -100)
down_arrow_speed = random.randint(2, 6)

up_arrow_position = random.randint(-200, -100)
up_arrow_speed = random.randint(2, 6)

# left_arrow_position %= screen_height
# up_arrow_position %= screen_height
# down_arrow_position %= screen_height
# right_arrow_position %= screen_height

difficulty = 1

while running:

    

    screen.blit(background_surface,(0,0))

    if not game_started:
        
        screen.blit(start_button_img, button_pos)
        
        

    else:

        
        left_arrow_position += left_arrow_speed
        up_arrow_position += up_arrow_speed
        down_arrow_position += down_arrow_speed
        right_arrow_position += right_arrow_speed

        if left_arrow_position > screen_height:
            left_arrow_position = random.randint(-600, -100)
            left_arrow_speed = random.randint(1, 4) * difficulty

        if up_arrow_position > screen_height:
            up_arrow_position = random.randint(-600, -100)
            up_arrow_speed = random.randint(1, 4) * difficulty

        if right_arrow_position > screen_height:
            right_arrow_position = random.randint(-600, -100)
            right_arrow_speed = random.randint(1, 4) * difficulty

        if down_arrow_position > screen_height:
            down_arrow_position = random.randint(-600, -100)
            down_arrow_speed = random.randint(1, 4) * difficulty

        screen.blit(left_arrow, (150, left_arrow_position))
        screen.blit(up_arrow, (500, up_arrow_position))
        screen.blit(down_arrow, (850, down_arrow_position))
        screen.blit(right_arrow, (1200, right_arrow_position))

    screen.blit(caption_img,caption_pos)
    # pygame.draw.rect(screen, 'Pink', text_rect)
    # pygame.draw.rect(screen, 'Pink', text_rect,10)
    

    BOTTOM_ARROW_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    rectangles = draw_bottom_boxes(screen, screen_width, screen_height, BOTTOM_ARROW_COLORS, 8)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: {}".format(score), True, 'white')
    screen.blit(score_text, (10, 10))

    

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and game_started:

            if event.key==pygame.K_UP and rectangles[1].collidepoint((500, up_arrow_position)):
                score += 1
                difficulty += .1

            elif event.key==pygame.K_RIGHT and rectangles[3].collidepoint((1200, right_arrow_position)):
             score += 1
             difficulty += .1
             
            elif event.key==pygame.K_DOWN and rectangles[2].collidepoint((850, down_arrow_position)):
             score += 1
             difficulty += .1
                
            elif event.key==pygame.K_LEFT and rectangles[0].collidepoint((150, left_arrow_position)):
             score += 1
             difficulty += .1

        elif event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
            game_started = True
            pygame.mixer.music.play()


    pygame.display.update()
    clock.tick(60)




pygame.quit()