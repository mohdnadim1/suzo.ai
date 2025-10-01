import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.vision.classifier import ImageClassifier
from PIL import Image
import os

# Create a dummy image file for demonstration purposes
if not os.path.exists("dummy_image.jpg"):
    img = Image.new('RGB', (60, 30), color = 'red')
    img.save('dummy_image.jpg')

# Initialize the image classifier
classifier = ImageClassifier()

# Path to the image file
image_path = "dummy_image.jpg"

# Classify the image
label = classifier.classify(image_path)

# Print the result
print(f"The image is classified as: {label}")