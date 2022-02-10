import fileinput

# --- Day 3: Binary Diagnostic, Part 2 ---
# Next, you should verify the life support rating, which can be determined by
# multiplying the oxygen generator rating by the CO2 scrubber rating.
# Both the oxygen generator rating and the CO2 scrubber rating are values that can
# be found in your diagnostic report - finding them is the tricky part.
# Both values are located using a similar process that involves filtering out values
# until only one remains.
# Before searching for either rating value,
# start with the full list of binary numbers from your diagnostic report and
# consider just the first bit of those numbers.
# Then:
# Keep only numbers selected by the bit criteria for the type of rating value for which
# you are searching. Discard numbers which do not match the bit criteria.
# If you only have one number left, stop;
# this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:
#     To find oxygen generator rating, determine the most common value (0 or 1)
#     in the current bit position, and keep only numbers with that bit in that position.
#     If 0 and 1 are equally common, keep values with a 1 in the position.
#     To find CO2 scrubber rating, determine the least common value (0 or 1)
#     in the current bit position, and keep only numbers with that bit in that position.
#     If 0 and 1 are equally common, keep values with a 0 in the position.


def get_life_support_rating(report):
    num_length = len(report[0])
    bin_oxygen_rating, bin_co2_rating = report, report

    # print(bin_oxygen_rating, bin_co2_rating)

    for x in range(num_length):
        if len(bin_oxygen_rating) == 1:
            break

        x_elems = [num[x] for num in bin_oxygen_rating]
        count_0 = x_elems.count('0')
        count_1 = x_elems.count('1')
        # print("0 count:", count_0, "1 count:", count_1)

        if count_0 > count_1:
            bin_oxygen_rating = [i for i in bin_oxygen_rating if i[x] == '0']
        else:
            bin_oxygen_rating = [i for i in bin_oxygen_rating if i[x] == '1']

        # print(bin_oxygen_rating)

    for y in range(num_length):
        if len(bin_co2_rating) == 1:
            break

        y_elems = [num[y] for num in bin_co2_rating]
        count_0 = y_elems.count('0')
        count_1 = y_elems.count('1')
        # print("0 count:", count_0, "1 count:", count_1)

        if count_0 > count_1:
            bin_co2_rating = [i for i in bin_co2_rating if i[y] == '1']
        else:
            bin_co2_rating = [i for i in bin_co2_rating if i[y] == '0']

        # print(bin_co2_rating)

    # print(bin_oxygen_rating, bin_co2_rating)

    oxygen_rating = int(bin_oxygen_rating[0], 2)
    co2_rating = int(bin_co2_rating[0], 2)
    return oxygen_rating * co2_rating


if __name__ == "__main__":
    diag_report = []
    for line in fileinput.input("input.txt"):
        diag_report.append(line.strip())

    life_support_rating = get_life_support_rating(diag_report)
    print("Life support rating of submarine:", life_support_rating)
