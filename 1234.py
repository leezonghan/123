from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open(r'C:\Users\leezo\OneDrive\桌面\1624836545176@2x.jpeg')
text = pytesseract.image_to_string(img, lang='eng')
print(text)
