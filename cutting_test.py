import os
from PIL import Image

path_input = "Test_RSC_SY/Rookie"
path_output = "Test_RSC_SY\\Rookie_cut"

box = (640, 640, 1180, 1080)

for (root, directories, files) in os.walk(path_input):
    for file in files:
        input_img_path = os.path.join(root, file)
        img = Image.open(input_img_path)
        cut_img = img.crop(box)
        cut_img.save(os.path.join(path_output, file))