"""
NumPy Foundations: 2D Broadcasting & Outer Products
---------------------------------------------------
Demonstrating shape expansion rules during broadcasting:
1. Row vector (1, 4) * Column vector (4, 1) -> (4, 4) Matrix
2. Column vector (10, 1) * 1D Array (10,) -> (10, 10) Multiplication Table
"""

import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Row Vector (1, 4) and Column Vector (4, 1)
    # ---------------------------------------------------------
    array_1 = np.array([[1, 2, 3, 4]])  # Shape: (1, 4)
    array_2 = np.array([[5], [6], [7], [8]])  # Shape: (4, 1)

    print("--- Shapes ---")
    print("Array 1 Shape:", array_1.shape)
    print("Array 2 Shape:", array_2.shape)

    # Broadcasting expands both arrays to (4, 4) and computes element-wise product
    product_2d = array_1 * array_2

    print("\n--- Broadcasted Result (4x4 Outer Product) ---")
    print(product_2d)
    print("Result Shape:", product_2d.shape)

    # ---------------------------------------------------------
    # 2. Creating a 10x10 Multiplication Table via Broadcasting
    # ---------------------------------------------------------
    col_vector = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9],
                           [10]])  # Shape: (10, 1)
    row_vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Shape: (10,)

    # Shape (10, 1) * Shape (10,) broadcasts to (10, 10)
    multiplication_table = col_vector * row_vector

    print("\n--- 10x10 Multiplication Table ---")
    print(multiplication_table)


if __name__ == "__main__":
    main()
