import sys
import json
from pathlib import Path
from datetime import datetime
import ollama
from config.hardware import HARDWARE_MACHINES
from config.models import ALL_MODELS
from core.runner import BenchmarkRunner
from benchmarks import DEEPEVAL_BENCHMARKS

def check_ollama_status():
    """Verifies that the Ollama local server is running."""
    print("Checking Ollama connection...")
    try:
        ollama.list()
        print("[+] Ollama server is active.\n")
    except Exception:
        print("\n[-] Error: Could not connect to Ollama.")
        print("    Please ensure the daemon is running in another terminal:")
        print("    $ ollama serve")
        sys.exit(1)

def select_hardware() -> str:
    print("Select Hardware Machine Identifier:")
    for key, name in HARDWARE_MACHINES.items():
        print(f"  [{key}] {name}")
    
    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice in HARDWARE_MACHINES:
            return HARDWARE_MACHINES[choice]
        print("Invalid selection.")

def select_model() -> str:
    print("\nSelect LLM Model to Benchmark:")
    model_mapping = {}
    counter = 1

    for category, models in ALL_MODELS.items():
        print(f"\n  -- {category} --")
        for model in models:
            model_mapping[str(counter)] = model
            print(f"    [{counter}] {model}")
            counter += 1

    while True:
        choice = input(f"\nEnter choice (1-{counter - 1}): ").strip()
        if choice in model_mapping:
            return model_mapping[choice]
        print("Invalid model selection.")

def select_mode() -> int:
    print("\nSelect benchmark mode:")
    print("  [1] DeepEval official benchmarks (automated, 20 questions each)")
    print("  [2] Prompt Qualification (manual scoring, Spanish prompts)")
    print("  [3] Both")
    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            return int(choice)
        print("Invalid selection.")

def run_deepeval(hardware: str, model: str):
    print(f"\n{'='*42}")
    print(f"Starting DeepEval Automated Benchmarks")
    print(f"Hardware: {hardware}")
    print(f"Model:    {model}")
    print(f"{'='*42}\n")

    results = []
    for BenchmarkClass in DEEPEVAL_BENCHMARKS:
        benchmark_instance = BenchmarkClass()
        print(f"\n--- Running DeepEval: {benchmark_instance.name} ---")
        try:
            res = benchmark_instance.run(model=model, hardware=hardware)
            results.append(res)
            print(f"Score: {res.get('score', 0)}")
        except Exception as e:
            print(f"[-] Error running {benchmark_instance.name}: {e}")

    safe_model = model.replace(":", "_").replace("/", "_")
    safe_hw = hardware.split()[0].lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    filepath = Path("results") / f"deepeval_{safe_model}_{safe_hw}_{timestamp}.json"
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    print(f"\n[+] DeepEval results saved to {filepath}")

def main():
    print("==================================================")
    print("      Ollama Academic Benchmark Suite (Local)     ")
    print("==================================================\n")

    check_ollama_status()

    try:
        hardware = select_hardware()
        model = select_model()
        mode = select_mode()
        
        if mode in [1, 3]:
            run_deepeval(hardware=hardware, model=model)
            
        if mode in [2, 3]:
            # This triggers existing runner logic bound to ALL_BENCHMARKS
            runner = BenchmarkRunner(hardware=hardware, model=model)
            runner.run()
            
    except KeyboardInterrupt:
        print("\n\n[-] Benchmark interrupted by user. Exiting gracefully.")
        sys.exit(0)

if __name__ == "__main__":
    main()