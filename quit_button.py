
import pygame

class QuitButton:
    def __init__(self, screen):
        self.screen = screen
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)
        self._prep_button()

    def _prep_button(self):
        self.text_image = self.font.render("Quit", True, self.text_color)
        self.rect = self.text_image.get_rect()
        self.rect.topright = (self.screen.get_width() - 20, 20)

    def draw_button(self):
        self.screen.blit(self.text_image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)