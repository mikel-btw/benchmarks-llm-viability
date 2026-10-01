# LLM Viability Benchmark

Sistema de benchmarking para evaluar la viabilidad de ejecutar modelos de lenguaje (LLMs) de forma local en computadores modestos, midiendo velocidad de inferencia y calidad de respuesta. Proyecto del CIAI (Centro de Inteligencia Artificial e Innovacion), Colombia.

Corre sobre [Ollama](https://ollama.com). No usa APIs externas.

## Que mide

- Velocidad: tiempo al primer token, tiempo total, tokens por segundo y RAM usada.
- Calidad: benchmarks automaticos con deepeval (MMLU, HellaSwag, TruthfulQA) y un benchmark manual de 10 prompts en espanol (Prompt Qualification).

GSM8K y ARC Challenge estan deshabilitados por un bug de deepeval 4.2.3. Ver `src/benchmarks/_disabled/README.txt`.

## Instalacion

Requiere Python 3.10 o superior y Ollama instalado y corriendo (`ollama serve`).

```bash
git clone https://github.com/mikel-btw/benchmarks-llm-viability.git
cd benchmarks-llm-viability
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

Los comandos para descargar los modelos estan en la documentacion (`docs/index.html`, seccion Instalacion).

## Uso

```bash
python3 src/benchmarkcli.py
```

El CLI pide la maquina, el modelo y el benchmark. Los resultados se guardan como JSON en `results/`.

## Tests

```bash
pip install -r requirements-dev.txt
pytest
```

## Estructura

```
src/
  benchmarkcli.py     Punto de entrada
  config/             Maquinas y modelos
  core/               Metricas, scorer, recorder y runner
  benchmarks/         Benchmarks (deepeval y manual)
  tests/              Tests unitarios
docs/                 Pagina de documentacion (HTML estatico)
results/              Salida en JSON (no versionada)
```

## Autor

Miguel Angel Osorio Orduz, mangelosorio@uts.edu.co

## Licencia

Ver `LICENSE.md`.
