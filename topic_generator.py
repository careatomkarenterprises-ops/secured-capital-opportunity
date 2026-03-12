import random
from datetime import datetime

# Add seasonal topics based on current events
def get_seasonal_topics():
    month = datetime.now().month
    
    if month in [3, 4]:  # Financial year end
        return [
            "tax planning strategies before March 31",
            "FY26 budget impact on investments",
            "year-end portfolio rebalancing"
        ]
    elif month in [10, 11, 12]:  # Festive season
        return [
            "Diwali portfolio strategies",
            "festive season market trends",
            "Q3 earnings expectations"
        ]
    else:
        return []

def generate_topic():
    categories = {
        "business": [
            "capital allocation strategies",
            "business growth frameworks",
            "cash flow optimization",
            "risk management systems",
            "succession planning",
            "corporate restructuring",
            "merger & acquisition readiness",
            "ESG compliance for SMEs",
            "digital transformation roadmap"
        ],
        "investor": [
            "portfolio diversification",
            "asset allocation models",
            "retirement planning",
            "tax-efficient investing",
            "market cycle analysis",
            "sector rotation strategies",
            "dividend growth investing",
            "value investing principles",
            "technical analysis basics"
        ]
    }
    
    # 70% chance of standard topic, 30% chance of seasonal
    if random.random() < 0.3:
        seasonal = get_seasonal_topics()
        if seasonal:
            category = "investor"  # seasonal tends to be investor-focused
            keyword = random.choice(seasonal)
            return {
                "title": keyword.title(),
                "description": f"As we approach {datetime.now().strftime('%B')}, understanding {keyword} becomes crucial for smart financial planning.",
                "category": "Seasonal Insights"
            }
    
    category = random.choice(list(categories.keys()))
    keyword = random.choice(categories[category])
    
    # More varied title patterns
    patterns = [
        "{}: A Complete Guide",
        "Understanding {}",
        "{} Explained",
        "The Art of {}",
        "Mastering {}",
        "{} Demystified",
        "Your {} Roadmap",
        "Essential {} Strategies",
        "Why {} Matters in {}"
    ]
    
    pattern = random.choice(patterns)
    
    if "{}" in pattern:
        title = pattern.format(keyword.title())
    else:
        title = f"{keyword.title()}: A Practical Guide"
    
    descriptions = [
        f"Discover proven {keyword} techniques used by successful professionals.",
        f"A comprehensive look at {keyword} and how it applies to your financial journey.",
        f"Everything you need to know about {keyword}, explained simply.",
        f"Practical insights on {keyword} from years of market experience."
    ]
    
    category_display = "Business Strategy" if category == "business" else "Investment Education"
    
    return {
        "title": title,
        "description": random.choice(descriptions),
        "category": category_display
    }
