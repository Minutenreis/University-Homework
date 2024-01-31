from PIL import Image
import sys
import time
import os

start = time.time()

if len(sys.argv) != 2:
    print("Usage: python trim.py <image>")
    exit(1)

input_name = sys.argv[1]

input_image = Image.open(input_name)
output_name = os.path.basename(input_name).split(".")[0] + "_trimmed.png"

input_image = input_image.convert("RGBA")

datas = input_image.getdata()

radius = 10

def shouldAddWhite(datas, i, j):
    for k in range(-radius, radius+1):
        for l in range(-radius, radius+1):
            if k*k + l*l <= radius*radius:
                if i+k >= 0 and i+k < input_image.width and j+l >= 0 and j+l < input_image.height:
                    if datas[i+k + (j+l) * input_image.width][3] != 0:
                        return True
    return False

newData = []

for i in range(input_image.width * input_image.height):
    if datas[i][3] == 0 and shouldAddWhite(datas, i % input_image.width, i // input_image.width):
        newData.append((255,255,255,255))
    else:
        newData.append(datas[i])
                
input_image.putdata(newData)
input_image.save(output_name, "PNG")

end = time.time()
print("Trimmed image saved as " + output_name + " in " + str(end - start) + " seconds.")