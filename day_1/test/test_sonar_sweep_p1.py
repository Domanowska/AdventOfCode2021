import fileinput

from day_1.sonar_sweep_p1 import count_increases


def test_count():
    sonar_input = []
    for line in fileinput.input("day_1/test/sample_input.txt"):
        sonar_input.append(int(line))
    assert count_increases(sonar_input) == 7, "The number of increases should be 7"
