from utils.helper import read_inp, mapl
from utils.complexmatrix import cindex, cset, cadd, crange


lines = read_inp("inp.txt")
lines = mapl(list, lines)

timelines = [[0] * len(lines[0]) for i in range(len(lines))]

start = lines[0].index("S")
cset(timelines, start, 1)

for pos in crange(0, complex(len(lines[0]), len(lines))):
    timelines_before = cindex(timelines, pos - 1j)

    if cindex(lines, pos) == ".":
        cadd(timelines, pos, timelines_before)

    elif cindex(lines, pos) == "^":
        cadd(timelines, pos - 1, timelines_before)
        cadd(timelines, pos + 1, timelines_before)

print(sum(timelines[-1]))
