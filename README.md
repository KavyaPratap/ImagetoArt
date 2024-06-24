<h1>Cartoonizer Application</h1><br>
This program allows you to convert any image into a cartoon-like version using OpenCV and Tkinter for the graphical user interface (GUI). The program applies various image processing techniques to achieve a cartoon effect.

<h3>**Features**</h3>
Load an image from your computer.

Convert the loaded image to a cartoonized version.

Save the cartoonized image to your desired location.

<h3>**Requirements**</h3>

Python 3.x
OpenCV
NumPy
Tkinter (comes pre-installed with Python)

<h3>**Installation**</h3>

Ensure you have the required libraries installed. You can install them using pip:

<u>**bash, Copy code**</u>

pip install opencv-python numpy

<u>**How to Use**</u>

Open the Program:

Run the script to launch the GUI.
You will see a window with options to open an image, save an image, and generate the cartoonized image.

Load an Image:

Click the "Browse" button next to "Open Image".
Select the image file you want to cartoonize from the file dialog that appears.

Save Location:

Click the "Browse" button next to "Save Image As".
Choose the location and name for the cartoonized image file to be saved.

Generate Cartoonized Image:

Click the "Generate" button.

The cartoonized image will be processed and saved to the location you specified.

A message will appear in the console indicating the save location of the cartoonized image.

<h2>**Logic and Workflow**</h2>

Reading the Image:

The image is read using cv2.imread().
Grayscale Conversion and Blurring:

The image is converted to grayscale using cv2.cvtColor().
A median blur is applied to reduce noise using cv2.medianBlur().
Edge Detection:

Edges in the image are detected using the Canny edge detector cv2.Canny().

Edge Enhancement:

The edges are dilated to make them more pronounced using cv2.dilate().

Color Filtering:

A bilateral filter is applied to the original image to smooth colors while keeping edges sharp using cv2.bilateralFilter().

Color Quantization:

The image is converted to a simpler color palette using k-means clustering.
This reduces the number of colors in the image, giving it a cartoon-like appearance.
Combining Edges and Colors:

The edges are inverted and combined with the color-filtered image using cv2.bitwise_and() to produce the final cartoon effect.

Resizing and Saving:

The final cartoonized image is resized to the original dimensions.
The image is saved using cv2.imwrite().
GUI Components

Labels and Entries:

Label and Entry widgets are used to create input fields for file paths.

Buttons:

Button widgets trigger the open file dialog, save file dialog, and the cartoonization process.

<h3>Enhancements</h3>

You can adjust the number of colors by changing the value of K in the k-means clustering step. Setting K = 25 will provide finer color details.
The outline enhancement can be fine-tuned by adjusting the parameters of the edge detection and dilation steps.
By following these instructions, you should be able to use and understand the cartoonizer program effectively.

<h2>Contributing</h2>
    <p>Contributions are welcome! Feel free to fork this project and submit pull requests with improvements or new features.</p>
    
   <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="https://opensource.org/licenses/MIT">LICENSE</a> file for details.</p>
    



