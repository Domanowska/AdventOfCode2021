import fileinput

from day_1.puzzle_p2 import sum_increases


def test_sum_count():
    sonar_input = []
    for line in fileinput.input("sample_input.txt"):
        sonar_input.append(int(line))
    assert sum_increases(sonar_input) == 5, "The number of sum increases should be 5"


if __name__ == "__main__":
    test_sum_count()
    print("Test sum passed!")
