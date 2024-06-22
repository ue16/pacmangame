import pygame
import sys
from game_constants import WIDTH, HEIGHT, TOP_OFFSET, TIME_BETWEEN_ANIMATIONS

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define fonts
font = pygame.font.Font(None, 25)

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Main menu loop
def Main_menu():
    speed = None
    ghosts = None
    running = True
    while running:
        screen.fill(BLACK)

        draw_text('Main Menu', font, WHITE, screen, 260, 25)
        draw_text('Select Game Speed:', font, WHITE, screen, 200, 125)
        draw_text('1. Slow', font, WHITE, screen, 250, 175)
        draw_text('2. Medium', font, WHITE, screen, 250, 225)
        draw_text('3. Fast', font, WHITE, screen, 250, 275)
        draw_text(f'Selected Speed: {speed}', font, RED, screen, 200, 325)

        draw_text('Select Number of Ghosts:', font, WHITE, screen, 200, 375)
        draw_text('1. One', font, WHITE, screen, 250, 425)
        draw_text('2. Two', font, WHITE, screen, 250, 475)
        draw_text('3. Three', font, WHITE, screen, 250, 525)
        draw_text(f'Selected Ghosts: {ghosts}', font, RED, screen, 200, 575)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if not speed:
                        speed = 50  ##return framerate = 50
                    elif not ghosts:
                        ghosts = 1 ## return number of ghosts accepted
                elif event.key == pygame.K_2:
                    if not speed:
                        speed = 100 ##return framerate = 100
                    elif not ghosts:
                        ghosts = 2 ## return number of ghosts accepted
                elif event.key == pygame.K_3:
                    if not speed:
                        speed = 150  ##return framerate = 150
                    elif not ghosts:
                        ghosts = 3     ## return number of ghosts

                elif event.key == pygame.K_RETURN and speed and ghosts:
                    running = False

    return speed, ghosts

# Call the main menu and get settings
game_speed, num_ghosts = Main_menu()
print(f"Game Speed: {game_speed}, Number of Ghosts: {num_ghosts}")

# Here you would start the main game loop using the chosen settings
# For example:
# start_game(game_speed, num_ghosts)
