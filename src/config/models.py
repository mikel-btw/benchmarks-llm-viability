from typing import Dict, List

MODEST_HARDWARE_MODELS = [
    "qwen2.5:0.5b",
    "qwen3.5:0.8b",
    "llama3.2:1b",
    "tinyllama:1.1b",
    "deepseek-r1:1.5b",
    "gemma2:2b",
    "llama3.2:3b",
    "qwen2.5:1.5b",
    "phi4-mini:3.8b",
]

LAB_HARDWARE_MODELS = [
    "VIDRAFT/pocket-26b",
    "ministral-3:8b",
    "gemma3:12b",
    "deepseek-r1-distill-qwen:14b",
    "qwen3:30b-a3b-q4_K_M",
]

ALL_MODELS: Dict[str, List[str]] = {
    "Modest Hardware": MODEST_HARDWARE_MODELS,
    "Lab Hardware": LAB_HARDWARE_MODELS,
}
