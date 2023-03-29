from .. import convert_precision

def test_cp():
    assert convert_precision('0.000001') == 6, "Заданная точность должна быть 6"