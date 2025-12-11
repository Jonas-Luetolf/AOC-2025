from utils.helper import read_inp

inp = read_inp("inp.txt")
devices = {}

for line in inp:
    name, connections = line.split(":")[0], line.split(":")[1]
    connections = connections.strip().split()
    devices.update({name: connections})

paths = {}
stack = [("you", 0)]

while stack:
    curr, visited = stack.pop()
    if not visited:
        if curr in paths:
            continue

        elif curr == "out":
            paths["out"] = 1

        else:
            stack.append((curr, 1))

            for next in devices[curr]:
                stack.append((next, 0))

    else:
        paths[curr] = sum(paths[next] for next in devices[curr])

print(paths["you"])
