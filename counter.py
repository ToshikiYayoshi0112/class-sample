class Counter:
    def __init__(self, value):
        self.value = value

    def increase(self):
        self.value += 1


if __name__ == "__main__":
    counter_1 = Counter(0)
    print(counter_1.value)  # 0が出力される

    counter_1.increase()
    print(counter_1.value)  # 1が出力される

    counter_1.increase()
    print(counter_1.value)  # 2が出力される

    counter_2 = Counter(15)
    print(counter_2.value)  # 15が出力される

    counter_2.increase()
    print(counter_2.value)  # 16が出力される

    counter_2.increase()
    print(counter_2.value)  # 17が出力される
