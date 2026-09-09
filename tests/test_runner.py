import unittest
from unittest.mock import patch
from core.metrics import InferenceMetrics
from benchmarks import ALL_BENCHMARKS

class TestBenchmarkSuite(unittest.TestCase):
    def test_benchmark_prompt_counts(self):
        for benchmark in ALL_BENCHMARKS:
            prompts = benchmark.get_prompts()
            self.assertEqual(len(prompts), 5, f"{benchmark.name} does not have 5 prompts")

    @patch("ollama.chat")
    def test_metrics_measure_stream(self, mock_chat):

        mock_chat.return_value = iter([
            {"message": {"content": "Hello"}},
            {"message": {"content": " world!"}, "eval_count": 2},
        ])
        
        metrics = InferenceMetrics.measure_stream_response("llama3.2:1b", "Test prompt")
        
        self.assertEqual(metrics["response"], "Hello world!")
        self.assertIn("ttft_seconds", metrics)
        self.assertIn("total_time_seconds", metrics)
        self.assertIn("tokens_per_second", metrics)
        self.assertIn("ram_used_mb", metrics)

if __name__ == "__main__":
    unittest.main()