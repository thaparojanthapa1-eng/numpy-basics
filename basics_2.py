"""
NumPy Foundations: 2D Array Slicing & Strides
----------------------------------------------
Demonstrating row/column slicing using start:stop:step notation, full-axis
selection (:), and multi-dimensional subarray extraction.
"""

import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Initialize 4x4 Matrix
    # ---------------------------------------------------------
    # [[ 1,  2,  3,  4],
    #  [ 5,  6,  7,  8],
    #  [ 9, 10, 11, 12],
    #  [13, 14, 15, 16]]
    matrix = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    )

    print("--- Original 4x4 Matrix ---")
    print(matrix)

    # ---------------------------------------------------------
    # 2. Row Slicing with Strides
    # ---------------------------------------------------------
    print("\n--- Every 2nd row (Rows 0 and 2) ---")
    print(matrix[0:4:2])

    # ---------------------------------------------------------
    # 3. Column Slicing & Extraction
    # ---------------------------------------------------------
    print("\n--- First Column (All rows, Column 0 as 1D vector) ---")
    print(matrix[:, 0])

    print("\n--- First 3 Columns (All rows, Columns 0 to 2) ---")
    print(matrix[:, :3])

    print("\n--- Every 2nd Column up to Column 3 (Columns 0 and 2) ---")
    print(matrix[:, :3:2])

    # ---------------------------------------------------------
    # 4. Sub-block Slicing
    # ---------------------------------------------------------
    print("\n--- First 2 Rows (All columns) ---")
    print(matrix[:2, :])

    print("\n--- Row 0 only (using step of 2 up to index 1) ---")
    print(matrix[:1:2, :])

    print("\n--- Top-Left 2x2 Sub-matrix ---")
    print(matrix[:2, :2])


if __name__ == "__main__":
    main()
