from weatherAPI import getairportinfo
from weatherAPI import getweatherinfo
def test_getairportinfo():
    assert getairportinfo('Total Rf Heliport') == 'Bensalem'
    assert getairportinfo('Aero B Ranch Airport') == 'Leoti'

