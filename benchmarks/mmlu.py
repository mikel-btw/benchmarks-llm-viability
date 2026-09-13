from deepeval.benchmarks import MMLU
from .deepeval_llm import OllamaDeepEvalLLM

class MMLUBenchmark:
    name = "MMLU"

    def run(self, model: str, hardware: str) -> dict:
        llm = OllamaDeepEvalLLM(model=model)
        benchmark = MMLU(n_shots=0)
        
        # Monkey-patch dataset loader to enforce 10-question limit
        original_load = getattr(benchmark, 'load_benchmark_dataset', None)
        if original_load and callable(original_load):
            def limited_load(*args, **kwargs):
                res = original_load(*args, **kwargs)
                if res is None:
                    return res
                if hasattr(res, 'select'): # Support for HuggingFace Datasets
                    return res.select(range(min(10, len(res))))
                return res[:10] # Support for standard lists
            benchmark.load_benchmark_dataset = limited_load

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