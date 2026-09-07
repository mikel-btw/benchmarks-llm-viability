from datetime import datetime
from typing import List, Dict, Any
from benchmarks import ALL_BENCHMARKS
from core.metrics import InferenceMetrics
from core.scorer import ManualScorer
from core.recorder import ResultRecorder

class BenchmarkRunner:
    def __init__(self, hardware: str, model: str):
        self.hardware = hardware
        self.model = model

    def run(self) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []

        print(f"\n{'='*42}\nStarting Benchmark Run\nHardware: {self.hardware}\nModel:    {self.model}\n{'='*42}\n")

        for benchmark in ALL_BENCHMARKS:
            print(f"\n--- Category: {benchmark.name} ---")
            prompts = benchmark.get_prompts()

            for i, prompt in enumerate(prompts, 1):
                print(f"\n[{i}/{len(prompts)}] Prompt: {prompt}")
                print("Generating response from Ollama...")

                metrics = InferenceMetrics.measure_stream_response(self.model, prompt)

                print(f"\nResponse:\n{metrics['response']}\n")
                print(f"Metrics -> TTFT: {metrics['ttft_seconds']}s | "
                      f"Total Time: {metrics['total_time_seconds']}s | "
                      f"Speed: {metrics['tokens_per_second']} tok/s | "
                      f"RAM: {metrics['ram_used_mb']} MB")

                score = ManualScorer.get_score()

                results.append({
                    "hardware": self.hardware,
                    "model": self.model,
                    "benchmark": benchmark.name,
                    "prompt": prompt,
                    "response": metrics["response"],
                    "score": score,
                    "ttft_seconds": metrics["ttft_seconds"],
                    "total_time_seconds": metrics["total_time_seconds"],
                    "tokens_per_second": metrics["tokens_per_second"],
                    "ram_used_mb": metrics["ram_used_mb"],
                    "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                })

        ResultRecorder.save(self.hardware, self.model, results)
        return results