from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from KeyWordExtracting import KeyWordExtracting

url_list = []  # 创建一个空列表来存储URL

# 创建Chrome浏览器选项
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 无界面模式，可以在后台运行

# 创建Chrome浏览器实例
driver = webdriver.Chrome(options=chrome_options)

# # 创建cookie字典
# cookie_dict = {'_cnt': '%3Bs1536*864*24%3Bt7%3Bo448.7914574283041%3BlSun%20May%2021%202023%2022%3A18%3A44%20GMT+0800%20%28%u4E2D%u56FD%u6807%u51C6%u65F6%u95F4%29%3Bv3',
#                'RPSESSION': '3e08e3cea6514eab51e9cc52af46cb78',
#                '_lpg': '0.05700265916602265',
#                'm2': 'TEN3R0MrM2JGZkMvWVlEcG5wZWUreFRxRVd5ZTR5SndhcVRyTktjMFNqSTNkdTNhY2NKRVhtRytPd3d4WXNLVA%3D%3D',
#                '_cnt': '%3Bs1536*864*24%3Bt52%3Bo448.06274630450554%3BlSun%20May%2021%202023%2022%3A17%3A14%20GMT+0800%20%28%u4E2D%u56FD%u6807%u51C6%u65F6%u95F4%29%3Bv3',
#                'PHPSESSID': 'dnoscmp49b20cue4b41q5p4hpa'}

# # 添加cookie
# driver.add_cookie(cookie_dict)

# # 刷新页面使cookie生效
# driver.refresh()

# 打开publicwww.com登录页面
driver.get('https://publicwww.com/profile/login.html')

driver.implicitly_wait(5)  # 等待5秒钟
# wait = WebDriverWait(driver, 10)
# wait.until(EC.url_to_be('https://publicwww.com/'))
# # 找到登录按钮并点击
# login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
# login_button.click()

# 找到用户名和密码的输入框，并输入你的登录凭据
username_input = driver.find_element(By.XPATH, '//*[@id="input01"]')
password_input = driver.find_element(By.XPATH, '//*[@id="input02"]')
username_input.send_keys('yuntian1215@sjtu.edu.cn')  # 输入用户名
password_input.send_keys('2da515c7')  # 输入密码

# 提交表单，完成登录
password_input.send_keys(Keys.RETURN)

# 等待登录完成，可以根据需要调整等待时间
driver.implicitly_wait(5)  # 等待5秒钟

def CreateSearchUrl(keyword):
    # 要搜索的关键词
    quoted_keyword = '"' + keyword + '"'
    print(quoted_keyword)
    encoded_keyword = quote(quoted_keyword, safe='')  # 对关键词进行URL编码
    print(encoded_keyword)

    # 构造搜索URL
    search_url = f'https://publicwww.com/websites/{encoded_keyword}'
    return search_url

def GetURL(search_url):
    
    print(search_url)
    search_url = str(search_url)
    print(search_url)

    # 使用浏览器打开搜索URL
    driver.get(search_url)

    # 等待页面加载完成
    driver.implicitly_wait(10)  # 设置隐式等待时间，根据需要进行调整

    # 获取页面源代码
    html = driver.page_source

    # 解析HTML内容
    soup = BeautifulSoup(html, 'html.parser')

    # 提取搜索结果的URL
    link_elements = soup.select('table tbody tr td a')
    for link_element in link_elements:
        url = link_element.get('href')
        if url.startswith('http'):
            url_list.append(url)


def GetBadUrl(num):
    keywords = KeyWordExtracting()

    for keyword in keywords:
        # 使用相应关键词搜集恶意网页
        search_url = CreateSearchUrl(keyword)
        print(search_url)
        
        GetURL(search_url)
    
        if len(url_list) > num:
            break

    # 打印符合条件的URL
    for url in url_list:
        print(url)
   
GetBadUrl(256)

filename = "badurls.txt"

# 打开文件以写入模式，如果文件不存在则创建新文件
with open(filename, "w") as file:
    # 遍历 url_list，将每个 URL 写入文件中
    for url in url_list:
        file.write(url + "\n")

# 关闭浏览器
driver.quit()