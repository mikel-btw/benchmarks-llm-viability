class PromptQualificationBenchmark:
    name = "Prompt Qualification"

    def get_prompts(self) -> list[str]:
        return [
            # 1. Instruction following
            "Explica qué es un agujero negro en exactamente tres viñetas.",
            # 2. Summarization
            "Resume el siguiente texto en una oración: El Imperio Incaico fue el mayor imperio en la América precolombina. Su centro administrativo, político y militar estaba en la ciudad del Cusco, y surgió en las tierras altas del Perú en algún momento a principios del siglo XIII.",
            # 3. Logical reasoning
            "Si Juan es más alto que Pedro, y Pedro es más alto que María, ¿quién es el más bajo de los tres?",
            # 4. Math word problem
            "Si compro 3 manzanas por $2 cada una y pago con un billete de $10, ¿cuánto cambio recibo?",
            # 5. Factual knowledge
            "¿Cuál es la capital de Australia y en qué año se fundó?",
            # 6. Role following
            "Actúa como un profesor de primaria y explica el ciclo del agua de forma sencilla.",
            # 7. Multilingual code-switching
            "Explica el concepto de 'garbage collection' en programación, usando términos técnicos en inglés pero explicando en español.",
            # 8. Handling ambiguity
            "¿Qué banco es mejor para sentarse?",
            # 9. Structured response
            "Escribe los pros y los contras de los vehículos eléctricos en una tabla Markdown.",
            # 10. Conciseness
            "Define la inteligencia artificial en una sola oración."
        ]