from fastapi import FastAPI, File, UploadFile
from src.text.generator import TextGenerator
from src.vision.classifier import ImageClassifier
from src.chatbot.engine import ChatbotEngine
import uvicorn
import os
from PIL import Image
import io

app = FastAPI()

# Initialize models
text_generator = TextGenerator()
image_classifier = ImageClassifier()
chatbot_engine = ChatbotEngine()

@app.post("/generate")
async def generate_text(prompt: str):
    """
    Generates text based on a given prompt.
    """
    generated_text = text_generator.generate(prompt)
    return {"generated_text": generated_text}

@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    """
    Classifies an uploaded image.
    """
    # Ensure the upload directory exists
    os.makedirs("uploads", exist_ok=True)

    # Save the uploaded file temporarily
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Classify the image
    label = image_classifier.classify(file_path)

    # Clean up the uploaded file
    os.remove(file_path)

    return {"label": label}

@app.post("/chat")
async def chat_with_bot(message: str):
    """
    Gets a response from the chatbot.
    """
    response = chatbot_engine.get_response(message)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)