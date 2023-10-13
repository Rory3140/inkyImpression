from inky.auto import auto
from PIL import Image

display = auto()

path = 'arsenal.png'
try:  
    img  = Image.open(path)  
except IOError: 
    print('Error: Could not find imaeg')
    pass
display.set_border(inky.BLUE)  
display.set_image(img) 
display.show()
