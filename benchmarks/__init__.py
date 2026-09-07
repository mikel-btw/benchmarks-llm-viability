from .mmlu import MMLUBenchmark
from .gsm8k import GSM8KBenchmark
from .hellaswag import HellaSwagBenchmark
from .truthfulqa import TruthfulQABenchmark
from .arc_challenge import ARCChallengeBenchmark

ALL_BENCHMARKS = [
    MMLUBenchmark(),
    GSM8KBenchmark(),
    HellaSwagBenchmark(),
    TruthfulQABenchmark(),
    ARCChallengeBenchmark(),
]
