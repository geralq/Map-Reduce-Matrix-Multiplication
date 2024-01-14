import os
import random


def generate_matrices(n):

    file_a_name = 'matrixA.txt'
    file_b_name = 'matrixB.txt'

    if os.path.exists(file_a_name):
        os.remove(file_a_name)
    if os.path.exists(file_b_name):
        os.remove(file_b_name)

    matrix_a = []
    for i in range(n):
        for j in range(n):
            matrix_a.append((i, j, random.randint(0, 100)))

    # Matriz B
    matrix_b = []
    for i in range(n):
        for j in range(n):
            matrix_b.append((i, j, random.randint(0, 100)))

    with open(file_a_name, 'w') as file_a:
        file_a.write(f'{n} {n}\n')
        for item in matrix_a:
            file_a.write(' '.join(map(str, item)) + '\n')

    with open(file_b_name, 'w') as file_b:
        file_b.write(f'{n} {n}\n')
        for item in matrix_b:
            file_b.write(' '.join(map(str, item)) + '\n')


generate_matrices(3)