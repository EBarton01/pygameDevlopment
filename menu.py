import pygame
pygame.init()

class PygameMenu:
    def __init__(self, options, screen_width=800, screen_height=600):
        self.options = options
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render("Menu", True, (255, 255, 255))
        self.option_positions = self._calculate_option_positions()
        
    def _calculate_option_positions(self):
        positions = []
        for i in range(len(self.options)):
            option = self.options[i]
            option_text = self.font.render(option, True, (255, 255, 255))
            x = self.screen_width / 2 - option_text.get_width() / 2
            y = self.screen_height / 2 - self.font.get_height() * (len(self.options) / 2 - i)
            positions.append((option_text, (x, y)))
        return positions
    
    def _get_option(self, mouse_pos):
        for i in range(len(self.options)):
            option_text, position = self.option_positions[i]
            if position[0] <= mouse_pos[0] <= position[0] + option_text.get_width() and \
                    position[1] <= mouse_pos[1] <= position[1] + option_text.get_height():
                return self.options[i]
        return None
    
    def run(self):
        menu_running = True
        while menu_running:
            self.screen.blit(self.text, (self.screen_width/2 - self.text.get_width()/2, 50))
            for option_text, position in self.option_positions:
                self.screen.blit(option_text, position)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    selected_option = self._get_option(mouse_pos)
                    if selected_option is not None:
                        return selected_option
                    