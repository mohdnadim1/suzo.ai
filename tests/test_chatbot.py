import unittest
from unittest.mock import MagicMock, patch
from src.chatbot.engine import ChatbotEngine

class TestChatbotEngine(unittest.TestCase):

    @patch('src.chatbot.engine.pipeline')
    def test_prompt_formatting(self, mock_pipeline):
        # Arrange
        # Create a mock for the tokenizer and the pipeline
        mock_tokenizer = MagicMock()
        mock_tokenizer.eos_token = "<|endoftext|>"
        mock_tokenizer.eos_token_id = 50256

        mock_chatbot_pipeline = MagicMock()
        mock_chatbot_pipeline.tokenizer = mock_tokenizer
        # Configure the mock pipeline to return a predefined response
        mock_chatbot_pipeline.return_value = [{'generated_text': "Hello<|endoftext|>Hi there!"}]
        mock_pipeline.return_value = mock_chatbot_pipeline

        engine = ChatbotEngine()

        # Act
        engine.get_response("Hello") # First turn
        engine.get_response("How are you?") # Second turn

        # Assert
        # Check the prompt passed to the text-generation pipeline on the *second* call
        # The history should be ["Hello", "Hi there!", "How are you?"]
        # The buggy prompt is "HelloHi there!<|endoftext|>How are you?<|endoftext|>"
        # The correct prompt should be "Hello<|endoftext|>Hi there!<|endoftext|>How are you?<|endoftext|>"

        # To get the bot response for the first turn, we need to simulate the logic
        # from the engine's get_response method.
        # prompt1 = "Hello" + mock_tokenizer.eos_token -> "Hello<|endoftext|>"
        # full_response1 = "Hello<|endoftext|>Hi there!"
        # bot_response1 = "Hi there!"
        # history after turn 1 = ["Hello", "Hi there!<|endoftext|>"]

        # prompt2 = "HelloHi there!<|endoftext|>How are you?" + mock_tokenizer.eos_token
        # -> "HelloHi there!<|endoftext|>How are you?<|endoftext|>"

        # Let's get the actual call from the mock
        # The second call to the pipeline is what we want to inspect.
        args, kwargs = mock_chatbot_pipeline.call_args_list[1]
        actual_prompt = args[0]

        expected_prompt = "Hello<|endoftext|>Hi there!<|endoftext|>How are you?<|endoftext|>"

        # This assertion will fail with the current implementation
        self.assertEqual(expected_prompt, actual_prompt)

if __name__ == '__main__':
    unittest.main()