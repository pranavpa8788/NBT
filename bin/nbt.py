from PIL import Image
import time

#TO DO:
# Back propagation
# Documentation
# Comments

offset = 7
lower_threshold = 20
upper_threshold = lower_threshold + offset

img_path = 'Images/dog.jpg'
img = Image.open(img_path)
img = img.convert('RGB')

width, height = img.size
area = width * height

img_data = img.getdata()

r_band, g_band, b_band = img.getdata(band=0), img.getdata(band=1), img.getdata(band=2)

r_avg, g_avg, b_avg = sum(r_band)/len(r_band), sum(g_band)/len(g_band), sum(b_band)/len(b_band)

mark_color = (0, 200, 200)

for pixel in range(area):
    r_diff, g_diff, b_diff = abs(img_data[pixel][0] - r_avg), abs(img_data[pixel][1] - g_avg), abs(img_data[pixel][2] - b_avg)
    if min(r_diff, g_diff, b_diff) >= lower_threshold:
        if max(r_diff, g_diff, b_diff) <= upper_threshold:
            y, x = pixel//width, pixel%width
            img.putpixel((x, y), mark_color)

img.show()
