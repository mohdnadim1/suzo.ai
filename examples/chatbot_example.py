import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.chatbot.engine import ChatbotEngine

# Initialize the chatbot engine
chatbot = ChatbotEngine()

# Start a conversation
print("Chatbot initialized. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = chatbot.get_response(user_input)
    print(f"Chatbot: {response}")