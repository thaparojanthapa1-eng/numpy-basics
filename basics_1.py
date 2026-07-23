"""
NumPy Foundations: Array Creation, Dimensions, Shapes, and Multi-Dimensional Indexing
-------------------------------------------------------------------------------------
Demonstrating NumPy versioning, scalar vs. N-dimensional arrays (.ndim),
array shapes (.shape), multi-dimensional indexing syntax, and element extraction.
"""

import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. NumPy Version Check
    # ---------------------------------------------------------
    print(f"NumPy Version: {np.__version__}")

    # ---------------------------------------------------------
    # 2. Dimensions (.ndim) - 0D to 3D Arrays
    # ---------------------------------------------------------
    # 1D Array (Vector)
    arr_1d = np.array([1, 2, 3, 4])
    print("\n--- 1D Array ---")
    print(arr_1d)
    print("Dimensions:", arr_1d.ndim)

    # 0D Array (Scalar)
    arr_0d = np.array("A")
    print("\n--- 0D Array (Scalar) ---")
    print("Dimensions:", arr_0d.ndim)

    # 2D Array (Matrix)
    arr_2d = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
    print("\n--- 2D Array ---")
    print("Dimensions:", arr_2d.ndim)

    # 3D Array (Tensor)
    arr_3d = np.array(
        [
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
        ]
    )
    print("\n--- 3D Array ---")
    print("Dimensions:", arr_3d.ndim)
    print("Shape:", arr_3d.shape)

    # ---------------------------------------------------------
    # 3. Multi-Dimensional Indexing
    # ---------------------------------------------------------
    print("\n--- Element Access ---")
    # Python list style indexing vs. native NumPy tuple indexing
    print("arr_3d[0][0][0] :", arr_3d[0][0][0])
    print("arr_3d[0, 0, 0] :", arr_3d[0, 0, 0])  # Preferred NumPy syntax

    # Concatenating values extracted from array
    one_two = str(arr_3d[0, 0, 0]) + str(arr_3d[1, 1, 1])
    print("Concatenated elements string:", one_two)


if __name__ == "__main__":
    main()
