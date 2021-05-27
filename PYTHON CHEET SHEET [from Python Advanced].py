# 1. [:] - splitting string into characters
text = 'koi si'
reversed_word = []
reversed_word[:] = text
# ['k', 'o', 'i', ' ', 's', 'i']

#2 rotate - rotating a list/counting n times /with deque/:
from collections import deque
players_left = deque(input())
players_left.rotate(-int(input()))
player_out = players_left.pop()

