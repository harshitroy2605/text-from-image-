import pytesseract
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img=Image.open('1.jpg')
text=pytesseract.image_to_string(img)
print(text)