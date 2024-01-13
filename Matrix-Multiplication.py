import sys
import time


def load_matrix_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            rows, columns = map(int, lines[0].split())

            matrix = [[0] * columns for _ in range(rows)]

            for line in lines[1:]:
                i, j, value = map(int, line.split())
                matrix[i][j] = value

            return matrix
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading matrix from file '{file_name}': {e}")
        sys.exit(1)


def save_matrix_to_file(matrix, file_name):
    try:
        with open(file_name, 'w') as file:
            for row in matrix:
                file.write(' '.join(map(str, row)) + '\n')
    except Exception as e:
        print(f"Error saving matrix to file '{file_name}': {e}")
        sys.exit(1)


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:
        print(
            "Matrices must have the same dimensions")
        return None

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


def matrix_multiplication():
    if len(sys.argv) != 3:
        print("Please provide two file names containing matrices as arguments.")
        sys.exit(1)

    file_name_a = sys.argv[1]
    file_name_b = sys.argv[2]

    matrix_a = load_matrix_from_file(file_name_a)
    matrix_b = load_matrix_from_file(file_name_b)

    result = multiply_matrices(matrix_a, matrix_b)

    save_matrix_to_file(result, "Output.txt")

    with open("Output.txt", 'r') as output_file:
        for line in output_file:
            print(line.strip())


if __name__ == "__main__":
    t0 = time.time()
    matrix_multiplication()
    t1 = time.time()

    totalWithoutWrite = t1 - t0
    print("Time: " + str(totalWithoutWrite))
