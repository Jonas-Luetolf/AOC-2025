def cindex(arr, c):
    return arr[int(c.imag)][int(c.real)]


def cset(arr, c, value):
    arr[int(c.imag)][int(c.real)] = value


def cadd(arr, c, a):
    cset(arr, c, cindex(arr, c) + a)


def crange(c0, c1, realstep=1, imagstep=1):
    for a in range(int(c0.imag), int(c1.imag), imagstep):
        for b in range(int(c0.real), int(c1.real), realstep):
            yield complex(b, a)


def get_neighbors(arr: list[list], c: complex(), self_included: bool = False) -> list:
    neighbors = []

    r_len = len(arr[0])
    i_len = len(arr)

    for neighbor_pos in crange(c - (1 + 1j), c + (2 + 2j)):

        if not self_included and c == neighbor_pos:
            continue

        if 0 <= neighbor_pos.imag < i_len and 0 <= neighbor_pos.real < r_len:
            neighbors.append(cindex(arr, neighbor_pos))

    return neighbors
