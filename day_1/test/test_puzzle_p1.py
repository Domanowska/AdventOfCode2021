import fileinput

from day_1.puzzle_p1 import count_increases


def test_count():
    sonar_input = []
    for line in fileinput.input("sample_input.txt"):
        sonar_input.append(int(line))
    assert count_increases(sonar_input) == 7, "The number of increases should be 7"


if __name__ == "__main__":
    test_count()
    print("Test count passed!")
