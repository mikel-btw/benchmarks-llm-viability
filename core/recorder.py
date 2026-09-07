import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

class ResultRecorder:
    @staticmethod
    def save(hardware: str, model: str, results: List[Dict[str, Any]]) -> None:
        safe_model = model.replace(":", "_").replace("/", "_")
        safe_hw = hardware.split()[0].lower()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        filepath = RESULTS_DIR / f"{safe_model}_{safe_hw}_{timestamp}.json"

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)

        print(f"\n[+] Results successfully saved to {filepath}")