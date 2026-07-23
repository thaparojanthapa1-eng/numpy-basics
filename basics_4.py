"""
NumPy Foundations: Element-wise Operations & Boolean Mask Assignment
---------------------------------------------------------------------
Demonstrating element-wise arithmetic between arrays, boolean comparisons,
and conditional element mutation using boolean indexing.
"""

import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Initialize Arrays
    # ---------------------------------------------------------
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])

    print("Array 1:", array1)
    print("Array 2:", array2)

    # ---------------------------------------------------------
    # 2. Element-wise Vector Arithmetic
    # ---------------------------------------------------------
    print("\n--- Element-wise Arithmetic ---")
    print("Addition (array1 + array2)      :", array1 + array2)
    print("Multiplication (array1 * array2):", array1 * array2)
    print("Subtraction (array1 - array2)   :", array1 - array2)
    print("Division (array1 / array2)      :", array1 / array2)

    # ---------------------------------------------------------
    # 3. Boolean Comparison & Masking
    # ---------------------------------------------------------
    print("\n--- Boolean Comparison ---")
    print("Is element equal to 2? (array1 == 2):", array1 == 2)

    # ---------------------------------------------------------
    # 4. Conditional Value Assignment (In-Place Mutation)
    # ---------------------------------------------------------
    # Replace all elements in array1 that are less than 2 with 4
    array1[array1 < 2] = 4

    print("\n--- Array 1 After Mask Assignment (array1[array1 < 2] = 4) ---")
    print(array1)


if __name__ == "__main__":
    main()
