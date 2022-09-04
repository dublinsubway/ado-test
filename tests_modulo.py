import pytest
from modulo import modulo

name = str("ado-pipeline")

@pytest.mark.parametrize("numbers", [
[10, 5],
[2, 2]
])
def test_correct_data(numbers):
    assert modulo(numbers[0], numbers[1]) == 0