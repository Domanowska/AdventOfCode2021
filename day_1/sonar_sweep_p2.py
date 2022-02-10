import fileinput

# --- Day 1: Sonar Sweep, Part 2 ---
# Comparing each single measurement isn't really useful...
# instead, compare the sums of a three-measurement sliding window


def sum_increases(input_array: [int]) -> int:
    count = 0
    previous_sum = sum(input_array[:3])

    for i in range(1, len(input_array)):
        if i > len(input_array)-3:
            break
        elif previous_sum < sum(input_array[i:i+3]):
            count += 1

        previous_sum = sum(input_array[i:i + 3])

    return count


if __name__ == "__main__":
    # Get input from sonar
    sonar_input = []
    for line in fileinput.input("input.txt"):
        sonar_input.append(int(line))

    answer = sum_increases(sonar_input)
    print("Number of sum of three depth measurement increases: ", answer)
