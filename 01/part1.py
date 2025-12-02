from utils.helper import *


def move_ptr(curr: int, step: int) -> int:
    return (curr + step) % 100


inp = read_inp("inp.txt")

curr = 50
zeros = 0

for line in inp:
    step = int(line.replace("L", "-").replace("R", ""))
    curr = move_ptr(curr, step)

    zeros += curr == 0

print(zeros)
