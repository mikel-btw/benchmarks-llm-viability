class ARCChallengeBenchmark:
    name = "ARC Challenge"

    def get_prompts(self) -> list[str]:
        return [
            "Why do we see lightning before hearing thunder?",
            "What causes the seasons to change?",
            "Why do objects fall to the ground?",
            "What makes the moon shine at night?",
            "Why do we see different constellations at different times of the year?",
        ]