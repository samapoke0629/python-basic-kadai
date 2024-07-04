import random

# リストの作成
array = [
    "月曜日は晴れです",
    "火曜日は雨です",
    "水曜日は晴れです",
    "木曜日は晴れです",
    "金曜日は曇りです",
    "土曜日は曇りのち雨です",
    "日曜日は雷雨です"
]

# ディクショナリの作成
dictionary = {
    "mon": "晴れ",
    "tue": "雨",
    "wed": "晴れ",
    "thu": "晴れ",
    "fri": "曇り",
    "sat": "曇りのち雨",
    "sun": "雷雨"
}

# リストからランダムに要素を取り出す
random_element_from_array = random.choice(array)
print("リストからのランダムな要素:", random_element_from_array)

# ディクショナリからランダムにキーを選び、その値を取り出す
random_key = random.choice(list(dictionary.keys()))
random_value_from_dictionary = dictionary[random_key]
print("ディクショナリからのランダムな要素:", random_key, random_value_from_dictionary)