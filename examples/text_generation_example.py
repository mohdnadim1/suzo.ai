import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.text.generator import TextGenerator

# Initialize the text generator
generator = TextGenerator()

# Define a prompt
prompt = "The future of AI is"

# Generate text
generated_text = generator.generate(prompt, max_length=50)

# Print the generated text
print(f"Prompt: {prompt}")
print(f"Generated Text: {generated_text}")