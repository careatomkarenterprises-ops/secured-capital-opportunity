import random
from datetime import datetime

# Track generated topics to avoid duplicates
_generated_topics = []

def reset_topic_tracker():
    """Reset the tracker at the start of each run"""
    global _generated_topics
    _generated_topics = []

def is_duplicate(title):
    """Check if topic was already generated in this run"""
    global _generated_topics
    # Simple check - if title contains similar keywords
    for existing in _generated_topics:
        # Extract key words from titles (remove common words)
        words1 = set(existing.lower().split())
        words2 = set(title.lower().split())
        # If more than 60% words match, it's duplicate
        if len(words1 & words2) > 3:
            return True
    return False

def add_to_generated(title):
    """Add title to generated list"""
    global _generated_topics
    _generated_topics.append(title)

# Add seasonal topics based on current events
def get_seasonal_topics():
    month = datetime.now().month
    
    if month in [3, 4]:  # Financial year end
        return [
            "tax planning before March 31",
            "financial year end portfolio review",
            "last minute investment strategies"
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
            "portfolio diversification methods",
            "asset allocation models",
            "retirement planning strategies",
            "tax efficient investing",
            "market cycle analysis",
            "sector rotation strategies",
            "dividend growth investing",
            "value investing principles",
            "technical analysis basics"
        ]
    }
    
    max_attempts = 20  # Prevent infinite loop
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        
        # 30% chance of seasonal topic
        if random.random() < 0.3:
            seasonal = get_seasonal_topics()
            if seasonal:
                keyword = random.choice(seasonal)
                title = keyword.title()
                description = f"As we approach {datetime.now().strftime('%B')}, understanding {keyword} becomes crucial for smart financial planning."
                category_display = "Seasonal Planning"
                
                # Check for duplicate
                if not is_duplicate(title):
                    add_to_generated(title)
                    return {
                        "title": title,
                        "description": description,
                        "category": category_display
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
            "Why {} Matters"
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
        
        description = random.choice(descriptions)
        category_display = "Business Strategy" if category == "business" else "Investment Education"
        
        # Check for duplicate
        if not is_duplicate(title):
            add_to_generated(title)
            return {
                "title": title,
                "description": description,
                "category": category_display
            }
    
    # Fallback if all attempts fail
    return {
        "title": "Understanding Financial Markets: A Beginner's Guide",
        "description": "Educational overview of financial markets and investment concepts.",
        "category": "Investment Education"
    }