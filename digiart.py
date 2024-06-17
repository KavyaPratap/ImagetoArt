import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog

def cartoonize_image(img_path, output_path):
    # Read the image
    img = cv2.imread(img_path)
    if img is None:
        print(f"Could not open or find the image: {img_path}")
        return
    
    original_height, original_width = img.shape[:2]
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    gray_blur = cv2.medianBlur(gray, 7)
    
    edges = cv2.Canny(gray_blur, 50, 150)
    
    kernel = np.ones((1,1),np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    
    color = cv2.bilateralFilter(img, d=9, sigmaColor=55, sigmaSpace=55)
    
    # Convert the image to a simpler color palette using k-means clustering
    Z = color.reshape((-1, 3))
    Z = np.float32(Z)
    
    K = 15  # Number of colors
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((color.shape))
    
    # Create a mask from edges
    edges_inv = cv2.bitwise_not(edges)
    edges_colored = cv2.cvtColor(edges_inv, cv2.COLOR_GRAY2BGR)
    
    cartoon = cv2.bitwise_and(res2, edges_colored)
    
    cartoon = cv2.resize(cartoon, (original_width, original_height))
    

    cv2.imwrite(output_path, cartoon)
    print(f"Cartoonized image saved at: {output_path}")

def open_file_dialog():
    file_path = filedialog.askopenfilename(initialdir='/', title="Open a file")
    input_image_path.set(file_path)
    print(file_path)

def save_file_dialog():
    file_path = filedialog.asksaveasfilename(initialdir='/', title="Save file", defaultextension=".png")
    output_image_path.set(file_path)
    print(file_path)

root = Tk()
root.title("Cartoonizer")

input_image_path = StringVar()
output_image_path = StringVar()

label_open = Label(root, text="Open Image:")
label_open.grid(row=0, column=0, padx=5, pady=5)

entry_open = Entry(root, textvariable=input_image_path, width=50)
entry_open.grid(row=0, column=1, padx=5, pady=5)

button_open = Button(root, text="Browse", command=open_file_dialog)
button_open.grid(row=0, column=2, padx=5, pady=5)

label_save = Label(root, text="Save Image As:")
label_save.grid(row=1, column=0, padx=5, pady=5)

entry_save = Entry(root, textvariable=output_image_path, width=50)
entry_save.grid(row=1, column=1, padx=5, pady=5)

button_save = Button(root, text="Browse", command=save_file_dialog)
button_save.grid(row=1, column=2, padx=5, pady=5)

button_generate = Button(root, text="Generate", command=lambda: cartoonize_image(input_image_path.get(), output_image_path.get()))
button_generate.grid(row=2, column=1, pady=10)

root.mainloop()
#enchance outline and set k=25 if wanted
