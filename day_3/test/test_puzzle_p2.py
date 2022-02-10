import fileinput

from day_3.puzzle_p2 import get_life_support_rating


def test_life_support_rating(report):
    assert get_life_support_rating(report) == 230, \
        f"{get_life_support_rating(report)} does not equal 230"


if __name__ == "__main__":
    sample_report = []
    for line in fileinput.input("sample_input.txt"):
        sample_report.append(line.strip())

    test_life_support_rating(sample_report)
    print("Test Life Support Rating Passed!")
