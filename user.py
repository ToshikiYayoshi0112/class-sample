class User:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


if __name__ == "__main__":
    bob = User("Bob", 15, "USA")  # Userクラスをインスタンス化
    print(bob)  # <__main__.User object at 0x10a3438d0>
    print(bob.name)  # Bob
    print(bob.age)
    print(bob.country)

    tom = User("Tom", 57, "USA")
    print(tom)
    print(tom.name)
    print(tom.age)
    print(tom.country)

    ken = User("Ken", 49, "JP")
    print(ken)
    print(ken.name)
    print(ken.age)
    print(ken.country)
