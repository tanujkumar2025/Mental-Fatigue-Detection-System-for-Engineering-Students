def analyze_sentiment(text):

    text = text.lower()

    negative_words = [
        "stress",
        "tired",
        "exhausted",
        "pressure",
        "overwhelmed"
    ]

    positive_words = [
        "happy",
        "good",
        "relaxed",
        "motivated"
    ]

    for word in negative_words:
        if word in text:
            return "Negative"

    for word in positive_words:
        if word in text:
            return "Positive"

    return "Neutral"