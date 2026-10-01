from .mmlu import MMLUBenchmark
from .hellaswag import HellaSwagBenchmark
from .truthfulqa import TruthfulQABenchmark
from .prompt_qualification import PromptQualificationBenchmark

DEEPEVAL_BENCHMARKS = [
    MMLUBenchmark,
    HellaSwagBenchmark,
    TruthfulQABenchmark,
]

MANUAL_BENCHMARKS = [
    PromptQualificationBenchmark()
]
