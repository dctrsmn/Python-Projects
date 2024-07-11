import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import easyocr
from PIL import Image, ImageTk

def recognize_text(img_path):
    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path)

def process_image(img_path):
    try:
        result = recognize_text(img_path)
        text_list = [text for (bbox, text, prob) in result]
        print("Recognized Text:")
        for text in text_list:
            print(text)
        extracted_text = "\n".join(text_list)
        label.config(text=f"Extracted Text:\n{extracted_text}")
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        image_label.config(image=image)
        image_label.image = image
        image_width, image_height = image.width(), image.height()
        window_width = min(image_width, 800)
        window_height = min(image_height, 600)
        root.geometry(f"{window_width}x{window_height}")
    except Exception as e:
        print(f"Error: {e}")
        label.config(text=f"Error processing image: {e}")
def select_image():
    file_path = filedialog.askopenfilename()
    if len(file_path) > 0:
        process_image(file_path)

root = tk.Tk()
root.title("OCR Uygulaması")
root.geometry("800x600")

load_button = tk.Button(root, text="Resim Yükle", command=select_image)
load_button.pack()

label = tk.Label(root, text="Yüklenecek resmi seçin ve analiz edin.", wraplength=600)
label.pack()

image_label = tk.Label(root)
image_label.pack()

root.mainloop()


