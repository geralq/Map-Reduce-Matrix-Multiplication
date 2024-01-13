from mrjob.job import MRJob
from mrjob.step import MRStep
import os
import time

counter = 0


class MatrixMultiplication(MRJob):
    result_file = open('Output.txt', 'w')

    def mapper(self, _, line):
        global counter
        line = line.split()
        line = list(map(int, line))
        if len(line) == 3:
            row, col, value = line
        elif len(line) == 2 and counter == 1:
            row, value = line
            col = 0
        elif len(line) == 2 and counter == 0:
            counter = 1
            return

        filename = os.environ['map-reduce-input-matrix']

        if 'A' in filename:
            yield col, (0, row, value)
        elif 'B' in filename:
            yield row, (1, col, value)

    def reducer_multiply(self, keys, values):
        matrix_a = []
        matrix_b = []

        for value in values:
            if value[0] == 0:
                matrix_a.append(value)
            elif value[0] == 1:
                matrix_b.append(value)

        for row_a, col_a, val_a in matrix_a:
            for row_b, col_b, val_b in matrix_b:
                yield (col_a, col_a), val_a * val_b

    def change_key(self, key, value):
        yield key, value

    def reducer_sum(self, key, values):
        total = sum(values)
        yield key, total
        x = key[0]
        y = key[1]
        self.result_file.write(str(x) + " " + str(y) + " ")
        self.result_file.write(str(total) + "\n")

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_multiply),
            MRStep(mapper=self.change_key,
                   reducer=self.reducer_sum)
        ]


if __name__ == '__main__':
    t0 = time.time()
    MatrixMultiplication.run()
    t1 = time.time()

    totalWithoutWrite = t1 - t0
    print("Time: " + str(totalWithoutWrite))
