from utils.helper import read_inp, mapl
from utils.matrix import transpose

lines = read_inp("inp.txt")
lines = mapl(list, lines)

max_line_len = max(map(len, lines))

for line in lines:
    line += [" "] * (max_line_len - len(line))

columns = transpose(lines)
columns = list(filter(lambda x: any(c != " " for c in x), columns))

result = 0
curr_res = 0
operation = "+"

for col in columns:
    if col[-1] in ["+", "*"]:
        result += curr_res

        operation = col[-1]
        curr_res = int("".join(col[:-1]).strip())

    else:
        num = int("".join(col[:-1]).strip())

        if operation == "+":
            curr_res += num

        elif operation == "*":
            curr_res *= num

result += curr_res
print(result)
