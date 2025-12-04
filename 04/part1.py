from utils.helper import read_inp, mapl
from utils.complexmatrix import cindex, crange, get_neighbors

lines = read_inp("inp.txt")
lines = mapl(list, lines)
end = complex(len(lines[0]), len(lines))

accesseable = 0

for position in crange(0, end):

    if cindex(lines, position) == "@":
        neighbors = get_neighbors(lines, position)

        if neighbors.count("@") < 4:
            accesseable += 1


print(accesseable)
