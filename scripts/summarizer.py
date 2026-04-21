def summarize(text):
    if not text:
        return "No summary"

    sentences = text.split(". ")
    return ". ".join(sentences[:2]) + "."
