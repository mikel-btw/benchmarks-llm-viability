import time
import psutil
from typing import Dict, Any, Generator
import ollama

class InferenceMetrics:
    @staticmethod
    def measure_stream_response(model: str, prompt: str) -> Dict[str, Any]:
        process = psutil.Process()
        start_time = time.perf_counter()
        first_token_time = None
        full_response = ""
        eval_count = 0

        stream: Generator = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        for chunk in stream:
            if first_token_time is None:
                first_token_time = time.perf_counter()
            
            content = chunk.message.content if hasattr(chunk, 'message') else ""
            full_response += content

            if hasattr(chunk, 'eval_count') and chunk.eval_count:
                eval_count = chunk.eval_count

        end_time = time.perf_counter()
        ram_used_mb = int(process.memory_info().rss / (1024 * 1024))
        ttft_seconds = round((first_token_time - start_time), 2) if first_token_time else 0.0
        total_time_seconds = round((end_time - start_time), 2)

        if eval_count == 0 and full_response:
            eval_count = len(full_response.split())

        gen_duration = total_time_seconds - ttft_seconds
        if gen_duration > 0 and eval_count > 0:
            tokens_per_second = round(eval_count / gen_duration, 1)
        elif total_time_seconds > 0 and eval_count > 0:
            tokens_per_second = round(eval_count / total_time_seconds, 1)
        else:
            tokens_per_second = 0.0

        return {
            "response": full_response,
            "ttft_seconds": ttft_seconds,
            "total_time_seconds": total_time_seconds,
            "tokens_per_second": tokens_per_second,
            "ram_used_mb": ram_used_mb,
        }