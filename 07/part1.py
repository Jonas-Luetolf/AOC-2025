from utils.helper import read_inp, mapl
from utils.complexmatrix import cindex
from collections import deque

lines = read_inp("inp.txt")
lines = mapl(list, lines)

start = lines[0].index("S")

visited = []
splits = []
neighbors = deque([start])

while neighbors:
    curr = neighbors.popleft()

    if curr in visited:
        continue

    visited.append(curr)

    if cindex(lines, curr) == "^":
        splits.append(curr)
        neighbors.append(curr - 1)
        neighbors.append(curr + 1)

    else:
        if curr.imag < len(lines) - 1:
            neighbors.append(curr + 1j)

print(len(set(splits)))
