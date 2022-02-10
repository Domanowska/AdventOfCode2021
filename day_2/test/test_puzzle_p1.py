import fileinput

from day_2.puzzle_p1 import get_position


_expected_position = {
    'latitude': 15,
    'depth': 10
}


def test_position():
    instructions = []
    for line in fileinput.input("sample_input.txt"):
        instructions.append(line)
    assert get_position(instructions) == _expected_position, \
        f"{get_position(instructions)} does not equal {_expected_position}"


if __name__ == "__main__":
    test_position()
    print("Test position passed!")
