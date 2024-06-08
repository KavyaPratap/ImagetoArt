import cv2
import numpy as np

def cartoonize_image(img_path, output_path):
    # Read the image
    img = cv2.imread(img_path)
    if img is None:
        print(f"Could not open or find the image: {img_path}")
        return
    
    # Get the dimensions of the input image
    original_height, original_width = img.shape[:2]
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply a median blur to reduce noise
    gray_blur = cv2.medianBlur(gray, 7)
    
    # Detect edges using Canny edge detection
    edges = cv2.Canny(gray_blur, 50, 150)
    
    # Dilate edges to make them more prominent
    kernel = np.ones((1,1),np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    
    # Apply a bilateral filter to reduce color palette while preserving edges
    color = cv2.bilateralFilter(img, d=9, sigmaColor=55, sigmaSpace=55)
    
    # Convert the image to a simpler color palette using k-means clustering
    Z = color.reshape((-1, 3))
    Z = np.float32(Z)
    
    # Define criteria, number of clusters(K) and apply k-means
    K = 9  # Number of colors
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((color.shape))
    
    # Create a mask from edges
    edges_inv = cv2.bitwise_not(edges)
    edges_colored = cv2.cvtColor(edges_inv, cv2.COLOR_GRAY2BGR)
    
    # Combine edges with the color-quantized image
    cartoon = cv2.bitwise_and(res2, edges_colored)
    
    # Resize the cartoon image to the original dimensions
    cartoon = cv2.resize(cartoon, (original_width, original_height))
    
    # Save the output
    cv2.imwrite(output_path, cartoon)
    print(f"Cartoonized image saved at: {output_path}")

# Example usage
input_image_path = 'input6.jpg'  # Replace with your input image path
output_image_path = 'digiart1.png'  # Replace with your desired output path

cartoonize_image(input_image_path, output_image_path)
