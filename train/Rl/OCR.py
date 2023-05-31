import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'E:\\Sem_8\\Soft_Development\\Tesseract_OCR\\tesseract.exe'

# 打开图像文件
image = Image.open('test2.png')

# 使用pytesseract进行图像文本提取
text = pytesseract.image_to_string(image, lang='chi_sim')

# 输出提取到的文本
print(text)