def cindex(arr, c):
    return arr[int(c.imag)][int(c.real)]


def complexset(arr, c, value):
    arr[int(c.imag)][int(c.real)] = value



def crange(c0, c1, realstep = 1, imagstep = 1):
    for a in range(int(c0.imag), int(c1.imag), imagstep):
        for b in range(int(c0.real), int(c1.real), realstep):
            yield complex(a, b)
