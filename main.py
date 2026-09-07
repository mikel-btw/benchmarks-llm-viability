import sys
from config import HARDWARE_MACHINES
from models.model_list import ALL_MODELS
from runner.benchmark_runner import BenchmarkRunner


def select_hardware() -> str:
    print("\nSelect Hardware Machine Identifier:")
    for key, name in HARDWARE_MACHINES.items():
        print(f"  [{key}] {name}")
    
    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice in HARDWARE_MACHINES:
            return HARDWARE_MACHINES[choice]
        print("Invalid selection. Please choose a valid hardware option.")


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
        print("Invalid model selection. Please pick a number from the list.")


def main():
    print("==================================================")
    print("      Ollama Academic Benchmark Suite (Local)     ")
    print("==================================================")

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
