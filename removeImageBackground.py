from rembg import remove
from PIL import Image

input_path = 'what-does-sustainable-mean-cover.jpg'
output_path = 'removebg.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
