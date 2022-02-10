import fileinput

from day_1.sonar_sweep_p2 import sum_increases


def test_sum_count():
    sonar_input = []
    for line in fileinput.input("day_1/test/sample_input.txt"):
        sonar_input.append(int(line))
    assert sum_increases(sonar_input) == 5, "The number of sum increases should be 5"
