class HellaSwagBenchmark:
    name = "HellaSwag"

    def get_prompts(self) -> list[str]:
        return [
            "The chef prepared the ingredients. Then, he ____.",
            "The baby was crying. The mother ____.",
            "The car wouldn't start. The mechanic ____.",
            "The student studied all night. In the morning, he ____.",
            "The dog saw the mailman. It ____.",
        ]