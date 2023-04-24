import pygame
import pygame_menu
import random
import menu
import shop
#test comit


# Initialize Pygame
pygame.init()

# Set the window dimensions
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Set the square dimensions
SQUARE_WIDTH = 50
SQUARE_HEIGHT = 50

# Set the initial position of the square
square_x = 200
square_y = 200

rnd_x = random.randint(20,620)
rnd_y = random.randint(60,460)
rnd_width = random.randint(5,10)
rnd_height = random.randint(5,10)

# Set the movement speed of the square
SPEED = 0.1

# Create a window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

font = pygame.font.Font(None, 36)
Varspeed = 1
Strspeed = str(Varspeed)

VarPoints = 0
StrPoints = str(VarPoints)

# Render the text
text_speed = font.render("Speed:", True, (0, 0, 0))
text_points = font.render("points:", True, (0, 0, 0))

#Inilitize the shop
my_shop = shop.TheShop()

def pause():
    menuz = menu.PygameMenu(["Resume", "Shop", "Exit"])
    selected_option = menuz.run() 
    return  selected_option

# Add a main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                if Varspeed < 10:
                    Varspeed += 1
                    Strspeed = str(Varspeed)
                    SPEED = 0.1 * Varspeed
                else:
                    Varspeed = 10
                    Strspeed = str(Varspeed)
                    SPEED = 0.1 * Varspeed
            elif event.key == pygame.K_l:
                if Varspeed > 1:
                    Varspeed -= 1
                    Strspeed = str(Varspeed)
                    SPEED = 0.1 * Varspeed
                else:
                    Varspeed = 1
                    Strspeed = str(Varspeed)
                    SPEED = 0.1 * Varspeed

            elif event.key == pygame.K_SPACE:
                paused = True
                while paused:
                    selected_option = pause()
                    if selected_option == "Exit":
                        paused = False
                        running = False
                    elif selected_option == "Resume":
                        paused = False
                    elif selected_option == "Shop":
                        selection = my_shop.open_shop()
                        if selection < 0:
                            paused = False
                        else:
                            continue

    # Move the square based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if square_x > 0:
            square_x -= SPEED
        else:
            square_x = 0
    if keys[pygame.K_RIGHT]:
        if square_x < 600:
            square_x += SPEED
        else:
            square_x = 600
    if keys[pygame.K_UP]:
        if square_y > 25:
            square_y -= SPEED
        else:
            square_y = 25
    if keys[pygame.K_DOWN]:
        if square_y < 440:
            square_y += SPEED
        else:
            square_y = 440

    
    text_speed_num = font.render(Strspeed, True, (0, 0, 0))
    points_num = font.render(StrPoints, True, (0, 0, 0))

    # Draw the updated square to the screen
    screen.fill((255, 255, 255)) # Clear the screen
    player = pygame.Rect(square_x, square_y, SQUARE_WIDTH, SQUARE_HEIGHT)
    spot = pygame.Rect(rnd_x, rnd_y, rnd_width, rnd_height)

    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (0, 0, 0), spot)

    if player.colliderect(spot):
        rnd_x = random.randint(20,600)
        rnd_y = random.randint(60,440)
        rnd_width = random.randint(5,10)
        rnd_height = random.randint(5,10)

        VarPoints += 1 * my_shop.multiply()
        StrPoints = str(VarPoints)

    screen.blit(text_speed, (0, 0))
    screen.blit(text_speed_num, (90, 0))
    screen.blit(text_points, (510, 0))
    screen.blit(points_num, (610, 0))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()