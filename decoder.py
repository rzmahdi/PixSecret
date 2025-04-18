from PIL import Image


print("\n=== Image Decoder ===\n\n")
img_path = input("Enter image path: ")

while True:
    try:
        img = Image.open(img_path)
        break
    except Exception as e:
        print(f"err: {e}\n")
        img_path = input("Enter image path: ")

message = ""
CONTIN = True

for i in range(0, img.size[0], 30):
    if CONTIN:
        for j in range(0, img.size[1], 30):
            rgb = img.getpixel((i, j))
            if rgb[0] == 0:
                CONTIN = False
                break
            message += chr(rgb[0])
    else:
        break

print(f"message: {message}")
