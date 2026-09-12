from deepeval.benchmarks import GSM8K
from .deepeval_llm import OllamaDeepEvalLLM

class GSM8KBenchmark:
    name = "GSM8K"

    def run(self, model: str, hardware: str) -> dict:
        llm = OllamaDeepEvalLLM(model=model)
        benchmark = GSM8K(n_shots=0)
        
        if hasattr(benchmark, 'golden_set') and len(benchmark.golden_set) > 20:
            benchmark.golden_set = benchmark.golden_set[:20]
        if hasattr(benchmark, 'dataset') and len(benchmark.dataset) > 20:
            benchmark.dataset = benchmark.dataset[:20]

        benchmark.evaluate(model=llm)
        
        return {
            "benchmark": self.name,
            "model": model,
            "hardware": hardware,
            "score": getattr(benchmark, 'overall_score', 0.0),
            "details": [{"query": getattr(pred, 'input', ''), "correct": getattr(pred, 'success', False)} for pred in getattr(benchmark, 'predictions', [])]
        }