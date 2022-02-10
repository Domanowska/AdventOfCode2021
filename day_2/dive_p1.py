import fileinput

# --- Day 2: Dive! ---
# It seems like the submarine can take a series of commands like
# forward 1, down 2, or up 3:
#     forward X increases the horizontal position by X units.
#     down X increases the depth by X units.
#     up X decreases the depth by X units.
# The submarine seems to already have a planned course (your puzzle input).
# You should probably figure out where it's going.


def get_position(input_arr: [str]) -> {}:
    latitude, depth = 0, 0
    for x in input_arr:
        which_line = x.split(' ')
        if "forward" in which_line:
            latitude += int(which_line[1])
        if "down" in which_line:
            depth += int(which_line[1])
        if "up" in which_line:
            depth -= int(which_line[1])

    return {
        'latitude': latitude,
        'depth': depth
    }


if __name__ == "__main__":
    instructions = []
    for line in fileinput.input("input.txt"):
        instructions.append(line)

    position = get_position(instructions)

    print("Horizontal position is", position['latitude'])
    print("Depth is", position['depth'])
    print("Puzzle answer:", position['latitude'] * position['depth'],
          f"({position['latitude']} * {position['depth']})")
