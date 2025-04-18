from PIL import Image
import re


print("\n=== Image Coder ===\n\nthe coded image name is image_name.png")
img_path = input("Enter image path: ")

while True:
    try:
        img = Image.open(img_path)
        break
    except Exception as e:
        print(f"err: {e}\n")
        img_path = input("Enter image path: ")

ramz = input("Enter your message: ")
print("\nplease wait . . .\n")

CONTIN = True
counter = 0
for i in range(0, img.size[0], 30):
    if CONTIN:
        for j in range(0, img.size[1], 30):
            rgb = img.getpixel((i, j))
            try:
                img.putpixel((i, j), (ord(ramz[counter]), 0, 0))
            except:
                img.putpixel((i, j), (0, rgb[1], rgb[2]))
                CONTIN = False
                break
            counter += 1
    else:
        break


save_img_path = re.search(r"^\w+", img_path).group() + '.png'
img.save(save_img_path)
print(f"coded image name: {save_img_path}")
