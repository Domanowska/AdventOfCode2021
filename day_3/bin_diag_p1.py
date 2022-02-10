import fileinput

# --- Day 3: Binary Diagnostic ---
# The submarine has been making some odd creaking noises, so you ask it to
# produce a diagnostic report just in case.
# The diagnostic report consists of a list of binary numbers which,
# when decoded properly, can tell you many useful things about the conditions
# of the submarine.
# The first parameter to check is the power consumption.
# You need to use the binary numbers in the diagnostic report to generate
# two new binary numbers (called the gamma rate and the epsilon rate).
# The power consumption can then be found by multiplying the gamma rate by
# the epsilon rate.
# Each bit in the gamma rate can be determined by finding the most common bit
# in the corresponding position of all numbers in the diagnostic report.


def get_power_consumption(report):
    num_length = len(report[0])
    gamma, epsilon = [], []

    for x in range(num_length):
        count_0, count_1 = 0, 0
        for num in report:
            if num[x] == '0':
                count_0 += 1
            elif num[x] == '1':
                count_1 += 1

        if count_0 > count_1:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)

    gamma_rate = int(''.join(str(i) for i in gamma), 2)
    epsilon_rate = int(''.join(str(i) for i in epsilon), 2)

    return gamma_rate * epsilon_rate


if __name__ == "__main__":
    diag_report = []
    for line in fileinput.input("input.txt"):
        diag_report.append(line.strip())

    power_consumption = get_power_consumption(diag_report)
    print("Power consumption of submarine:", power_consumption)
