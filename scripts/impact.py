def detect_impact(text):
    text = text.lower()

    if "rate hike" in text:
        return "BULLISH 💵", "BEARISH 🪙"
    if "rate cut" in text:
        return "BEARISH 💵", "BULLISH 🪙"
    if "inflation" in text:
        return "NEUTRAL 💵", "BULLISH 🪙"

    return "NEUTRAL 💵", "NEUTRAL 🪙"
