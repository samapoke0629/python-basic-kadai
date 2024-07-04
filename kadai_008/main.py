import random  # random モジュールをインポート

def fizz_buzz(var):
    if var % 3 == 0 and var % 5 == 0:
        print("FizzBuzz")
    elif var % 3 == 0:
        print("Fizz")
    elif var % 5 == 0:
        print("Buzz")
    else:
        print(var)

# ランダムな値で関数をテスト
for _ in range(5):  # 5回繰り返す
    random_var = random.randint(1, 100)  # 1から100の間でランダムな整数を生成
    print(f"Testing with: {random_var}")  # テストする値を表示
    fizz_buzz(random_var)  # 関数を呼び出し