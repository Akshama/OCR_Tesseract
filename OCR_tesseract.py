'''==========================================
; Title:  OCR using Pytesser lib
; Author: Akshama
; Date:   22 Oct 2017
;==========================================
Reference: http://www.manejandodatos.es/2014/11/ocr-python-easy/
'''

from PIL import Image
from pytesseract import *
#Your image file's name goes here
image_file = 'pic.png'
im = Image.open(image_file)
text = image_to_string(im)
print text
