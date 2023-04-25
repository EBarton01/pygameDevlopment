import pygame
#import pygame_menu
import random
import menu
import shop
import shared_stats

pygame.init()

class Game:
    def __init__(self):
        #Inilitize the shop
        self.my_stats = shared_stats.Stats()
        self.my_shop = shop.TheShop()

        # Set the window dimensions
        self.WINDOW_WIDTH = 640
        self.WINDOW_HEIGHT = 480

        # Set the square dimensions
        self.SQUARE_WIDTH = 50
        self.SQUARE_HEIGHT = 50

        # Set the initial position of the square
        self.square_x = 200
        self.square_y = 200

        self.rnd_x = random.randint(20,620)
        self.rnd_y = random.randint(60,460)
        self.rnd_width = random.randint(5,10)
        self.rnd_height = random.randint(5,10)

        # Set the movement speed of the square
        self.SPEED = self.my_stats.SPEED

        # Create a window
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        self.font = pygame.font.Font(None, 36)
        self.Varspeed = 1
        self.Strspeed = str(self.Varspeed)

        self.VarPoints = self.my_stats.POINTS
        self.StrPoints = str(self.VarPoints)

        # Render the text
        self.text_speed = self.font.render("Speed:", True, (0, 0, 0))
        self.text_points = self.font.render("points:", True, (0, 0, 0))

    def pause(self):
        menuz = menu.PygameMenu(["Resume", "Shop", "Exit"])
        selected_option = menuz.run() 
        return  selected_option

# Add a main loop
    def main_Loop(self):
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        if self.Varspeed < 10:
                            self.Varspeed += 1
                            self.Strspeed = str(self.Varspeed)
                            self.SPEED = 0.1 * self.Varspeed
                        else:
                            self.Varspeed = 10
                            self.Strspeed = str(self.Varspeed)
                            self.SPEED = 0.1 * self.Varspeed
                    elif event.key == pygame.K_l:
                        if self.Varspeed > 1:
                            self.Varspeed -= 1
                            self.Strspeed = str(self.Varspeed)
                            self.SPEED = 0.1 * self.Varspeed
                        else:
                            self.Varspeed = 1
                            self.Strspeed = str(self.Varspeed)
                            self.SPEED = 0.1 * self.Varspeed

                    elif event.key == pygame.K_SPACE:
                        self.paused = True
                        while self.paused:
                            selected_option = self.pause()
                            if selected_option == "Exit":
                                self.running = False
                                self.paused = False
                                break
                            elif selected_option == "Resume":
                                self.paused = False
                            elif selected_option == "Shop":
                                selection = self.my_shop.open_shop()
                                if selection < 0:
                                    if selection == -1:
                                        print("ran")
                                        self.VarPoints = self.VarPoints - 25
                                        self.StrPoints = str(self.VarPoints)
                                        self.paused = False
                                else:
                                    continue

            # Move the square based on user input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if self.square_x > 0:
                    self.square_x -= self.SPEED
                else:
                    self.square_x = 0
            if keys[pygame.K_RIGHT]:
                if self.square_x < 600:
                    self.square_x += self.SPEED
                else:
                    self.square_x = 600
            if keys[pygame.K_UP]:
                if self.square_y > 25:
                    self.square_y -= self.SPEED
                else:
                    self.square_y = 25
            if keys[pygame.K_DOWN]:
                if self.square_y < 440:
                    self.square_y += self.SPEED
                else:
                    self.square_y = 440

            
            self.text_speed_num = self.font.render(self.Strspeed, True, (0, 0, 0))
            self.points_num = self.font.render(self.StrPoints, True, (0, 0, 0))

            # Draw the updated square to the screen
            self.screen.fill((255, 255, 255)) # Clear the screen
            self.player = pygame.Rect(self.square_x, self.square_y, self.SQUARE_WIDTH, self.SQUARE_HEIGHT)
            self.spot = pygame.Rect(self.rnd_x, self.rnd_y, self.rnd_width, self.rnd_height)

            pygame.draw.rect(self.screen, (0, 0, 255), self.player)
            pygame.draw.rect(self.screen, (0, 0, 0), self.spot)

            if self.player.colliderect(self.spot):
                self.rnd_x = random.randint(20,600)
                self.rnd_y = random.randint(60,440)
                self.rnd_width = random.randint(5,10)
                self.rnd_height = random.randint(5,10)

                self.VarPoints += 1 * self.my_shop.multiply()
                self.StrPoints = str(self.VarPoints)

            self.screen.blit(self.text_speed, (0, 0))
            self.screen.blit(self.text_speed_num, (90, 0))
            self.screen.blit(self.text_points, (510, 0))
            self.screen.blit(self.points_num, (610, 0))

            # Update the screen
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()

Game().main_Loop()