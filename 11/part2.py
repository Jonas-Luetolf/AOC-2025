from utils.helper import read_inp

inp = read_inp("inp.txt")
devices = {}

for line in inp:
    name, connections = line.split(":")[0], line.split(":")[1]
    connections = connections.strip().split()
    devices.update({name: connections})

paths = {}
stack = [("svr", False, False, 0)]

while stack:
    curr, visited_fft, visited_dac, visited = stack.pop()
    key = (curr, visited_fft, visited_dac)

    if not visited:
        if key in paths:
            continue

        elif curr == "out":
            paths[key] = visited_fft and visited_dac

        else:
            stack.append((curr, visited_fft, visited_dac, 1))

            for next in devices[curr]:

                stack.append(
                    (
                        next,
                        visited_fft or next == "fft",
                        visited_dac or next == "dac",
                        0,
                    )
                )
    else:
        new_paths = 0
        for next in devices[curr]:
            next_key = (
                next,
                visited_fft or next == "fft",
                visited_dac or next == "dac",
            )

            new_paths += paths[next_key]

        paths[key] = new_paths


print(paths[("svr", False, False)])
