from utils.helper import read_2_part_inp, get_nums, mapl

ranges, ingredients = read_2_part_inp("inp.txt")

ingredients = mapl(int, ingredients)
ranges = mapl(lambda line: range(get_nums(line)[0], get_nums(line)[1] + 1), ranges)

filtered = filter(
    lambda ingredient: any(map(lambda r: ingredient in r, ranges)), ingredients
)

print(len(list(filtered)))
