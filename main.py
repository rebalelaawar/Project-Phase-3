import pygame 
from bottom_boxes import draw_bottom_boxes
from arrow import Arrow
import random
from quit_button import QuitButton
from lives_tracker import LivesTracker



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

#Streak

show_streak_message = False
streak_message_display_time = 0

#LOADING ARROW IMAGES 
left_arrow = pygame.image.load("arrowLeft.png").convert_alpha()
up_arrow = pygame.image.load('arrowUp.png').convert_alpha()
right_arrow = pygame.image.load("arrowRight.png").convert_alpha()
down_arrow = pygame.image.load("arrowDown.png").convert_alpha()

start_button_img = pygame.image.load('start3.png')
button_pos = (screen_width // 2 - start_button_img.get_width() // 2, screen_height // 2 - start_button_img.get_height() // 2)


background_image = pygame.image.load('Space_Background3.png').convert()
background_image = pygame.transform.scale(background_image, (relative_width, relative_height))

background_surface.blit(background_image, (0, 0))

#INITIAL ARROW POSITIONS 



quit_button = QuitButton(screen)
lives_tracker = LivesTracker(screen)


left_scored = False
right_scored = False
down_scored = False
up_scored = False



while running:
    screen.blit(background_surface,(0,0))

    if not game_started:

        score = 0
        streak = 0
        

        left_arrow_position = random.randint(-300, -200)
        left_arrow_speed = random.randint(2, 3)

        right_arrow_position = random.randint(-800, -300)
        right_arrow_speed = random.randint(2, 3)

        down_arrow_position = random.randint(-900, -400)
        down_arrow_speed = random.randint(2, 3)

        up_arrow_position = random.randint(-1000, -500)
        up_arrow_speed = random.randint(2, 3)

        difficulty = 1
        lives_tracker = LivesTracker(screen)
        caption_img = pygame.image.load('codecode.png')
        caption_pos = (screen_width // 2 - caption_img.get_width() // 2, 50)
        screen.blit(caption_img,caption_pos)
        screen.blit(start_button_img, button_pos)
        

    else:
        screen.blit(score_text, (x_centered, y_top))
        quit_button.draw_button()
        lives_tracker.draw()
        
        if lives_tracker.lives == 0:
            font_game_over = pygame.font.Font(None, 100)
            game_over_text = font_game_over.render("Game Over", True, (255, 0, 0))  # Red color
            game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(game_over_text, game_over_rect)
            
            game_over_display_time = pygame.time.get_ticks()

            while pygame.time.get_ticks() - game_over_display_time < 3000:
                pygame.display.update()
            
            game_started = False
            pygame.mixer.music.stop()

#SETTING ARROW POSITIONS TO THEIR SPEED 

        left_arrow_position += left_arrow_speed
        up_arrow_position += up_arrow_speed
        down_arrow_position += down_arrow_speed
        right_arrow_position += right_arrow_speed

#IF STATEMENTS TO SET ARROW POSITIONS BACK TO TOP AFTER FALLING TO BOTTOM 
        if left_arrow_position > screen_height:
            left_arrow_position = random.randint(-600, -150)
            left_arrow_speed = random.randint(1, 2) * difficulty
            if left_scored == False:
                lives_tracker.lose_life()
            left_scored = False

        if up_arrow_position > screen_height:
            up_arrow_position = random.randint(-600, -150)
            up_arrow_speed = random.randint(1, 2) * difficulty
            if up_scored == False:
                lives_tracker.lose_life()
            up_scored = False

        if right_arrow_position > screen_height:
            right_arrow_position = random.randint(-600, -150)
            right_arrow_speed = random.randint(1, 2) * difficulty
            if right_scored == False:
                lives_tracker.lose_life()
            right_scored = False

        if down_arrow_position > screen_height:
            down_arrow_position = random.randint(-600, -150)
            down_arrow_speed = random.randint(1, 2) * difficulty
            if down_scored == False:
                lives_tracker.lose_life()
            down_scored = False


#BLIT ARROWS ON SCREEN 
        screen.blit(left_arrow, (150, left_arrow_position))
        screen.blit(up_arrow, (500, up_arrow_position))
        screen.blit(down_arrow, (850, down_arrow_position))
        screen.blit(right_arrow, (1200, right_arrow_position))

    

    bottom_box_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    rectangles = draw_bottom_boxes(screen, screen_width, screen_height, bottom_box_colors, 8)
  

    font_path = "nova.ttf" 
    font = pygame.font.Font(font_path, 72)
    score_text = font.render("Score: {}".format(score), True, 'pink')

    score_text_width, score_text_height = font.size("Score: {}".format(score))
    x_centered = (screen_width - score_text_width) // 2
    y_top = 20
    
    # EVENT LOOP FOR ARROW AND HITBOX COLLIDING

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and game_started:
        
            
            if event.key==pygame.K_UP:
                if rectangles[1].collidepoint((500, up_arrow_position + 50 )) and not up_scored:
                    score += 1
                    difficulty += .075
                    up_scored = True 
                    streak += 1
                    pygame.draw.rect(screen, "white", rectangles[1])
                

            elif event.key==pygame.K_RIGHT and rectangles[3].collidepoint((1200, right_arrow_position + 50)) and not right_scored:
                score += 1
                difficulty += .075
                right_scored = True
                streak += 1
                pygame.draw.rect(screen, "white", rectangles[3])
             
            elif event.key==pygame.K_DOWN and rectangles[2].collidepoint((850, down_arrow_position + 50)) and not down_scored:
                score += 1
                difficulty += .075
                down_scored = True
                streak += 1
                pygame.draw.rect(screen, "white", rectangles[2])
                
            elif event.key==pygame.K_LEFT and rectangles[0].collidepoint((150, left_arrow_position + 50)) and not left_scored:
                score += 1
                difficulty += .075
                left_scored = True
                streak += 1
                pygame.draw.rect(screen, "white", rectangles[0])
             

            if streak % 10==0 and streak >0 and not show_streak_message:
                    show_streak_message = True
                    streak_message_display_time = pygame.time.get_ticks() 
                    lives_tracker.gain_life()
                    

                
            if show_streak_message and pygame.time.get_ticks() - streak_message_display_time > 75:
                show_streak_message = False
                    
                    

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                game_started = True
                pygame.mixer.music.play()
            
            elif quit_button.is_clicked(event.pos):
                game_started = False
                streak = 0
                show_streak_message = False
                pygame.mixer.music.stop()

    if show_streak_message:
        font_streak_message = pygame.font.Font(font_path, 50)
        streak_message_text = font_streak_message.render("10 Streak! +1 life", True, 'pink')
        streak_message_rect = streak_message_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(streak_message_text, streak_message_rect)

        


    pygame.display.update()
    clock.tick(60)




pygame.quit()