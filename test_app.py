def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def porcentaje(total, porcentaje):
    return (total * porcentaje) / 100



def test_porcentaje():
    assert porcentaje(100, 20) == 20
    assert porcentaje(50, 50) == 25
    assert porcentaje(200, 10) == 20
    assert porcentaje(0, 100) == 0
def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0.3, 0.7) == 1



def test_resta():
    assert resta(5, 2) == 3
    assert resta(1, 1) == 1