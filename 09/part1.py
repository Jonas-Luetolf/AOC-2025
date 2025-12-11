from utils.helper import read_inp, mapl, get_nums

tiles = read_inp("inp.txt")
tiles = mapl(get_nums, tiles)

areas = []
for i, tile_a in enumerate(tiles):
    for j, tile_b in enumerate(tiles[i:]):
        x_len = abs(tile_b[0] - tile_a[0]) + 1
        y_len = abs(tile_b[1] - tile_a[1]) + 1

        area = x_len * y_len

        areas.append((i, i + j, area))
areas = sorted(areas, key=lambda x: x[2], reverse=True)

print(areas[0][2])
