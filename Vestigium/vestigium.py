from copy import deepcopy


class Matrix:

    def __init__(self):
        self.elements = int(input())
        self.range = list(range(1, self.elements + 1))
        self.rows = []
        self.rep_rows = 0
        self.rep_cols = 0
        self.trace = 0
        self.build()
        self.process()

    def build(self):
        for count in range(self.elements):
            row = [int(val) for val in input().split(" ")]
            self.rows.append(row)

    def process(self):
        for i in range(self.elements):
            col_check = deepcopy(self.range)
            row_check = deepcopy(self.range)
            for j in range(self.elements):
                row_elem = self.rows[i][j]
                col_elem = self.rows[j][i]
                if row_elem in row_check:
                    row_check.remove(row_elem)
                if col_elem in col_check:
                    col_check.remove(col_elem)
                if i == j:
                    self.trace += self.rows[i][j]
            if len(row_check) != 0:
                self.rep_rows += 1
            if len(col_check) != 0:
                self.rep_cols += 1


def my_func():
    test_count = int(input())
    for t in range(1, test_count + 1):
        m1 = Matrix()
        print("Case #{}: {} {} {}".format(t, m1.trace, m1.rep_rows, m1.rep_cols))
        # print(f"Case #{t}: {m1.trace} {m1.rep_rows} {m1.rep_cols}")


if __name__ == "__main__":
    my_func()
