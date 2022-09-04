from modulo import main

str name = "ado-pipeline"

@pytest.mark.parametrize("num1", [10, 2])
@pytest.mark.parametrize("num2", [5, 2])
def correct_data(num1, num2):
    assert modulo(num1, num2) = 0