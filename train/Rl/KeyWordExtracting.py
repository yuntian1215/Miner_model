import re

def KeyWordExtracting(): 
    
    file_path = "filters.txt"

    with open(file_path, "r") as file:
        text = file.read()

    text = text.splitlines()

    matching_keywords = [] 

    for line in text:
        filtered_letters = list(filter(str.isalnum, line))
        first_letter = filtered_letters[0]
        last_letter = filtered_letters[len(filtered_letters) - 1]
        first_letter_index = line.find(first_letter) if first_letter else -1
        last_letter_index = line.rfind(last_letter) if first_letter else -1

        keyword = line[first_letter_index : last_letter_index + 1]
        matching_keywords.append(keyword)  # 将关键词添加到匹配列表中

    extend_keywords = ["new CoinHive.Anonymous", "new CryptoLoot.Anonymous", "lib/miner.min.js", "new deep.Miner.Anonymous",
                        "new CRLT.Anonymous", "new CoinImp.Anonymous", "new CoinPirate.Anonymous", "ppoi.org/lib/projectpoi.min.js", "new ProjectPoi.Anonymous"]
        
    matching_keywords.extend(extend_keywords)

        # print(matching_keywords)
        # 测试下标集
        # print("First letter:", first_letter)
        # print("First letter index:", first_letter_index)
        # print("Last letter:", last_letter)
        # print("Last letter index:", last_letter_index)

    # 测试关键词集
    # print(matching_keywords)

    return matching_keywords
        


    html_file_path = "GoodURL\\f9750d2b4598085e45412c54c4a0554a.html"

    with open(html_file_path, "r", encoding="utf-8") as file:
        html_text = file.read()

    pattern = r"\b(?:{})\b".format("|".join(map(re.escape, matching_keywords)))
    html_contains_keywords = re.findall(pattern, html_text, re.IGNORECASE)

    if html_contains_keywords:
        print("HTML 包含匹配的关键词")
        print(html_contains_keywords)
    else:
        print("HTML 不包含匹配的关键词")
