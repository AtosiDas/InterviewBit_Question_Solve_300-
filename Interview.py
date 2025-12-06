def classifier(text: str) -> str:
    pos = 0
    neg = 0

    #split the text:
    text = text.split()

    for txt in text:
        if txt in ["Good", "Great"]:
            pos += 1
        if txt in ["Bad", "Poor"]:
            neg += 1
        
    if pos > neg:
        return "positive"
    elif pos < neg:
        return "negative"
    else:
        return "neutral"   