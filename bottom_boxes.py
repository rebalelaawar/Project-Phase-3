import pygame

def draw_bottom_boxes(screen, screen_width, screen_height, bottom_box_colors, border,):
    bottom_box_width = 200
    bottom_box_height = 155
    bottom_box_spacing = 250

    bottom_box_y = screen_height - bottom_box_height - 175  # Y position for boxes

  
  
    bottom_box_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

    bottom_num_box = 4  # Change this value to adjust the number of arrows
    bottom_box_spacing = (screen_width - (bottom_box_width * bottom_num_box)) // (bottom_num_box + 1)
    bottom_box_x_positions = [bottom_box_spacing * (i + 1) + bottom_box_width * i for i in range(bottom_num_box)]

    bottom_arrow_rects = []

    for i, color in enumerate(bottom_box_colors):
        arrow_rect = pygame.Rect(bottom_box_x_positions[i], bottom_box_y, bottom_box_width, bottom_box_height)
        pygame.draw.rect(screen, color, arrow_rect, border)
        bottom_arrow_rects.append(arrow_rect)

    return bottom_arrow_rects









    
