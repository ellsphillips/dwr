from itertools import cycle, product

COLOURS = ["red", "green", "blue"]

OPACITIES = ["100", "70", "40"]

COLOUR_WHEEL = cycle(product(OPACITIES, COLOURS))


def get_colour_spec() -> str:
    return "!".join(reversed(next(COLOUR_WHEEL)))


for _ in range(30):
    print(get_colour_spec())
