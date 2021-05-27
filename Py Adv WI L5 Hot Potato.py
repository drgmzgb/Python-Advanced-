# Py Adv WI L5 Hot Potato

# input
# Tracy Emily Daniel
# 2
# output
# Removed Emily
# Removed Tracy
# Last is Daniel

player_in_game = input()
times = int(input())
players_left = player_in_game.split()
from collections import deque
while len(players_left) > 1:
    players_left = deque(players_left)
    players_left.rotate(-times)
    player_out = players_left.pop()
    print(f"Removed {player_out}")
last_player_out = players_left.pop()
print(f'Last is {last_player_out}')