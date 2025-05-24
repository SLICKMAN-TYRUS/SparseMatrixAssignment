class SparseMatrix:
    """Represents a sparse matrix using a dictionary to store nonzero values."""

    def __init__(self, rows, cols):
        """Initialize an empty sparse matrix with specified dimensions."""
        self.rows = rows
        self.cols = cols
        self.values = {}  # Dictionary to store nonzero values {(row, col): value}

    @classmethod
    def from_file(cls, file_path):
        """Manually parse a sparse matrix from a file without using regex."""
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]  # Ignore empty lines

            # Validate format
            if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
                raise ValueError("Input file has wrong format")

            rows = int(lines[0].split('=')[1])
            cols = int(lines[1].split('=')[1])
            matrix = cls(rows, cols)

            for line in lines[2:]:
                # Manually extract row, col, and value
                try:
                    raw_values = line.strip("()").split(',')
                    row, col, value = map(int, raw_values)
                    matrix.set_element(row, col, value)
                except ValueError:
                    raise ValueError("Input file has wrong format")

            return matrix
        except Exception as e:
            print(f"Error loading matrix: {e}")
            return None

    def get_element(self, row, col):
        """Retrieve the value at a specific row and column."""
        return self.values.get((row, col), 0)

    def set_element(self, row, col, value):
        """Update the matrix with a new value or remove zero values."""
        if value != 0:
            self.values[(row, col)] = value
        elif (row, col) in self.values:
            del self.values[(row, col)]  # Remove zero entries to optimize memory

    def add(self, other):
        """Add two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result = SparseMatrix(self.rows, self.cols)

        for (row, col), value in self.values.items():
            result.set_element(row, col, value)

        for (row, col), value in other.values.items():
            result.set_element(row, col, result.get_element(row, col) + value)

        return result

    def subtract(self, other):
        """Subtract two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        result = SparseMatrix(self.rows, self.cols)

        for (row, col), value in self.values.items():
            result.set_element(row, col, value)

        for (row, col), value in other.values.items():
            result.set_element(row, col, result.get_element(row, col) - value)

        return result

    def multiply(self, other):
        """Optimized multiplication method for sparse matrices."""
        if self.cols != other.rows:
            raise ValueError("Matrix multiplication is not possible. A.cols must equal B.rows.")

        result = SparseMatrix(self.rows, other.cols)

        for (row_a, col_a), value_a in self.values.items():
            for row_b in range(other.rows):
                if (col_a, row_b) in other.values:
                    value_b = other.get_element(col_a, row_b)
                    result.set_element(row_a, row_b, result.get_element(row_a, row_b) + (value_a * value_b))

        return result
