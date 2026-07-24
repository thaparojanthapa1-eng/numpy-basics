"""
NumPy Foundations: Random Number Generation & Sampling
------------------------------------------------------
Demonstrating modern Generator usage (np.random.default_rng) for:
1. Integer generation (rng.integers)
2. Continuous uniform distribution (rng.uniform)
3. In-place array shuffling (rng.shuffle)
4. Random selection and multi-dimensional sampling (rng.choice)
"""

import numpy as np


def main() -> None:
    # Instantiate modern, high-performance PCG64 random generator
    rng = np.random.default_rng()

    # ---------------------------------------------------------
    # 1. Discrete Integer Sampling (e.g., Rolling 6-sided dice)
    # ---------------------------------------------------------
    # Generates integers from low (1) up to high-1 (6), shaped (6, 6)
    dice_rolls = rng.integers(1, 7, size=(6, 6))

    print("--- 6x6 Dice Rolls (1 to 6) ---")
    print(dice_rolls)

    # ---------------------------------------------------------
    # 2. Continuous Uniform Sampling
    # ---------------------------------------------------------
    # Floating-point values uniformly distributed over [1.0, 6.0)
    uniform_matrix = rng.uniform(1.0, 6.0, size=(3, 2))

    print("\n--- 3x2 Uniform Floating-Point Matrix ---")
    print(uniform_matrix)

    # ---------------------------------------------------------
    # 3. In-Place Shuffling
    # ---------------------------------------------------------
    # Shuffling NumPy array
    num_array = np.array([1, 2, 3, 4, 5, 6])
    rng.shuffle(num_array)

    print("\n--- Shuffled NumPy Array ---")
    print(num_array)

    # Shuffling standard Python list
    fruits = ["apple", "banana", "mango", "guava", "pineapple"]
    rng.shuffle(fruits)

    print("\n--- Shuffled List of Fruits ---")
    print(fruits)

    # ---------------------------------------------------------
    # 4. Random Sampling from Sequence
    # ---------------------------------------------------------
    # Draws random elements with replacement into a 3x2 grid
    selected_fruits = rng.choice(fruits, size=(3, 2))

    print("\n--- 3x2 Matrix Sampled from Fruits ---")
    print(selected_fruits)


if __name__ == "__main__":
    main()
