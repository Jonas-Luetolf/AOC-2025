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

for connection in connections:
    a, b, dist = connection

    for circuit in circuits:
        if a in circuit and b in circuit:
            continue

        elif a in circuit:
            circuit.add(b)
            break

        elif b in circuit:
            circuit.add(a)
            break
    else:
        circuits.append({a, b})

    circuits = merge_sets(circuits)

    if len(circuits[0]) == len(boxes):
        print(boxes[connection[0]][0] * boxes[connection[1]][0])
        break
