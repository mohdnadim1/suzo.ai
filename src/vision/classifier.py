from transformers import pipeline
from PIL import Image

class ImageClassifier:
    def __init__(self, model_name="google/vit-base-patch16-224"):
        self.classifier = pipeline("image-classification", model=model_name)

    def classify(self, image_path):
        try:
            image = Image.open(image_path)
            results = self.classifier(image)
            return results[0]['label']
        except FileNotFoundError:
            return "Image file not found."
        except Exception as e:
            return f"An error occurred: {e}"