class LLMClient:
    """
    Abstraction layer so we can switch between:
    - OpenAI
    - Claude
    - Gemini
    - Local models
    """

    def generate(self, prompt: str) -> str:
        # Placeholder for real LLM integration
        return f"[AI RESPONSE] {prompt}"
