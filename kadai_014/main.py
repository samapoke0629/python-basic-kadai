price1 = 100
price2 = 200
tax = 1.1  # taxをグローバル変数として定義

def total():
    return price1 + price2

print(total() * tax)  # taxが関数外でも使用可能