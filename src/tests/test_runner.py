import unittest
from unittest.mock import patch
from core.metrics import InferenceMetrics
from benchmarks import DEEPEVAL_BENCHMARKS, MANUAL_BENCHMARKS
from benchmarks.deepeval_llm import OllamaDeepEvalLLM

class MockMessage:
    def __init__(self, content):
        self.content = content

class MockChunk:
    def __init__(self, content, eval_count=None):
        self.message = MockMessage(content)
        self.eval_count = eval_count

class TestBenchmarkSuite(unittest.TestCase):
    
    def test_manual_benchmark_prompts(self):
        """Verify the Prompt Qualification benchmark contains exactly 10 Spanish prompts."""
        self.assertEqual(len(MANUAL_BENCHMARKS), 1, "Should only be 1 manual benchmark loaded.")
        for benchmark in MANUAL_BENCHMARKS:
            prompts = benchmark.get_prompts()
            self.assertEqual(len(prompts), 10, f"{benchmark.name} does not have 10 prompts")

    def test_deepeval_benchmarks_structure(self):
        """Verify DeepEval benchmarks are correctly loaded and expose the run method."""
        self.assertEqual(len(DEEPEVAL_BENCHMARKS), 5, "There should be exactly 5 DeepEval benchmarks")
        for BenchmarkClass in DEEPEVAL_BENCHMARKS:
            instance = BenchmarkClass()
            self.assertTrue(hasattr(instance, 'run'), f"{instance.name} is missing the 'run' method")

    @patch("ollama.chat")
    def test_metrics_measure_stream(self, mock_chat):
        """Test inference metric capture and timing structures for manual mode."""
        # Mock the generator stream returned by ollama.chat(stream=True) using object attributes
        mock_chat.return_value = iter([
            MockChunk("Hola"),
            MockChunk(" mundo!", eval_count=2),
        ])
        
        metrics = InferenceMetrics.measure_stream_response("llama3.2:1b", "Test prompt")
        
        self.assertEqual(metrics["response"], "Hola mundo!")
        self.assertIn("ttft_seconds", metrics)
        self.assertIn("total_time_seconds", metrics)
        self.assertIn("tokens_per_second", metrics)
        self.assertIn("ram_used_mb", metrics)

    @patch("ollama.chat")
    def test_deepeval_llm_wrapper(self, mock_chat):
        """Test the DeepEval wrapper properly routes calls to Ollama."""
        # Mock a standard (non-streamed) response from Ollama using object attributes
        mock_chat.return_value = MockChunk("Respuesta simulada para DeepEval")
        
        llm = OllamaDeepEvalLLM(model="llama3.2:1b")
        response = llm.generate("Test prompt")
        
        self.assertEqual(response, "Respuesta simulada para DeepEval")
        self.assertEqual(llm.get_model_name(), "llama3.2:1b")
        
        # Verify it called the ollama client with the correct payload
        mock_chat.assert_called_once_with(
            model="llama3.2:1b",
            messages=[{"role": "user", "content": "Test prompt"}]
        )

if __name__ == "__main__":
    unittest.main()