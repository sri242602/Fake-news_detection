def analyze_news(text, model):
    # Perform NLP analysis
    prediction = model.predict([text])[0]
    probability = model.predict_proba([text]).max()
    
    # Generate explanations
    indicators = {
        'emotional_language': check_emotional_tone(text),
        'source_quality': check_sources(text),
        'fact_consistency': check_facts(text)
    }
    
    return {
        'is_fake': bool(prediction),
        'confidence': float(probability),
        'indicators': indicators
    }
