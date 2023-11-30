import pygame

class LivesTracker:
    def __init__(self, screen, initial_lives=10):
        self.screen = screen
        self.lives = initial_lives
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)  # White color for lives
        self._prep_text()

    def _prep_text(self):
        lives_text = f"Lives: {self.lives}"
        self.text_image = self.font.render(lives_text, True, self.text_color)

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            self._prep_text()

    def gain_life(self):
        self.lives += 1
        self._prep_text()

    def draw(self):
        self.screen.blit(self.text_image, (20, 10))  # Set the position directly when drawing