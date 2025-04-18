
# PixSecret 🔴

**PixSecret** is a simple image steganography tool written in Python. It hides secret messages inside images using the red (R) channel of selected pixels.

---

## 🔍 What is PixSecret?

This tool encodes a message into an image by modifying the red component of pixels. Later, the decoder script can read the message back from the same image.

---

## 🛠️ Features

- 🔴 Hides characters in the red channel of every 30th pixel
- 🧩 Stops reading when a red value of 0 is encountered
- 💡 Simple terminal-based usage
- 🖼️ Works with PNG or JPG images
- 🧪 Great for educational/demo purposes

---

## 🧰 Requirements

- Python 3.12
- Pillow (`pip install pillow`)

---

## 🚀 How to Use

### ▶️ Encoding a message

```bash
python coder.py
```

- Input the path to your image.
- Enter your secret message.
- The new image will be saved with `.png` extension.

### 🔓 Decoding the message

```bash
python decoder.py
```

- Input the path to the image with the hidden message.
- It will print the extracted message.

---

## 💡 How It Works

- Every 30 pixels, both horizontally and vertically, the red (R) value of the pixel is set to the ASCII value of the message character.
- When the message ends, the next red value is set to `0`, signaling the end of the message.
- Green (G) and Blue (B) channels remain unchanged to minimize visual distortion.

---

## 📌 Notes

- For better results, use larger images.
- This method is not secure for serious use — it's designed for fun and learning.
- You can expand this by using LSB (Least Significant Bit) or encrypting messages before hiding.

---

## 🖼️ Example

Original Image → Encoded Image → Decoded Message ✔️

---

## 📜 License

MIT License — use freely, modify, and share.

---

## 🤝 Contributions

Feel free to open issues or submit pull requests if you’d like to improve this tool!

---
