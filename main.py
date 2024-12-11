# find_min_element.py
def find_min_element(arr):
    if not arr:
        raise ValueError("Масив не може бути порожнім")
    return min(arr)

# sum_of_negative_elements.py
def sum_of_negative_elements(arr):
    negative_elements = [x for x in arr if x < 0]
    return sum(negative_elements)

# fibonacci.py
def fibonacci(n):
    if n <= 0:
        raise ValueError("N має бути позитивним числом")
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b if n > 1 else a

# current_in_circuit.py
def current_in_circuit(voltage, resistance):
    if resistance == 0:
        raise ValueError("Опір не може бути нульовим")
    return voltage / resistance
