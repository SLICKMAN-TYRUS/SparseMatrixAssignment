from sparse_matrix import SparseMatrix

def print_matrix(matrix, operation_name):
    """Print matrix summary instead of full rows for cleaner output."""
    print(f"\n{operation_name} Result: {matrix.rows} x {matrix.cols}")
    print("Sample elements:")
    
    # Selecting key sample positions to display
    sample_positions = [(0, 1), (2, 2), (4, 4)]
    for row, col in sample_positions:
        print(f"({row}, {col}): {matrix.get_element(row, col)}")

# Load matrices from files
matrix1 = SparseMatrix.from_file("../../sample_inputs/matrix1.txt")
matrix2 = SparseMatrix.from_file("../../sample_inputs/matrix2.txt")

if matrix1 and matrix2:
    print(f"Matrix 1 Loaded: {matrix1.rows} x {matrix1.cols}")
    print(f"Matrix 2 Loaded: {matrix2.rows} x {matrix2.cols}")

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            sum_matrix = matrix1.add(matrix2)
            print_matrix(sum_matrix, "Addition")
        elif choice == "2":
            diff_matrix = matrix1.subtract(matrix2)
            print_matrix(diff_matrix, "Subtraction")
        elif choice == "3":
            if matrix1.cols == matrix2.rows:
                product_matrix = matrix1.multiply(matrix2)
                print_matrix(product_matrix, "Multiplication")
            else:
                print("\nMatrix multiplication is not possible. A.cols must equal B.rows.")
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

else:
    print("Failed to load matrices. Check the file format or path.")
