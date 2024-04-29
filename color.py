import cv2
import numpy as np

# Load image
image_path = 'data\image.png'
image = cv2.imread(image_path)

if image is None:
    print(f"False {image_path}")
else:
    # Convert image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    mean_color = np.average(image_rgb, axis=0)
    color = np.average(mean_color, axis=0)

    print("Code color of RGB {}".format(tuple(map(int, color))))