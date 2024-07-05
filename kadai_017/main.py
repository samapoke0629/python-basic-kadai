class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です。")
        else:
            print(f"{self.name}は大人ではありません。")

# Humanクラスのインスタンスを生成してリストに追加
humans = [
    Human("田中", 22),
    Human("佐藤", 18),
    Human("鈴木", 30)
]

# リストの要素数分だけcheck_adultメソッドを呼び出す
for human in humans:
    human.check_adult()