import pygame 
from game import Game


pygame.init()
screen = pygame.display.set_mode((1200,800))

pygame.display.set_caption("Dance Dance Revolution")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)


left_arrow = pygame.image.load("arrowLeft.png").convert_alpha()
up_arrow = pygame.image.load('arrowUp.png').convert_alpha()
right_arrow = pygame.image.load("arrowRight.png").convert_alpha()
down_arrow = pygame.image.load("arrowDown.png").convert_alpha()


background_surface = pygame.Surface((1200,800))
background_surface.fill('Black')


text_surface = test_font.render("Code Code Revolution Hero",False, "Black")

text_rect = text_surface.get_rect(center = (600,50))

# penguin_surface = pygame.image.load("newguy.jpeg").convert_alpha()
up_arrow_position = 500
down_arrow_position = 300
left_arrow_position = 600
right_arrow_position = 400


keys = pygame.key.get_pressed()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif keys[pygame.K_UP]:
                up_arrow_rect = pygame.Rect(500, up_arrow_position)
                print("")
        if keys[pygame.K_RIGHT]:
             print("")
        if keys[pygame.K_DOWN]:
             print("")
        if keys[pygame.K_LEFT]:
             print("")
       
             
        
        
            
    screen.blit(background_surface,(0,0))

    up_arrow_position += 4
    down_arrow_position += 4
    left_arrow_position += 4 
    right_arrow_position += 4
    
    if left_arrow_position > 1000: left_arrow_position = -100
    screen.blit(left_arrow, (300, left_arrow_position))

    if up_arrow_position >1000: up_arrow_position = -100
    screen.blit(up_arrow,(400,up_arrow_position))
    

    if right_arrow_position > 1000: right_arrow_position = -100
    screen.blit(right_arrow,(500,right_arrow_position))

    if down_arrow_position > 1000: down_arrow_position = -100
    screen.blit(down_arrow,(600,down_arrow_position))

   
    screen.blit(text_surface,text_rect) 
    pygame.draw.rect(screen, 'Pink', text_rect)
    pygame.draw.rect(screen, 'Pink', text_rect,10)
    screen.blit(text_surface,text_rect)


   
    
    
    pygame.display.update()
    clock.tick(60)




pygame.quit()



