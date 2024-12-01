from utils import data_import


def build_layers(data, width, height):

    layers = []
    for _ in range(len(data) // (width * height)):
        layer = []
        for _ in range(height):
            layer.append([])
        layers.append(layer)

    for index, value in enumerate(data):
        layer = index // (width * height)
        line = (index % (width * height)) // width
        layers[layer][line].append(value)
    return layers


def count_item(layer, item):
    return sum(pixel == item for line in layer for pixel in line)


def part1(data, width=25, height=6):
    layers = build_layers(data, width, height)
    best_layer = min(layers, key=lambda a: count_item(a, '0'))

    return count_item(best_layer, '1') * count_item(best_layer, '2')


def merge_pixels(values):
    for value in values:
        if value != '2':
            return value


def merge_layers(layers):
    height = len(layers[0])
    width = len(layers[0][0])

    image = []
    for _ in range(height):
        image.append([])

    for y in range(height):
        for x in range(width):
            image[y].append(merge_pixels([layer[y][x] for layer in layers]))

    return image


def convert_pixel(pixel):
    if pixel == '1':
        return '#'
    return ' '


def display_layer(layer):
    for line in layer:
        print(''.join(convert_pixel(pixel) for pixel in line))


def part2(data, width=25, height=6):
    layers = build_layers(data, width, height)
    layer = merge_layers(layers)
    display_layer(layer)


if __name__ == '__main__':
    data = data_import('data/y2019/day8')[0]
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is')
    part2(data)
