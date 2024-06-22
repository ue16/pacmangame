import socket
import threading
import pickle
import pygame
import sys
from game_constants import WIDTH, HEIGHT, TILE_SIZE

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Client Game')
clock = pygame.time.Clock()

game_state = None
##receive game
def receive_game_state(client_socket):
    global game_state
    while True:
        try:
            game_state = pickle.loads(client_socket.recv(1024))
        except ConnectionResetError:
            break

def draw_game_state(screen, game_state):
    screen.fill((0, 0, 0))  # Clear screen with black background

    if game_state:
        pacman = game_state['pacman']
        ghosts = game_state['ghosts']

        # Draw Pacman
        pygame.draw.circle(screen, (255, 255, 0), (pacman[0], pacman[1]), TILE_SIZE // 2)

        # Draw Ghosts
        for ghost in ghosts:
            pygame.draw.circle(screen, (255, 0, 0), (ghost[0], ghost[1]), TILE_SIZE // 2)

    pygame.display.update()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    
    # Start a thread to receive game state updates
    receive_thread = threading.Thread(target=receive_game_state, args=(client,))
    receive_thread.start()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                client.close()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                input_data = None
                if event.key == pygame.K_RIGHT:
                    input_data = 'right'
                elif event.key == pygame.K_LEFT:
                    input_data = 'left'
                elif event.key == pygame.K_UP:
                    input_data = 'up'
                elif event.key == pygame.K_DOWN:
                    input_data = 'down'
                if input_data:
                    client.send(pickle.dumps(input_data))

        draw_game_state(screen, game_state)
        clock.tick(60)  # Cap the frame rate

if __name__ == '__main__':
    start_client()


