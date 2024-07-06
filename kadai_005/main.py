# 台形の面積を計算する関数
def calculate_trapezoid_area(top, bottom, height):
    # 台形の面積の公式を使用
    area = (top + bottom) * height / 2
    return area

# 変数に値を設定
top_side = 10  # 上辺
bottom_side = 20  # 下辺
height = 5  # 高さ

# 面積を計算
area = calculate_trapezoid_area(top_side, bottom_side, height)

# 結果を表示
print(f"台形の面積: {area} cm²")