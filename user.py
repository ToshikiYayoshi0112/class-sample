class User:
    def __init__(self, name, age, country):
        # インスタンス変数 self.name, self.age, self.countryのこと
        self.name = name
        self.age = age
        self.country = country

    def display_profile(self):
        # display_profile()は、Userクラスのインスタンスメソッド
        print(f"{self.name}国籍: {self.country} {self.age}歳です。")

    def chenge_nationality(self, country_name):
        self.country = country_name


if __name__ == "__main__":
    bob = User("Bob", 15, "USA")  # Userクラスをインスタンス化
    bob.chenge_nationality("Chine")
    bob.display_profile()

    tom = User("Tom", 57, "USA")
    tom.chenge_nationality("Australia")
    tom.display_profile()

    ken = User("Ken", 49, "JP")
    ken.chenge_nationality("Korea")
    ken.display_profile()
