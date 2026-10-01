VALID_SCORES = [1.0, 0.7, 0.5, 0.0]

class ManualScorer:
    @staticmethod
    def get_score() -> float:
        while True:
            try:
                raw_input = input("Enter Score (1.0 / 0.7 / 0.5 / 0.0): ").strip()
                score = float(raw_input)
                if score in VALID_SCORES:
                    return score
                print(f"Invalid score. Choose from {VALID_SCORES}")
            except ValueError:
                print("Invalid numerical input. Please enter a valid float score.")