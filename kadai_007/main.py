import random  # random モジュールをインポート

# 一週間の天気予報をリストで管理
array = [
    "月曜日は晴れです",  # 月曜日の天気
    "火曜日は雨です",    # 火曜日の天気
    "水曜日は晴れです",  # 水曜日の天気
    "木曜日は晴れです",  # 木曜日の天気
    "金曜日は曇りです",  # 金曜日の天気
    "土曜日は曇りのち雨です",  # 土曜日の天気
    "日曜日は雷雨です"   # 日曜日の天気
]

# 曜日ごとの天気をディクショナリで管理
dictionary = {
    "mon": "晴れ",  # 月曜日の天気
    "tue": "雨",    # 火曜日の天気
    "wed": "晴れ",  # 水曜日の天気
    "thu": "晴れ",  # 木曜日の天気
    "fri": "曇り",  # 金曜日の天気
    "sat": "曇りのち雨",  # 土曜日の天気
    "sun": "雷雨"   # 日曜日の天気
}

# リストからランダムに天気を選択し出力
random_element_from_array = random.choice(array)  # ランダムに選択
print("リストからのランダムな要素:", random_element_from_array)  # 出力

# ディクショナリからランダムに曜日を選び、対応する天気を出力
random_key = random.choice(list(dictionary.keys()))  # ランダムにキーを選択
random_value_from_dictionary = dictionary[random_key]  # キーに対応する値を取得
print("ディクショナリからのランダムな要素:", random_key, random_value_from_dictionary)  # 出力
