import sys
import ollama
from config.hardware import HARDWARE_MACHINES
from config.models import ALL_MODELS
from core.runner import BenchmarkRunner

def check_ollama_status():
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

def main():
    print("==================================================")
    print("      Ollama Academic Benchmark Suite (Local)     ")
    print("==================================================\n")

    check_ollama_status()

    try:
        hardware = select_hardware()
        model = select_model()
        runner = BenchmarkRunner(hardware=hardware, model=model)
        runner.run()
    except KeyboardInterrupt:
        print("\n\n[-] Benchmark interrupted by user. Exiting gracefully.")
        sys.exit(0)

if __name__ == "__main__":
    main()