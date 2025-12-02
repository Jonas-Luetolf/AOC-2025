from typing import Iterable
import re


def mapl(fun: callable, iter: Iterable) -> list:
    return list(map(fun, iter))


def mapt(fun: callable, iter: Iterable) -> tuple:
    return tuple(map(fun, iter))


def get_nums(line, sign=False):
    pattern = r"\b\d+\b"
    if sign:
        pattern = r"[\b+-]?\d+\b"
    return tuple(int(s) for s in re.findall(pattern, line))


def read_inp(filename, dtype=str, sep="\n"):
    with open(filename, "r") as f:
        inp = f.read().rstrip().split(sep)

    return mapl(dtype, inp)


def read_2_part_inp(
    filename, dtype1=str, dtype2=str, part_sep="\n\n", sep1="\n", sep2="\n"
):
    with open(filename, "r") as f:
        inp = f.read().rstrip().split(part_sep)

    inp_part1 = inp[0].split(sep1)
    inp_part2 = inp[1].split(sep2)

    inp_part1 = mapl(lambda s: s.strip(), inp_part1)
    inp_part2 = mapl(lambda s: s.strip(), inp_part2)

    return mapl(dtype1, inp_part1), mapl(dtype2, inp_part2)


def parse_sequence(line: str, sep: str, dtype) -> list:
    return mapl(dtype, line.strip().split(sep))


def parse_2_part_line(
    line: str, part_sep, func1=lambda x: x, func2=lambda x: x
) -> tuple:
    parts = line.split(part_sep)
    assert len(parts) == 2

    return (func1(parts[0]), func2(parts[1]))


def flatten(l: list):
    ret = []

    for sub_list in l:
        ret += sub_list

    return ret
