from utils.helper import read_inp, mapl
from utils.matrix import transpose
from utils.math import prod

lines = read_inp("inp.txt")
lines = mapl(str.split, lines)
columns = transpose(lines)

result = 0

for col in columns:
    if col[-1] == "+":
        result += sum(mapl(int, col[:-1]))

    elif col[-1] == "*":
        result += prod(mapl(int, col[:-1]))

print(result)
