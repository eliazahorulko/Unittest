import unittest

# Функция для пошуку мінімального елементу масиву
def find_min_element(arr):
    if not arr:
        raise ValueError("Масив не може бути порожнім")
    return min(arr)

# Функція для розрахунку суми від'ємних елементів
def sum_of_negative_elements(arr):
    negative_elements = [x for x in arr if x < 0]
    return sum(negative_elements)

# Функція для розрахунку N-го елементу послідовності Фібоначчі
def fibonacci(n):
    if n <= 0:
        raise ValueError("N має бути позитивним числом")
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b if n > 1 else a

# Функція для розрахунку сили струму на ділянці кола
def current_in_circuit(voltage, resistance):
    if resistance == 0:
        raise ValueError("Опір не може бути нульовим")
    return voltage / resistance


# Клас для тестування функцій
class TestAlgorithms(unittest.TestCase):

    def test_find_min_element(self):
        self.assertEqual(find_min_element([3, 2, 1, 4]), 1)
        self.assertRaises(ValueError, find_min_element, [])

    def test_sum_of_negative_elements(self):
        self.assertEqual(sum_of_negative_elements([-1, -2, 3, 4]), -3)
        self.assertEqual(sum_of_negative_elements([1, 2, 3]), 0)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        self.assertRaises(ValueError, fibonacci, 0)

    def test_current_in_circuit(self):
        self.assertEqual(current_in_circuit(10, 2), 5)
        self.assertRaises(ValueError, current_in_circuit, 10, 0)


if __name__ == "__main__":
    unittest.main()
