import random
from datetime import datetime

# ============================================
# BUSINESS TOPICS
# ============================================

business_keywords = [
    "capital allocation strategies",
    "business growth frameworks",
    "corporate financial planning",
    "cash flow optimization techniques",
    "raising capital for business",
    "business risk management approaches",
    "merger integration planning",
    "corporate restructuring methods",
    "strategic financial forecasting",
    "partnership structuring for MSMEs",
    "corporate governance essentials",
    "board structures and composition",
    "business succession planning",
    "operational efficiency improvement",
    "compliance requirements for businesses",
    "GST compliance guide",
    "ROC filing deadlines",
    "company law amendments",
    "ESOP structures explained",
    "business valuation methods"
]

# ============================================
# INVESTOR/STOCK MARKET TOPICS
# ============================================

investor_keywords = [
    "portfolio diversification methods",
    "long term wealth building",
    "retirement planning strategies",
    "stock market analysis techniques",
    "financial risk management",
    "asset allocation models",
    "dividend growth investing",
    "value investing principles",
    "market cycle analysis",
    "technical analysis basics",
    "support and resistance levels",
    "Fibonacci retracement explained",
    "RSI indicator guide",
    "moving average strategies",
    "candlestick patterns explained",
    "FII DII data interpretation",
    "IPO investing strategies",
    "mutual fund selection guide",
    "SIP vs lump sum investing",
    "tax efficient investing"
]

# ============================================
# TITLE PATTERNS
# ============================================

title_patterns = [
    "Complete Guide to {}",
    "Understanding {} for Beginners",
    "How {} Shapes Financial Success",
    "Common Mistakes in {}",
    "Why {} Matters Today",
    "{}: A Practical Approach",
    "The Art of {}",
    "Mastering {}",
    "{} Demystified",
    "Essential {} Strategies",
    "Your {} Roadmap",
    "Beyond Basics: {}",
    "{} Explained Simply",
    "The Science of {}",
    "{}: What You Need to Know"
]

# ============================================
# SEASONAL TOPICS
# ============================================

def get_seasonal_topics():
    """Generate topics based on current season/month"""
    month = datetime.now().month
    current_year = datetime.now().year
    
    # March - Financial year end
    if month == 3:
        return [
            {
                "title": f"Tax Planning Before March 31: Complete Guide for FY{current_year-1}-{current_year}",
                "description": "Last minute tax planning strategies and investment options for the financial year end.",
                "category": "Seasonal Planning"
            },
            {
                "title": f"Financial Year End Portfolio Review: What to Check",
                "description": "Essential steps to review your investment portfolio before the financial year closes.",
                "category": "Portfolio Management"
            }
        ]
    
    # April - New financial year
    elif month == 4:
        return [
            {
                "title": f"New Financial Year {current_year}-{current_year+1}: Investment Planning Guide",
                "description": "Start the new financial year with smart investment planning and goal setting.",
                "category": "Financial Planning"
            },
            {
                "title": f"FY{current_year-1}-{current_year} Tax Filing: Complete Guide",
                "description": "Everything you need to know about filing your income tax returns.",
                "category": "Tax Planning"
            }
        ]
    
    # July-September - Quarterly results
    elif month in [7, 8, 9]:
        return [
            {
                "title": f"Q{1 if month<9 else 2} Earnings Season: How to Analyze Results",
                "description": "Educational guide to understanding company quarterly results and their impact.",
                "category": "Market Analysis"
            },
            {
                "title": "Mid-Year Portfolio Review: Rebalancing Strategies",
                "description": "How to review and rebalance your investment portfolio mid-year.",
                "category": "Portfolio Management"
            }
        ]
    
    # October-December - Festive season
    elif month in [10, 11, 12]:
        return [
            {
                "title": "Diwali Investment Guide: Smart Ways to Invest",
                "description": "Educational guide to making smart investment decisions during the festive season.",
                "category": "Seasonal Planning"
            },
            {
                "title": "Year-End Market Trends: Historical Analysis",
                "description": "Analysis of how markets typically perform in the last quarter of the year.",
                "category": "Market Analysis"
            }
        ]
    
    # January-February - Budget season
    elif month in [1, 2]:
        return [
            {
                "title": f"Union Budget {current_year}: What Investors Should Know",
                "description": "Educational analysis of budget proposals and their potential impact.",
                "category": "Budget Analysis"
            },
            {
                "title": "Pre-Budget Investment Strategies: Historical Perspective",
                "description": "How markets typically behave before and after the budget announcement.",
                "category": "Market Education"
            }
        ]
    
    return []

# ============================================
# MAIN TOPIC GENERATOR
# ============================================

def generate_topic():
    """Generate varied educational topics"""
    
    # 30% chance of seasonal topic
    if random.random() < 0.3:
        seasonal_topics = get_seasonal_topics()
        if seasonal_topics:
            return random.choice(seasonal_topics)
    
    # 50% business topics, 50% investor topics
    if random.random() < 0.5:
        keyword = random.choice(business_keywords)
        category_display = "Business Strategy"
    else:
        keyword = random.choice(investor_keywords)
        category_display = "Investment Education"
    
    # Generate title
    pattern = random.choice(title_patterns)
    if "{}" in pattern:
        title = pattern.format(keyword.title())
    else:
        title = f"{keyword.title()}: A Practical Guide"
    
    # Generate description
    descriptions = [
        f"This educational guide explores {keyword} and how understanding these concepts can help in financial planning.",
        f"Learn about {keyword} in this comprehensive educational article. For learning purposes only.",
        f"A detailed look at {keyword} and its role in modern financial management.",
        f"Discover practical insights on {keyword} in this educational resource.",
        f"Understanding {keyword} is essential for informed decision-making. This guide explains the basics."
    ]
    
    description = random.choice(descriptions)
    
    return {
        "title": title,
        "description": description,
        "category": category_display
    }

# ============================================
# TRENDING TOPIC GENERATOR (FOR MARKET REPORTS)
# ============================================

def generate_trending_topic():
    """Generate trending topics based on current market themes"""
    
    # Mix of evergreen trending topics
    trending_pool = [
        {
            "title": "Why 90% of Traders Lose Money: Educational Analysis",
            "description": "An honest look at trading psychology and common mistakes. For learning only.",
            "category": "Trading Psychology"
        },
        {
            "title": "FII vs DII: Understanding Institutional Money Flows",
            "description": "Educational guide to how foreign and domestic institutions impact markets.",
            "category": "Market Education"
        },
        {
            "title": "Support and Resistance Levels: Complete Guide",
            "description": "Learn how to identify and use support and resistance in technical analysis.",
            "category": "Technical Analysis"
        },
        {
            "title": "Understanding Market Corrections: A Historical Perspective",
            "description": "Educational analysis of market corrections and how they've played out historically.",
            "category": "Market Education"
        },
        {
            "title": "The 17% Factor: Why Most IPO Investors Lose Money",
            "description": "Educational analysis of IPO investing and common pitfalls.",
            "category": "IPO Strategies"
        },
        {
            "title": "Smart Money vs Retail: Understanding Market Dynamics",
            "description": "Educational look at how different market participants behave.",
            "category": "Market Psychology"
        }
    ]
    
    return random.choice(trending_pool)


# For testing
if __name__ == "__main__":
    print("Testing topic generator...")
    for i in range(5):
        topic = generate_topic()
        print(f"\n{i+1}. {topic['title']}")
        print(f"   Category: {topic['category']}")
        print(f"   Desc: {topic['description'][:80]}...")
