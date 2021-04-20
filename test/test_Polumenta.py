import pytest
from polumenta.generator import jedanPolumenta, Polumente, rodiPolumentu

def test_jedanPolumenta_works():	
	pol = jedanPolumenta()
	assert(pol != '')

def test_jedanPolumenta_returnsAtLeast4Chars():	
	pol = jedanPolumenta()
	assert(len(pol) > 3)

def test_jedanPolumenta_returnsOneName():	
	pol = jedanPolumenta()
	assert(len(pol.split()) == 1)

def test_Polumente_low():
	poli = Polumente(-20)
	assert(len(poli) == 1)

def test_Polumente_high():
	with pytest.raises(ValueError):
		poli = Polumente(200)

def test_Polumente_num():
	poli = Polumente(20)
	assert(len(poli) == 20)
