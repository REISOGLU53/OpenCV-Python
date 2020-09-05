from PIL import Image
import pytesseract

img = Image.open("genclige.jpg")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(img, lang="eng")
print(text)
