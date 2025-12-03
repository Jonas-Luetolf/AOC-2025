from utils.helper import read_inp, mapl

banks = read_inp("inp.txt")
banks = mapl(list, banks)

voltages = []

for bank in banks:
    bank = mapl(int, bank)

    first_digit = max(bank[:-1])
    first_index = bank.index(first_digit)

    second_digit = max(bank[(first_index + 1):])

    voltages.append(first_digit * 10 + second_digit)

print(sum(voltages))
