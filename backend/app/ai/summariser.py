from app.ai.llm import LLMClient

llm = LLMClient()

def summarise_property(property_data: dict):
    prompt = f"""
    Summarise this property for a buyer:
    Location: {property_data.get('location')}
    Price: {property_data.get('price')}
    Bedrooms: {property_data.get('bedrooms')}
    """

    return llm.generate(prompt)
