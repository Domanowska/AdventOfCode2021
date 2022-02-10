import fileinput

from day_3.bin_diag_p2 import get_life_support_rating


def test_life_support_rating():
    sample_report = []
    for line in fileinput.input("day_3/test/sample_input.txt"):
        sample_report.append(line.strip())
    assert get_life_support_rating(sample_report) == 230
