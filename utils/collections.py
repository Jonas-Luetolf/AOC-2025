from collections import deque


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def length(self):
        return self.end - self.start

    def intersect(self, other):
        new_start = max(self.start, other.start)
        new_end = min(self.end, other.end)

        if new_start >= new_end:
            return None

        return Range(new_start, new_end)

    def concat(self, other):
        new_start = min(self.start, other.start)
        new_end = max(self.end, other.end)
        return Range(new_start, new_end)

    def overlaps(self, other):
        return not (self.end <= other.start or self.start >= other.end)


def merge_sets(sets: list[set]) -> list[set]:
    sets = deque(sets)
    result = []

    while sets:
        first = sets.popleft()
        merged = True

        while merged:
            merged = False
            remaining = deque()

            while sets:
                curr = sets.popleft()
                if first & curr:
                    first |= curr
                    merged = True

                else:
                    remaining.append(curr)

            sets = remaining

        result.append(first)

    return result
