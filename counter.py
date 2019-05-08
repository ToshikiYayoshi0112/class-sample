class Counter:
    def __init__(self, value, step):
        self.value = value
        self.step = step
    def increase(self):
        self.value += self.step

    # def increase3(self):
    #     self.value += 3
    #
    # def increase

if __name__ == "__main__":
    counter_1 = Counter(0, 1)
    print(counter_1.value)  # 0が出力される

    counter_1.increase()
    print(counter_1.value)  # 1が出力される

    counter_1.increase()
    print(counter_1.value)  # 2が出力される

    counter_2 = Counter(15, 3)
    print(counter_2.value)  # 15が出力される

    counter_2.increase()
    print(counter_2.value)  # 16が出力される

    counter_2.increase()
    print(counter_2.value)  # 17が出力される

    counter_3 = Counter(-5, 5)
    print(counter_3.value)
    counter_3.increase()
