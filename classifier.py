import re

KEYWORDS = {
    "bug": ["error", "crash", "broken", "не работает", "ошибка", "баг"],
    "feature": ["add", "feature", "would like", "хочу", "добавьте", "фича"],
    "praise": ["love", "great", "awesome", "спасибо", "нравится", "круто"],
    "complaint": ["hate", "terrible", "slow", "медленно", "ужасно", "плохо"],
}

NEGATIVE = ["bad", "slow", "broken", "hate", "плохо", "ужасно", "медленно"]
POSITIVE = ["love", "great", "awesome", "нравится", "круто", "спасибо"]

def classify(text):
    text_l = text.lower()
    scores = {cat: 0 for cat in KEYWORDS}
    for cat, words in KEYWORDS.items():
        for w in words:
            if w in text_l:
                scores[cat] += 1
    category = max(scores, key=scores.get) if any(scores.values()) else "other"

    pos = sum(1 for w in POSITIVE if w in text_l)
    neg = sum(1 for w in NEGATIVE if w in text_l)
    sentiment = "positive" if pos > neg else "negative" if neg > pos else "neutral"

    return {"category": category, "sentiment": sentiment, "scores": scores}
