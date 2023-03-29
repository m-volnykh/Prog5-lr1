from .. import sqrtDisp
from math import sqrt

def test_sd():
    assert sqrtDisp(1, 2, 3) == sqrt(2/3), "Неверное значение, правильное: sqrt(2/3)"
    assert sqrtDisp(1, 2, 3, 4, 5) == sqrt(2), "Неверное значение, правильное: sqrt(2)"