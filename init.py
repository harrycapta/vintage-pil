import vintage
from PIL import Image

im = Image.open('input.jpg')
im = vintage.vintage_colors(im)
im.save('vintage_picture.jpg')
