from PIL import Image

img = Image.open("cute.jpg")
area = (100,100,300,300)
cropped_img = img.crop(area)

img.show()
cropped_img.show()