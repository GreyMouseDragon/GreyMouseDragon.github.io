from PIL import Image

#765 total
darkest = (0, 51, 76) # x < 191
lightest = (252, 227, 166) # x > 574
light_middle = (112, 150, 158) # 383 < x < 573
dark_middle = (217, 26, 33) # 192 < x < 382

im = Image.open("Sariel_Nirkan_Chibi.png")
image_list = im.getdata()
image_list = list(image_list)

recolored = []

image_total = image_list[0] + image_list[1] + image_list[2]

for i in image_list:
    strength = i[0] + i[1] + i[2]
    if strength >= 546:
        recolored.append(lightest)
    if strength < 546 and strength >= 382:
        recolored.append(light_middle)
    if strength < 382 and strength >= 191:
        recolored.append(dark_middle)
    if strength < 191:
        recolored.append(darkest)


new_image = Image.new("RGB", im.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recolored.jpg", "jpeg")
