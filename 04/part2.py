from utils.helper import read_inp, mapl
from utils.complexmatrix import cindex, crange, cset, get_neighbors

lines = read_inp("inp.txt")
lines = mapl(list, lines)

end = complex(len(lines[0]), len(lines))

accesseable = 0
last_accesseable = 1

while last_accesseable > 0:
    last_accesseable = 0

    for position in crange(0, end):

        if cindex(lines, position) == "@":
            neighbors = get_neighbors(lines, position)

            if neighbors.count("@") < 4:
                cset(lines, position, "#")
                last_accesseable += 1

    accesseable += last_accesseable

print(accesseable)
