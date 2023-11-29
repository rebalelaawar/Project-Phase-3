import pygame 





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif keys[pygame.K_LEFT] and left_arrow_rect.colliderect(left_hitbox):
            score += 1 

        elif keys[pygame.K_UP] and up_hitbox.colliderect(up_hitbox):
            score += 1 
        
        elif keys[pygame.K_RIGHT] and right_hitbox.colliderect(right_hitbox):
            score += 1 

        elif keys[pygame.K_DOWN] and down_hitbox.colliderect(down_hitbox):
            score += 1 
