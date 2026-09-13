from deepeval.benchmarks import GSM8K
from .deepeval_llm import OllamaDeepEvalLLM

class GSM8KBenchmark:
    name = "GSM8K"

    def run(self, model: str, hardware: str) -> dict:
        llm = OllamaDeepEvalLLM(model=model)
        
        try:
            benchmark = GSM8K(n_shots=0, n_problems=20)
        except TypeError:
            benchmark = GSM8K(n_shots=0)
        
        original_load = getattr(benchmark, 'load_benchmark_dataset', None)
        if original_load and callable(original_load):
            def limited_load(*args, **kwargs):
                res = original_load(*args, **kwargs)
                if res is None:
                    return res
                if hasattr(res, 'select'):
                    return res.select(range(min(20, len(res))))
                return res[:20]
            benchmark.load_benchmark_dataset = limited_load

        benchmark.evaluate(model=llm)
        
        return {
            "benchmark": self.name,
            "model": model,
            "hardware": hardware,
            "score": getattr(benchmark, 'overall_score', 0.0),
            "details": [{"query": getattr(pred, 'input', ''), "correct": getattr(pred, 'success', False)} for pred in getattr(benchmark, 'predictions', [])]
        }