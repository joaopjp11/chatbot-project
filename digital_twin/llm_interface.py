# digital_twin/llm_interface.py

from gpt4all import GPT4All

class LLMInterface:
    def __init__(self, model_name: str, model_path: str = None, n_threads: int = None):
        """
        Inicializa o modelo GPT4All.
        """
        self.model = GPT4All(model_name, model_path=model_path, n_threads=n_threads)

    def generate(self, prompt: str, max_tokens: int = 150) -> str:
        with self.model.chat_session():
            response = self.model.generate(prompt, max_tokens=max_tokens)
        return response.strip()
