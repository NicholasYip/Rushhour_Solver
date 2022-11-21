from board import Board
from aa import aa
from ucs import uniform_cost_search
import time
from gbfs import greedy_best_first_search

fileName = 'test.txt'
file = open('../static/' + fileName, "r")

i = 0
for line in file:
    if line[0] == '#' or line == "\n":
        continue
    i = i + 1
    uniform_cost_search(line, i)
    for h in range(1, 5):
        greedy_best_first_search(line, i, h)
    for h in range(1, 5):
        aa(line, i, h)
