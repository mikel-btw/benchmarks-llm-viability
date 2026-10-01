from deepeval.benchmarks import HellaSwag
from .deepeval_llm import OllamaDeepEvalLLM

class HellaSwagBenchmark:
    name = "HellaSwag"

    def run(self, model: str, hardware: str) -> dict:
        llm = OllamaDeepEvalLLM(model=model)
        benchmark = HellaSwag(n_shots=0, n_problems=10)
        
        benchmark.evaluate(model=llm)
        
        return {
            "benchmark": self.name,
            "model": model,
            "hardware": hardware,
            "score": getattr(benchmark, 'overall_score', 0.0),
            "details": [{"query": getattr(pred, 'input', ''), "correct": getattr(pred, 'success', False)} for pred in getattr(benchmark, 'predictions', [])]
        }