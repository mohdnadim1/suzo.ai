from transformers import pipeline

class ChatbotEngine:
    def __init__(self, model_name="microsoft/DialoGPT-medium"):
        self.chatbot = pipeline("text-generation", model=model_name)
        # The conversation history will be a list of strings.
        self.conversation_history = []

    def get_response(self, user_input):
        # Append the user's input to the history.
        self.conversation_history.append(user_input)

        # Join the history with the model's end-of-string token to create the prompt.
        # This is the format DialoGPT expects.
        prompt = "".join(self.conversation_history) + self.chatbot.tokenizer.eos_token

        # Generate the response.
        response = self.chatbot(prompt, max_length=1000, pad_token_id=self.chatbot.tokenizer.eos_token_id)

        # Extract the generated text and isolate the bot's reply.
        full_response = response[0]['generated_text']
        bot_response = full_response[len(prompt):].strip()

        # Append the bot's response to the history for the next turn.
        self.conversation_history.append(bot_response + self.chatbot.tokenizer.eos_token)

        return bot_response