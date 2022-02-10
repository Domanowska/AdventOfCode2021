import fileinput

# --- Day 2: Dive!, Part 2 ---
# You find the submarine manual and discover that the process is actually
# slightly more complicated.
# In addition to horizontal position and depth, you'll also need to track a third value,
# aim, which also starts at 0.
# The commands also mean something entirely different than you first thought:
#     down X increases your aim by X units.
#     up X decreases your aim by X units.
#     forward X does two things:
#         It increases your horizontal position by X units.
#         It increases your depth by your aim multiplied by X.


def get_improved_position(input_arr: [str]) -> {}:
    latitude, depth, aim = 0, 0, 0
    for x in input_arr:
        which_line = x.split(' ')
        if "forward" in which_line:
            latitude += int(which_line[1])
            depth += int(which_line[1]) * aim
        if "down" in which_line:
            aim += int(which_line[1])
        if "up" in which_line:
            aim -= int(which_line[1])

    return {
        'latitude': latitude,
        'depth': depth
    }


if __name__ == "__main__":
    instructions = []
    for line in fileinput.input("input.txt"):
        instructions.append(line)

    position = get_improved_position(instructions)

    print("Horizontal position is", position['latitude'])
    print("Depth is", position['depth'])
    print("Puzzle answer:", position['latitude'] * position['depth'],
          f"({position['latitude']} * {position['depth']})")
