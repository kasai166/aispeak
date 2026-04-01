import MeCab
import pandas as pd
from collections import Counter
import re
# テキストデータを形態素解析する関数
def mecab_analysis(text):
    m = MeCab.Tagger("-Owakati")
    return m.parse(text)
# 単語の出現頻度をカウントする関数
def count_words(text):
    words = text.split()
    return Counter(words)
# 感情分類を行う関数
def classify_emotion(text):
    positive_words = ["良い", "嬉しい", "楽しい"]
    negative_words = ["悪い", "悲しい", "つらい"]
    word_count = count_words(text)
    positive_score = sum(word_count[word] for word in positive_words)
    negative_score = sum(word_count[word] for word in negative_words)
    if positive_score > negative_score:
        return "Positive"
    elif positive_score < negative_score:
        return "Negative"
    else:
        return "Neutral"
# テキストデータを読み込む
def emo():
    text_data = 'おはようございます'
    text_data=re.sub('　', '',text_data)
    print(text_data)
    # 感情分析を行う
    for text in text_data:
        analyzed_text = mecab_analysis(text)
        emotion = classify_emotion(analyzed_text)
        print(text, ":", emotion)