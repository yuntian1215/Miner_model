import spacy
from collections import Counter

# 加载spaCy的英文模型
nlp = spacy.load("en_core_web_sm")

def calculate_language_frequency(text):
    # 使用spaCy进行分词、词性标注和词形归并
    doc = nlp(text)

    # 提取词语并计算频率
    words = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    word_freq = Counter(words)
    total_words = sum(word_freq.values())
    language_freq = {word: freq / total_words for word, freq in word_freq.items()}

    return language_freq

# 示例用法
text = "http://emoticonfun.org/"
language_freq = calculate_language_frequency(text)

# 打印词语及其在自然语言中的频率
for word, freq in language_freq.items():
    print(word, freq)