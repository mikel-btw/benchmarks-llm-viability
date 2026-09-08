class MMLUBenchmark:
    name = "MMLU"

    def get_prompts(self) -> list[str]:
        return [
            "Who wrote 'One Hundred Years of Solitude'?",
            "What is the capital of Mongolia?",
            "What is the chemical symbol for gold?",
            "Who painted the Mona Lisa?",
            "What is the largest planet in our solar system?",
        ]