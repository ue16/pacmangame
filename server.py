import socket
import threading
import pickle
import main
from MainGame import MainGame

def handle_client(client_socket, game):
    while True:
        try:
            # Receive input from the client
            input_data = client_socket.recv(1024)
            if not input_data:
                break
            input_data = pickle.loads(input_data)

            # Update Pacman's direction based on input
            game.set_pacman_direction(input_data)
            
            # Update the game state
            game.update_game()
            
            # Send the updated game state back to the client
            game_state = game.get_game_state()
            client_socket.send(pickle.dumps(game_state))

        except ConnectionResetError:
            break

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9999))
    server.listen(5)
    print('Server listening on port 9999')
    game = main()

    while True:
        client_socket, addr = server.accept()
        print(f'Accepted connection from {addr}')
        client_handler = threading.Thread(target=handle_client, args=(client_socket, game))
        client_handler.start()

if __name__ == '__main__':
    start_server()
