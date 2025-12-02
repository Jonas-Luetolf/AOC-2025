from utils.helper import read_inp

inp = read_inp("inp.txt", sep=",")

numbers = []

for line in inp:
    a, b = int(line.split("-")[0]), int(line.split("-")[1])

    for i in range(a, b + 1):
        i_str = str(i)

        if i_str[0 : len(i_str) // 2] == i_str[len(i_str) // 2 :]:
            numbers.append(i)

print(sum(set(numbers)))
