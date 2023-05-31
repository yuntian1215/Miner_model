import os
import glob
import csv
from bs4 import BeautifulSoup
from URLCrawl import AnalysisHtml, AnalysisHtml2

from URLDivide import calculate_url_length, judge_url_isornothttps

def GetCSV():
    filename = "goodurlsrple.txt"

    with open(filename, "r") as file:
        url_list = file.read().splitlines()

    with open("training_dataset5.csv", "a", newline="") as file:
        writer = csv.writer(file)

        headers = ["URL", "UrlLength", "isornotHttps", "KeywordAppearTimes", "CryptFunctionAppearTimes", "DynamicFunctionAppearTimes", "CPUlimits", "Label"]  # 替换为你的属性列名
        writer.writerow(headers)

        # 遍历 URL 列表，为每个 URL 添加标签和其他属性，并写入 CSV 文件
        for url in url_list:
            label = 0
            
            urlLength = calculate_url_length(url)
            isornothttps = judge_url_isornothttps(url)
            
            keywordappeartimes, cryptfunctionappeartimes, dynamicfunctionappeartimes, ifcpulimit = AnalysisHtml(url)

            # 将 URL、标签和其他属性写入 CSV 文件的一行
            writer.writerow([url, urlLength, isornothttps, keywordappeartimes, cryptfunctionappeartimes, dynamicfunctionappeartimes, ifcpulimit, label])


def ModifyBadTrain():
    # 定义目录路径
    directory = 'BadTest'

    # 获取目录中的所有 HTML 文件
    html_files = glob.glob(os.path.join(directory, '*.html'))

    # 遍历 HTML 文件并进行分析
    for file_path in html_files:
        with open(file_path, 'r', encoding = 'UTF-8') as file:
            html_content = file.read()
            
            keywordappeartimes, cryptfunctionappeartimes, dynamicfunctionappeartimes, ifcpulimit = AnalysisHtml2(html_content)
            print("File:", file_path)
            print("keywordappeartimes, cryptfunctionappeartimes, dynamicfunctionappeartimes, ifcpulimit", keywordappeartimes, cryptfunctionappeartimes, dynamicfunctionappeartimes, ifcpulimit)


ModifyBadTrain()
GetCSV()