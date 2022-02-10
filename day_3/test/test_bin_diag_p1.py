import fileinput
from typing import List

from day_3.bin_diag_p1 import get_power_consumption


def test_power_consumption():
    sample_report = []
    for line in fileinput.input("day_3/test/sample_input.txt"):
        sample_report.append(line.strip())
    assert get_power_consumption(sample_report) == 198
