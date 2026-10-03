import numpy as np

def nerdy_computation(x):
    """Returns the sum of the squares of the first x natural numbers using numpy."""
    getallen = np.arange(1, x + 1)
    return int(np.sum(getallen ** 2))

print("Hello MUDE! Let's compute something nerdy:")
result = nerdy_computation(10)
print(f"The sum of the squares of the first 10 natural numbers is {result}")