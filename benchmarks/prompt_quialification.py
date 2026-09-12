class PromptQualificationBenchmark:
    name = "Prompt Qualification"

    def get_prompts(self) -> list[str]:
        return [
            "Explica qué es un agujero negro en exactamente tres viñetas.",
            "Resume el siguiente texto en una oración: El Imperio Incaico fue el mayor imperio en la América precolombina. Su centro administrativo, político y militar estaba en la ciudad del Cusco, y surgió en las tierras altas del Perú en algún momento a principios del siglo XIII.",
            "Si Juan es más alto que Pedro, y Pedro es más alto que María, ¿quién es el más bajo de los tres?",
            "Si compro 3 manzanas por $2 cada una y pago con un billete de $10, ¿cuánto cambio recibo?",
            "¿Cuál es la capital de Australia y en qué año se fundó?",
            "Actúa como un profesor de primaria y explica el ciclo del agua de forma sencilla.",
            "Explica el concepto de 'garbage collection' en programación, usando términos técnicos en inglés pero explicando en español.",
            "¿Qué banco es mejor para sentarse?",
            "Escribe los pros y los contras de los vehículos eléctricos en una tabla Markdown.",
            "Define la inteligencia artificial en una sola oración."
        ]