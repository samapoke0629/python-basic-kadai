def calculate_total_price(price, tax_rate=0.10):
    """
    商品の金額と消費税率を受け取り、税込み価格を計算して返す関数

    Args:
    price (float): 商品の金額
    tax_rate (float): 消費税率（デフォルトは10%）

    Returns:
    float: 税込み価格

    Raises:
    ValueError: 価格または税率が負の値の場合
    TypeError: 価格または税率が数値でない場合
    """
    if not isinstance(price, (int, float)):
        raise TypeError("価格は数値である必要があります。")
    if not isinstance(tax_rate, (int, float)):
        raise TypeError("消費税率は数値である必要があります。")
    if price < 0:
        raise ValueError("価格は0以上である必要があります。")
    if tax_rate < 0:
        raise ValueError("消費税率は0以上である必要があります。")

    total_price = price * (1 + tax_rate)
    return total_price

# 関数をテスト
try:
    print(calculate_total_price(100))  # 100円の商品の税込み価格を計算
    print(calculate_total_price(100, 0.08))  # 100円の商品の税込み価格を計算（消費税率は8%）
    print(calculate_total_price(500, 0.10))  # 500円の商品の税込み価格を計算（消費税率は10%）
    print(calculate_total_price(-100))  # 不正な価格でエラーをテスト
except Exception as e:
    print(f"エラー: {e}")