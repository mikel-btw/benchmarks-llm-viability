from deepeval.benchmarks import MMLU
from .deepeval_llm import OllamaDeepEvalLLM

class MMLUBenchmark:
    name = "MMLU"

    def run(self, model: str, hardware: str) -> dict:
        llm = OllamaDeepEvalLLM(model=model)
        benchmark = MMLU(n_shots=0)
        
        # Enforce the 20-question limit
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
            "details": [
                {"query": getattr(pred, 'input', ''), "correct": getattr(pred, 'success', False)} 
                for pred in getattr(benchmark, 'predictions', [])
            ]
        }
