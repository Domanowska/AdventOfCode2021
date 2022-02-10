import fileinput

from day_3.puzzle_p1 import get_power_consumption


def test_power_consumption(report):
    assert get_power_consumption(report) == 198, \
        f"{get_power_consumption(report)} does not equal 198"


if __name__ == "__main__":
    sample_report = []
    for line in fileinput.input("sample_input.txt"):
        sample_report.append(line.strip())

    test_power_consumption(sample_report)
    print("Test power consumption passed!")
