from utils.helper import *

inp = read_inp("inp.txt")

curr = 50
zeros = 0

for line in inp:
    step = int(line.replace("L", "-").replace("R", ""))

    last = curr
    curr = curr + step

    if step > 0:
        zeros_passed = (curr // 100) - (last // 100)

    else:
        zeros_passed = ((last - 1) // 100) - ((curr - 1) // 100)

    zeros += zeros_passed

print(zeros)
