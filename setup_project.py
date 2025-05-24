import os

# Define project structure
project_name = "SparseMatrixAssignment"
directories = [
    f"{project_name}/code/src",            # Source code directory
    f"{project_name}/sample_inputs"        # Sample input files directory
]
files = [
    f"{project_name}/code/src/sparse_matrix.py",   # Main class implementation
    f"{project_name}/code/src/main.py",           # Execution file
    f"{project_name}/sample_inputs/matrix1.txt",  # Sample matrix input
    f"{project_name}/sample_inputs/matrix2.txt",  # Sample matrix input
    f"{project_name}/.gitignore"                  # Git settings
]

def create_structure():
    """Creates the project directory structure and initializes necessary files."""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    for file in files:
        # Ensure README.md is not overwritten
        if "README.md" not in file:
            with open(file, "w") as f:
                if file.endswith(".gitignore"):
                    f.write("# Ignore unnecessary files\n")

    print("Project structure has been successfully created!")

if __name__ == "__main__":
    create_structure()
