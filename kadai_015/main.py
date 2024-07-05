class Human:
    def __init__(self, name, age):
        """
        Humanクラスのコンストラクタ
        :param name: 人の名前
        :param age: 人の年齢
        """
        self.name = name
        self.age = age

    def printinfo(self):
        """
        インスタンスの名前と年齢を出力する
        """
        print(f"名前: {self.name}, 年齢: {self.age}")

# Humanクラスのインスタンスを作成し、使用する例
person = Human("山田太郎", 30)
person.printinfo()