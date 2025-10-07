import math
import pytest
from app import calculator

def test_sqrt():
    assert calculator.sqrt(25) == 5
    with pytest.raises(ValueError):
        calculator.sqrt(-4)

def test_factorial():
    assert calculator.factorial(5) == 120
    assert calculator.factorial(0) == 1
    with pytest.raises(ValueError):
        calculator.factorial(-3)

def test_ln():
    assert math.isclose(calculator.ln(math.e), 1.0, rel_tol=1e-9)
    with pytest.raises(ValueError):
        calculator.ln(0)

def test_power():
    assert calculator.power(2, 3) == 8
