import requests
from bs4 import BeautifulSoup
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

from KeyWordExtracting import KeyWordExtracting

timeout_url = []

def GetHtml(url):
    # 设置页面加载超时时间为10秒
    timeout = 2

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无界面模式，可以在后台运行
    chrome_options.add_argument('--ignore-certificate-errors')
    
    # 创建Chrome浏览器实例
    driver = webdriver.Chrome(options=chrome_options)
    # 设置页面加载超时时间为5秒
    driver.set_page_load_timeout(10)

    # 创建Chrome浏览器实例
    try:   
        driver.get(url)
        html = driver.page_source
        print(html)
    except:
        html = " "
        with open('timeouturls.txt', 'a') as file:
            file.write(url + '\n')
        timeout_url.append(url)
    finally:
        driver.quit()
        print("success")
        return html

def AnalysisHtml(url):
    html = GetHtml(url)
    keywords = KeyWordExtracting()

    pattern = r"\b(?:{})\b".format("|".join(map(re.escape, keywords)))
    html_contains_keywords = re.findall(pattern, html, re.IGNORECASE)

    if html_contains_keywords:
        keywordappeartimes = len(html_contains_keywords)
    else:
        keywordappeartimes = 0
    
    cryptfuncs = ["Cryptonight", "SHA256", "hash", "wasmwrapper", "Web Assembly", "scrypt"]

    pattern = r"\b(?:{})\b".format("|".join(map(re.escape, cryptfuncs)))
    html_contains_cryptfuncs = re.findall(pattern, html, re.IGNORECASE)

    if html_contains_cryptfuncs:
        cryptfunctionappeartimes = len(html_contains_cryptfuncs)
    else:
        cryptfunctionappeartimes = 0

    dynamicfuncs = ["setTimeout", "setInterval"]

    pattern = r"\b(?:{})\b".format("|".join(map(re.escape, dynamicfuncs)))
    html_contains_dynamicfuncs = re.findall(pattern, html, re.IGNORECASE)

    if html_contains_dynamicfuncs:
        dynamicfunctionappeartimes = len(html_contains_cryptfuncs)
    else:
        dynamicfunctionappeartimes = 0

    cpulimits = ["throttle", "throttle:0.9"]
    pattern = r"\b(?:{})\b".format("|".join(map(re.escape, cpulimits)))
    html_contains_cpulimits = re.findall(pattern, html, re.IGNORECASE)

    if html_contains_dynamicfuncs:
        ifcpulimit = 1
    else:
        ifcpulimit = 0

    return keywordappeartimes, cryptfunctionappeartimes, dynamicfunctionappeartimes, ifcpulimit

def AnalysisHtml2(html):
    keywords = KeyWordExtracting()

    pattern = r"\b(?:{})\b".format("|".join(map(re.escape, keywords)))
    html_contains_keywords = re.findall(pattern, html, re.IGNORECASE)

    if html_contains_keywords:
        keywordappeartimes = len(html_contains_keywords)
    else:
        keywordappeartimes = 0
    
    cryptfuncs = ["Cryptonight", "SHA256", "hash", "wasmwrapper", "Web Assembly", "scrypt"]

    pattern = r"\b(?:{})\b".format("|".join(map(re.escape, cryptfuncs)))
    html_contains_cryptfuncs = re.findall(pattern, html, re.IGNORECASE)

    if html_contains_cryptfuncs:
        cryptfunctionappeartimes = len(html_contains_cryptfuncs)
    else:
        cryptfunctionappeartimes = 0

    dynamicfuncs = ["setTimeout", "setInterval"]

    pattern = r"\b(?:{})\b".format("|".join(map(re.escape, dynamicfuncs)))
    html_contains_dynamicfuncs = re.findall(pattern, html, re.IGNORECASE)

    if html_contains_dynamicfuncs:
        dynamicfunctionappeartimes = len(html_contains_cryptfuncs)
    else:
        dynamicfunctionappeartimes = 0

    cpulimits = ["throttle", "throttle:0.9"]
    pattern = r"\b(?:{})\b".format("|".join(map(re.escape, cpulimits)))
    html_contains_cpulimits = re.findall(pattern, html, re.IGNORECASE)

    if html_contains_dynamicfuncs:
        ifcpulimit = 1
    else:
        ifcpulimit = 0

    return keywordappeartimes, cryptfunctionappeartimes, dynamicfunctionappeartimes, ifcpulimit

GetHtml("https://www.baidu.com")