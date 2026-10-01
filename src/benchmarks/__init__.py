from .mmlu import MMLUBenchmark
from .gsm8k import GSM8KBenchmark
from .hellaswag import HellaSwagBenchmark
from .truthfulqa import TruthfulQABenchmark
from .arc_challenge import ARCChallengeBenchmark
from .prompt_qualification import PromptQualificationBenchmark

DEEPEVAL_BENCHMARKS = [
    MMLUBenchmark,
    GSM8KBenchmark,
    HellaSwagBenchmark,
    TruthfulQABenchmark,
    ARCChallengeBenchmark
]

MANUAL_BENCHMARKS = [
    PromptQualificationBenchmark()
]

# Exported explicitly to preserve backwards compatibility with core/runner.py 
# without altering existing runner logic.
ALL_BENCHMARKS = MANUAL_BENCHMARKS