from utils.helper import read_inp, mapl, parse_sequence, get_nums
import numpy as np
import pulp

inp = read_inp("inp.txt")
inp = mapl(str.split, inp)

machines = []

for machine in inp:
    buttons = machine[1:-1]
    buttons = mapl(get_nums, buttons)

    voltages = machine[-1][1:-1]
    voltages = parse_sequence(voltages, sep=",", dtype=int)

    machine = (buttons, voltages)
    machines.append(machine)

res = 0

for machine in machines:
    buttons, voltages = machine

    A = np.zeros((len(voltages), len(buttons)), dtype=int)
    for m, button in enumerate(buttons):
        for i in button:
            A[i][m] = 1

    B = np.array(voltages).T

    solver = pulp.LpProblem("solver", pulp.LpMinimize)
    X = [
        pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(buttons))
    ]

    solver += pulp.lpSum(X)

    for i in range(len(voltages)):
        solver += pulp.lpSum(A[i, j] * X[j] for j in range(len(buttons))) == B[i]

    solver.solve()
    res += sum([x.value() for x in X])

print(int(res))
