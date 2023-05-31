import re
from collections import Counter

# 10个URL示例
urls = [
    "https://slovenskyviral.com/",
    "http://findgiveaways.blogspot.com/",
    "http://psystems.gr",
    # ... 添加更多URL
]

# 构建词汇表
vocabulary = set()
for url in urls:
    # URL预处理
    url = url.lower()
    url = re.sub(r"[^\w\s]", "", url)

    # 分词
    words = url.split()

    # 更新词汇表
    vocabulary.update(words)

# 对每个URL进行向量化
print(vocabulary)
feature_vectors = []
for url in urls:
    # URL预处理
    url = url.lower()
    url = re.sub(r"[^\w\s]", "", url)
    # 分词
    words = url.split()
    # 统计词语出现次数
    word_freq = Counter(words)
    # 构建特征向量
    feature_vector = [word_freq[word] for word in vocabulary]

    # 添加到特征向量列表
    feature_vectors.append(feature_vector)

# 打印特征向量
for i, vector in enumerate(feature_vectors):
    print(f"URL {i+1} 特征向量：{vector}")