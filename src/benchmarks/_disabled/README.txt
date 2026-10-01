GSM8K y ARC Challenge: deshabilitados.

deepeval 4.2.3 referencia sus datasets en HuggingFace con URIs sin namespace
("gsm8k" en lugar de "openai/gsm8k", "ai2_arc" en lugar de "allenai/ai2_arc").
HuggingFace rechaza esas URIs y ambos benchmarks fallan antes de evaluar.

Los archivos se conservan aqui como referencia. No estan registrados en
benchmarks/__init__.py ni aparecen en el menu del CLI.
