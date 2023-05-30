import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from urllib.parse import urlparse


# nltk.download('punkt')

def calculate_url_length(url):
    # 计算URL的长度
    return len(url)

def judge_url_isornothttps(url):
    #判断URL是否是HTTPS协议
    if url.startswith('https'):
        return 1
    return 0

def tokenize_url(url):
    # 使用urllib.parse解析URL
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    domain = parsed_url.netloc


    # 分割域名为子域和顶级域
    subdomain, _, top_level_domain = domain.rpartition('.')
    tokens = subdomain.split('.') + [top_level_domain]
    tokens_without_last = tokens[:-1]
    return scheme, tokens_without_last


def calculate_language_frequency(tokens):
    # 计算分词后的语言频率
    freq_dist = FreqDist(tokens)
    total_tokens = len(tokens)
    language_freq = {token: freq_dist[token] / total_tokens for token in freq_dist.keys()}
    return language_freq




# 示例用法
url = "http://emoticonfun.org/"
shceme, tokens = tokenize_url(url)
language_freq = calculate_language_frequency(tokens)

# 打印语言频率
for token, freq in language_freq.items():
    print(token, freq)

if shceme == "http":
    print("no")


