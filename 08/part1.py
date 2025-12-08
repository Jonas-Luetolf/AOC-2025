from utils.helper import read_inp, mapt
from utils.collections import merge_sets

boxes = read_inp("inp.txt")
boxes = [mapt(int, box.split(",")) for box in boxes]

circuits = []
connections = []

for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        dist = sum((boxes[i][k] - boxes[j][k]) ** 2 for k in range(3))
        connections.append((i, j, dist))


connections = sorted(connections, key=lambda x: x[2])

connections_made = 0

for connection in connections:
    a, b, dist = connection

    for circuit in circuits:
        if a in circuit and b in circuit:
            continue

        elif a in circuit or b in circuit:
            circuit.add(a)
            circuit.add(b)

            connections_made += 1
            break

    else:
        circuits.append({a, b})
        connections_made += 1

    if connections_made == 1000:
        break


circuits = merge_sets(circuits)
circuits = sorted(circuits, key=lambda x: len(x), reverse=True)

print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))
