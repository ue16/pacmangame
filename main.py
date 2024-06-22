# main.py
from choice import Main_menu
from MainGame import MainGame

if __name__ == "__main__":
    game_speed, num_ghosts = Main_menu()
    game = MainGame(game_speed, num_ghosts)
    game.game_run()

