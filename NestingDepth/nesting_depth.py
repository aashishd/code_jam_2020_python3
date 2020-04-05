class NestingDepth:
    def __init__(self):
        raw_input = input()
        self.values = [int(raw_input[i]) for i in range(len(raw_input))]
        self.result = ""
        self.nested_string()

    def nested_string(self):
        # creates the string with nesting
        prev_num = 0
        for current_value in self.values:
            diff = current_value - prev_num
            paren = ")"
            if diff > 0:
                paren = "("
            parenthesis = "".join([paren for i in range(abs(diff))])
            self.result += parenthesis + str(current_value)
            prev_num = current_value
        self.result += "".join([")" for i in range(self.values[-1])])


def main():
    test_count = int(input())
    for t in range(1, test_count + 1):
        nested = NestingDepth()
        print("Case #{}: {}".format(t, nested.result))


if __name__ == "__main__":
    main()
