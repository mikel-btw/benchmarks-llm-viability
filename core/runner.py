from datetime import datetime
from typing import List, Dict, Any
from benchmarks import DEEPEVAL_BENCHMARKS, MANUAL_BENCHMARKS
from core.metrics import InferenceMetrics
from core.scorer import ManualScorer
from core.recorder import ResultRecorder

class BenchmarkRunner:
    def __init__(self, hardware: str, model: str):
        self.hardware = hardware
        self.model = model

    def run(self) -> List[Dict[str, Any]]:
        print("\nSelect benchmark to run:")
        print("  [1] MMLU (DeepEval)")
        print("  [2] GSM8K (DeepEval)")
        print("  [3] HellaSwag (DeepEval)")
        print("  [4] TruthfulQA (DeepEval)")
        print("  [5] ARC Challenge (DeepEval)")
        print("  [6] Prompt Qualification (Manual scoring)")
        print("  [7] Run all")
        
        while True:
            choice = input("Enter choice (1-7): ").strip()
            if choice in [str(i) for i in range(1, 8)]:
                choice = int(choice)
                break
            print("Invalid selection. Please enter a number between 1 and 7.")

        results: List[Dict[str, Any]] = []

        print(f"\n{'='*42}\nStarting Benchmark Run\nHardware: {self.hardware}\nModel:    {self.model}\n{'='*42}\n")

        deepeval_targets = []
        manual_targets = []

        # Map user choice to the execution targets
        if 1 <= choice <= 5:
            deepeval_targets.append(DEEPEVAL_BENCHMARKS[choice - 1]())
        elif choice == 6:
            manual_targets = MANUAL_BENCHMARKS
        elif choice == 7:
            deepeval_targets = [B() for B in DEEPEVAL_BENCHMARKS]
            manual_targets = MANUAL_BENCHMARKS

        # 1. Run DeepEval benchmarks (Automated)
        for benchmark_instance in deepeval_targets:
            print(f"\n--- Running DeepEval: {benchmark_instance.name} ---")
            try:
                res = benchmark_instance.run(model=self.model, hardware=self.hardware)
                results.append(res)
                print(f"Score: {res.get('score', 0)}")
            except Exception as e:
                print(f"[-] Error running {benchmark_instance.name}: {e}")

        # 2. Run Prompt Qualification benchmark (Manual Scoring)
        for benchmark in manual_targets:
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

        if results:
            ResultRecorder.save(self.hardware, self.model, results)
            
        return results