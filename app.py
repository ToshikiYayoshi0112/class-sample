from counter import Counter

if __name__ == "__main__":
    start_num = int(input("初期値は? > "))
    step = int(input("どんくらいの間隔でいく? > "))
    counter = Counter(start_num, step)

    comand = input("実行する?(するなら:y, やめるなら:q) > ")

    while comand != "q":
        if comand == "y":
            counter.increase()
            print("加算しちゃうね!")
            print(counter.value)

        else:
            print("ちゃんとしたコマンドをおしてね!")

        comand = input("まだ加算するでしょ?(続けるなら:y, やめるなら:q) > ")

    print("やめちゃうのね!")
