class User:
    def __init__(self, name, age, country):
        # インスタンス変数 self.name, self.age, self.countryのこと
        self.name = name
        self.age = age
        self.country = country


if __name__ == "__main__":
    bob = User("Bob", 15, "USA")  # Userクラスをインスタンス化

    tom = User("Tom", 57, "USA")

    ken = User("Ken", 49, "JP")
