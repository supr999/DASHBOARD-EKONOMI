def analyze_sentiment(text):
    text = text.lower()

    bullish = ["strong", "rise", "increase", "hawkish"]
    bearish = ["weak", "fall", "recession", "dovish"]

    score = 0

    for w in bullish:
        if w in text:
            score += 1

    for w in bearish:
        if w in text:
            score -= 1

    if score > 0:
        return "BULLISH 📈"
    elif score < 0:
        return "BEARISH 📉"
    return "NEUTRAL ⚖️"
