import pytest
from fibonacci import fibonacci


def test_fibonacci_correcto():
    assert fibonacci(10) == 100


def test_fibonacci_limite():
    assert fibonacci(0) == 0


def test_fibonacci_negativo():
    with pytest.raises(ValueError):
        fibonacci(-5)


def test_fibonacci_tipo_incorrecto():
    with pytest.raises(TypeError):
        fibonacci("hola")


def test_fibonacci_uno():
    assert fibonacci(1) == 1
