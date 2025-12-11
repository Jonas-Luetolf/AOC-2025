from utils.helper import read_inp, mapl, get_nums
from collections import deque

inp = read_inp("inp.txt")
inp = mapl(str.split, inp)

machines = []

for machine in inp:
    indicators = list(machine[0].replace("#", "1").replace(".", "0"))[1:-1]
    indicators = mapl(bool, mapl(int, indicators))

    buttons = machine[1:-1]
    buttons = mapl(get_nums, buttons)

    machine = (indicators, buttons)
    machines.append(machine)


def get_next(curr, button):
    res = curr.copy()
    for connection in button:
        res[connection] ^= 1

    return res


res = 0
for machine in machines:
    indicators, buttons = machine

    start = [0] * len(indicators)
    depth = {tuple(start): 0}
    queue = deque([start])
    visited = [start]

    while queue:
        curr = queue.popleft()
        for button in buttons:
            next = get_next(curr, button)

            if next not in visited:
                visited.append(next)
                depth.update({tuple(next): depth[tuple(curr)] + 1})
                queue.append(next)

        if curr == indicators:
            res += depth[tuple(curr)]
            break

print(res)
