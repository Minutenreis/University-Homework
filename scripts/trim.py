from PIL import Image
import sys
import time
import os
import math

start = time.time()

if len(sys.argv) != 2:
    print("Usage: python trim.py <image>")
    exit(1)

input_name = sys.argv[1]

input_image = Image.open(input_name)
output_name = os.path.basename(input_name).split(".")[0] + "_trimmed.png"

input_image = input_image.convert("RGBA")

datas = input_image.getdata()

radius = 15
radius_diag = math.floor(radius * math.cos(math.pi / 4))
radius_short = math.floor(radius * math.sin(math.pi / 8))
radius_long = math.floor(radius * math.cos(math.pi / 8))

def shouldAddWhite(datas, i, j):
    for l,k in [(-radius_diag,-radius_diag),(-radius_diag,radius_diag),(radius_diag,-radius_diag),(radius_diag,radius_diag), (-radius,0),(radius,0),(0,-radius),(0,radius), (-radius_short,-radius_long),(-radius_short,radius_long),(radius_short,-radius_long),(radius_short,radius_long), (-radius_long,-radius_short),(-radius_long,radius_short),(radius_long,-radius_short),(radius_long,radius_short)]:
    # for l,k in [(-radius,-radius),(-radius,radius),(radius,-radius),(radius,radius)]:
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