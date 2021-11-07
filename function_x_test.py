import pytest

import function_x


def test_x_negative_one():
    assert function_x.calculator(-1) == 0.0078125


def test_x_negative_two():
    assert function_x.calculator(-2) == -4


def test_x_positive_eight():
    assert function_x.calculator(8) == 0.0078125


def test_x_negative_eleven():
    assert function_x.calculator(-11) == 0.0078125


def test_x_negative_ten():
    assert function_x.calculator(-10) == -100


def test_x_positive_thirty_five():
    assert function_x.calculator(35) == 23


def test_x_positive_forty_five():
    assert function_x.calculator(45) == 0.0078125


def test_x_negative_thirteen():
    assert function_x.calculator(-13) == 0.0078125


def test_x_positive_sixty():
    assert function_x.calculator(60) == 0.0078125


def test_x_zero():
    assert function_x.calculator(0) == 1


def test_x_float_number():
    assert function_x.calculator(-1.456) == -5.385964912280702


def test_x_not_valid_special_character():
    with pytest.raises(TypeError):
        function_x.calculator("!@#$%$#$%")
    assert 'TypeError'


def test_x_not_valid_letters():
    with pytest.raises(TypeError):
        function_x.calculator("irdeto")
    assert 'TypeError'
