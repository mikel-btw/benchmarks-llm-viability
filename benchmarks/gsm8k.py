class GSM8KBenchmark:
    name = "GSM8K"

    def get_prompts(self) -> list[str]:
        return [
            "If I have 5 apples and buy 3 more, how many apples do I have in total?",
            "A train travels at 60 km/h for 2.5 hours. What distance does it cover?",
            "If 3 shirts cost $45, how much do 5 shirts cost?",
            "A rectangle has length 8 cm and width 5 cm. What is its area?",
            "If I have 12 cookies and give 1/3 away, how many do I have left?",
        ]