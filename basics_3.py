"""
NumPy Foundations: Vectorized Arithmetic & Element-wise Operations
-------------------------------------------------------------------
Demonstrating scalar broadcasting, vectorized mathematical operations,
universal functions (ufuncs) like sqrt, rounding routines, and 
constant-based vector calculations (area of circles with np.pi).
"""

import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Initialize 1D Array
    # ---------------------------------------------------------
    array = np.array([1, 2, 3])

    print("--- Original Array ---")
    print(array)

    # ---------------------------------------------------------
    # 2. Basic Vectorized Arithmetic (Scalar Broadcasting)
    # ---------------------------------------------------------
    print("\n--- Basic Arithmetic ---")
    print("Array + 1 :", array + 1)
    print("Array - 2 :", array - 2)
    print("Array * 2 :", array * 2)
    print("Array / 2 :", array / 2)
    print("Array ** 2:", array**2)

    # ---------------------------------------------------------
    # 3. Vectorized Math & Rounding Functions (ufuncs)
    # ---------------------------------------------------------
    sqrt_array = np.sqrt(array)

    print("\n--- Universal Functions & Rounding ---")
    print("Square Root         :", sqrt_array)
    print("Rounded (np.round)  :", np.round(sqrt_array))
    print("Ceiling (np.ceil)   :", np.ceil(sqrt_array))
    print("Floor (np.floor)    :", np.floor(sqrt_array))

    # ---------------------------------------------------------
    # 4. Math Constants & Vectorized Formula (Area = π * r²)
    # ---------------------------------------------------------
    circle_areas = np.pi * np.square(array)

    print("\n--- Circle Areas (r = [1, 2, 3]) ---")
    print("π * r² :", circle_areas)


if __name__ == "__main__":
    main()
