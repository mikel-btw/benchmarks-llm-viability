import ollama
from deepeval.models.base_model import DeepEvalBaseLLM

class OllamaDeepEvalLLM(DeepEvalBaseLLM):
    def __init__(self, model: str):
        self.model_name = model

    def load_model(self):
        # The model is managed externally by the local Ollama daemon
        return self.model_name

    def generate(self, prompt: str) -> str:
        response = ollama.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.message.content

    async def a_generate(self, prompt: str) -> str:
        client = ollama.AsyncClient()
        response = await client.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.message.content

    def get_model_name(self) -> str:
        return self.model_name