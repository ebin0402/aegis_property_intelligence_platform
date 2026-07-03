from app.ai.llm import LLMClient

llm = LLMClient()

def analyse_opportunity(property_data):
    prompt = f"""
    You are a property investment expert.

    Analyse this property:
    {property_data}

    Provide:
    - Investment summary
    - Risks
    - Opportunities
    - Recommendation
    """

    return llm.generate(prompt)
