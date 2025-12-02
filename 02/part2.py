from utils.helper import read_inp

inp = read_inp("inp.txt", sep=",")

numbers = []

for line in inp:
    a, b = int(line.split("-")[0]), int(line.split("-")[1])

    for i in range(a, b + 1):
        i_str = str(i)

        for l in range(1, len(i_str) // 2 + 1):
            seq = i_str[0:l]
            if seq * (len(i_str) // l) == i_str:
                numbers.append(i)
                break

print(sum(set(numbers)))
