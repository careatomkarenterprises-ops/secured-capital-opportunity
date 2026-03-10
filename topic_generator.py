import random

business_keywords = [
    "business strategy",
    "capital allocation",
    "corporate growth",
    "business risk management",
    "financial planning for companies",
    "raising capital for business",
    "cash flow management",
]

investor_keywords = [
    "personal finance planning",
    "wealth building strategies",
    "long term investing",
    "stock market investment strategy",
    "portfolio diversification",
    "risk management in investing",
]

question_patterns = [
    "How to improve {}",
    "Why {} is important",
    "Common mistakes in {}",
    "Complete guide to {}",
    "Best strategies for {}",
]


def generate_topic():

    category = random.choice(["business", "investor"])

    if category == "business":
        keyword = random.choice(business_keywords)
    else:
        keyword = random.choice(investor_keywords)

    pattern = random.choice(question_patterns)

    title = pattern.format(keyword.title())

    description = f"Educational guide explaining {keyword} and practical strategies people should understand."

    return {
        "title": title,
        "description": description
    }
