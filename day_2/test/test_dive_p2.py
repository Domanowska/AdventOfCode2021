import fileinput

from day_2.dive_p2 import get_improved_position


_expected_position = {
    'latitude': 15,
    'depth': 60
}


def test_position():
    instructions = []
    for line in fileinput.input("day_2/test/sample_input.txt"):
        instructions.append(line)
    assert get_improved_position(instructions) == _expected_position, \
        f"{get_improved_position(instructions)} does not equal {_expected_position}"
