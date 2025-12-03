from utils.helper import read_inp, mapl

banks = read_inp("inp.txt")
banks = mapl(list, banks)

voltages = []

for bank in banks:
    bank = mapl(int, bank)

    digits = []
    last_index = -1

    for end in range(len(bank) - 11, len(bank) + 1):
        sub_bank = bank[(last_index + 1):end]
        digit = max(sub_bank)

        last_index = sub_bank.index(digit) + last_index + 1
        digits.append(digit)

    voltage = 0

    for pow, digit in enumerate(digits):
        voltage += digit * (10 ** (11 - pow))

    voltages.append(voltage)


print(sum(voltages))
