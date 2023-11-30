import pygame

def draw_bottom_boxes(screen, screen_width, screen_height, BOTTOM_ARROW_COLORS, border, glow_thickness=5):
    bottom_arrow_width = 200
    bottom_arrow_height = 155
    bottom_arrow_spacing = 250

    bottom_arrow_y = screen_height - bottom_arrow_height - 175  # Y position for boxes

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BOTTOM_ARROW_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

    bottom_num_arrows = 4  # Change this value to adjust the number of arrows
    bottom_arrow_spacing = (screen_width - (bottom_arrow_width * bottom_num_arrows)) // (bottom_num_arrows + 1)
    bottom_arrow_x_positions = [bottom_arrow_spacing * (i + 1) + bottom_arrow_width * i for i in range(bottom_num_arrows)]

    bottom_arrow_rects = []

    for i, color in enumerate(BOTTOM_ARROW_COLORS):
        arrow_rect = pygame.Rect(bottom_arrow_x_positions[i], bottom_arrow_y, bottom_arrow_width, bottom_arrow_height)
        pygame.draw.rect(screen, color, arrow_rect, border)
        bottom_arrow_rects.append(arrow_rect)

    return bottom_arrow_rects









    
