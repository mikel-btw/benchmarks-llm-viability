from deepeval.benchmarks import ARC
from deepeval.benchmarks.modes import ARCMode
from .deepeval_llm import OllamaDeepEvalLLM

class ARCChallengeBenchmark:
    name = "ARC Challenge"

    def run(self, model: str, hardware: str) -> dict:
        llm = OllamaDeepEvalLLM(model=model)
        
        try:
            benchmark = ARC(n_shots=0, n_problems=10, mode=ARCMode.CHALLENGE)
        except TypeError:
            benchmark = ARC(n_shots=0, n_problems=10)
            
        benchmark.evaluate(model=llm)
        
        return {
            "benchmark": self.name,
            "model": model,
            "hardware": hardware,
            "score": getattr(benchmark, 'overall_score', 0.0),
            "details": [{"query": getattr(pred, 'input', ''), "correct": getattr(pred, 'success', False)} for pred in getattr(benchmark, 'predictions', [])]
        }