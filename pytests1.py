import pytest

# Импортируем функцию, которую нужно протестировать
from main import sozdaem_triangle

def test_generate_pascal_triangle():
    # Проверяем числа
    assert sozdaem_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    # Проверяем ввод отрицательного значения
    with pytest.raises(ValueError):
        sozdaem_triangle(-1)

    # Проверяем ввод значения 0
    assert sozdaem_triangle(0) == []

    # Проверка больших значений
    assert len(sozdaem_triangle(1000)) == 1000

    # Проверка числа
    with pytest.raises(TypeError):
        sozdaem_triangle(3.5)

    # Проверка ввода строки
    with pytest.raises(TypeError):
        sozdaem_triangle("abc")
