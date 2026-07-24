"""
NumPy Foundations: Boolean Masking & Conditional Selection
----------------------------------------------------------
Demonstrating element filtering with boolean logic (&), 
1D extraction via boolean indexing, and conditional array 
transformation using np.where().
"""

import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Initialize Array
    # ---------------------------------------------------------
    ages = np.array([[10, 12, 14, 16, 18], [11, 13, 15, 17, 19]])

    print("--- Original Ages Array (2x5) ---")
    print(ages)

    # ---------------------------------------------------------
    # 2. Boolean Indexing (Extracting Subsets as 1D Arrays)
    # ---------------------------------------------------------
    # Filter ages strictly less than 15
    early_teens = ages[ages < 15]
    print("\n--- Early Teens (Age < 15) ---")
    print(early_teens)

    # Compound boolean condition using & (15 <= Age < 18)
    late_teens = ages[(ages >= 15) & (ages < 18)]
    print("\n--- Late Teens (15 <= Age < 18) ---")
    print(late_teens)

    # Filter ages greater than or equal to 18
    adults = ages[ages >= 18]
    print("\n--- Adults (Age >= 18) ---")
    print(adults)

    # Filter multiples of 5 using modulo operator (%)
    mult_v = ages[ages % 5 == 0]
    print("\n--- Multiples of 5 ---")
    print(mult_v)

    # ---------------------------------------------------------
    # 3. Conditional Transformation with np.where()
    # ---------------------------------------------------------
    # Preserve array shape while replacing non-multiples of 3 with "NA"
    mult_iii = np.where(ages % 3 == 0, ages, "NA")
    print("\n--- Multiples of 3 (np.where conditional output) ---")
    print(mult_iii)


if __name__ == "__main__":
    main()
