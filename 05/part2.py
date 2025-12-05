from utils.helper import read_2_part_inp, get_nums, mapl
from utils.collections import Range
from functools import reduce


class Container:
    def __init__(self):
        self.ranges = []

    def add(self, new_range):
        if self.ranges and self.ranges[-1].overlaps(new_range):
            new_range = new_range.concat(self.ranges[-1])
            self.ranges[-1] = new_range

        else:
            self.ranges.append(new_range)

        return self


ranges, _ = read_2_part_inp("inp.txt")

ranges = mapl(lambda line: Range(get_nums(line)[0], get_nums(line)[1] + 1), ranges)
ranges.sort(key=lambda r: r.start)

while any(map(lambda r1, r2: r1.overlaps(r2), ranges[:-1], ranges[1:])):
    c0 = Container()

    container = reduce(lambda c, r: c.add(r), ranges, c0)
    container.ranges.sort(key=lambda r: r.start)

    ranges = container.ranges


lenght = reduce(lambda curr, r: curr + r.length(), ranges, 0)

print(lenght)
