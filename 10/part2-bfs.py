from utils.helper import read_inp, mapl, parse_sequence, get_nums
from collections import deque

inp = read_inp("test_inp.txt")
inp = mapl(str.split, inp)

machines = []

for machine in inp:
    buttons = machine[1:-1]
    buttons = mapl(get_nums, buttons)

    voltages = machine[-1][1:-1]
    voltages = parse_sequence(voltages, sep=",", dtype=int)

    machine = (buttons, voltages)
    machines.append(machine)


def get_next(curr, button):
    res = curr.copy()
    for connection in button:
        res[connection] += 1

    return res


res = 0

for machine in machines:
    buttons, voltages = machine

    start = [0] * len(voltages)
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

        if curr == voltages:
            res += depth[tuple(curr)]
            break

print(res)
