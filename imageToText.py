import pytesseract as tess
from gtts import gTTS
import os
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('textHand2.png')
text = tess.image_to_string(img)

print(text)

with open('text_file.txt', mode='w') as file:
    file.write(text)
    print("ready")

fh = open("text_file.txt", "r")
myText = fh.read().replace("\n", " ")
language = 'en'
output  = gTTS(text = myText, lang = language, slow = True)
output.save("speech1.mp3")
fh.close()
os.system("start speech1.mp3") 


# adds more image processing capabilities
#from PIL import Image, ImageEnhance
# assigning an image from the source path
#img = Image.open(‘image_test/virginia-quote.jpg’)
# adding some sharpness and contrast to the image 
#enhancer1 = ImageEnhance.Sharpness(img)
#enhancer2 = ImageEnhance.Contrast(img)
#img_edit = enhancer1.enhance(20.0)
#img_edit = enhancer2.enhance(1.5)
# save the new image
#img_edit.save("edited_image.png")
# converts the image to result and saves it into result variable
#result = pytesseract.image_to_string(img_edit)
#with open(‘text_result2.txt’, mode =’w’) as file:
#file.write(result)
#print(“ready!”)
