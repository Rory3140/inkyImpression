from inky.auto import auto
from PIL import Image

display = auto()

path = '/testImage'
try:  
    img  = Image.open(path)  
except IOError: 
    pass
  
display.set_image(img) 
display.show()
