import fileinput

# --- Day 1: Sonar Sweep ---
# You have accidentally dropped santa's sleigh keys into the ocean.
# Santa's elves have a submarine with sonar equipped.
# On a small screen, the sonar sweep report (your puzzle input) appears:
# each line is a measurement of the sea floor depth as the sweep looks further
# and further away from the submarine.
# Figure out how quickly the depth increases, just so you know what you're dealing with
# - you never know if the keys will get carried into deeper water by an
# ocean current or a fish or something.
# To do this, count the number of times a depth measurement increases
# from the previous measurement.


def count_increases(input_array: [int]) -> int:
    count = 0
    previous_input = input_array[0]
    for x in input_array[1:]:
        if previous_input < x:
            count += 1
        previous_input = x

    return count


if __name__ == "__main__":
    # Get input from sonar
    sonar_input = []
    for line in fileinput.input("input.txt"):
        sonar_input.append(int(line))

    answer = count_increases(sonar_input)
    print("Number of depth measurement increases: ", answer)
