"""
NumPy Foundations: Statistical Aggregations & Axis Operations
-------------------------------------------------------------
Demonstrating global reduction operations (sum, mean, std, var, min, max),
index location of extremes (argmin, argmax), and directional axis-wise aggregations.
"""

import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Initialize 2x4 Array
    # ---------------------------------------------------------
    # [[1, 2, 3, 4],
    #  [5, 6, 7, 8]]
    array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    print("--- Original 2x4 Array ---")
    print(array)

    # ---------------------------------------------------------
    # 2. Global Aggregations (Over Entire Array)
    # ---------------------------------------------------------
    print("\n--- Global Statistics ---")
    print("Sum               :", np.sum(array))
    print("Mean              :", np.mean(array))
    print("Standard Deviation:", np.std(array))
    print("Variance          :", np.var(array))
    print("Minimum Value     :", np.min(array))
    print("Maximum Value     :", np.max(array))

    # ---------------------------------------------------------
    # 3. Argmin & Argmax (Flattened Index Locations)
    # ---------------------------------------------------------
    print("\n--- Extreme Indices (Flattened) ---")
    print("Argmin (Index of Min Value):", np.argmin(array))
    print("Argmax (Index of Max Value):", np.argmax(array))

    # ---------------------------------------------------------
    # 4. Axis-Specific Aggregations
    # ---------------------------------------------------------
    print("\n--- Axis Operations ---")
    # axis=0: Collapse along rows -> operates vertically down columns
    print("Sum along Axis 0 (Columns sum) :", np.sum(array, axis=0))

    # axis=1: Collapse along columns -> operates horizontally across rows
    print("Sum along Axis 1 (Rows sum)    :", np.sum(array, axis=1))


if __name__ == "__main__":
    main()
