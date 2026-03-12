#!/usr/bin/env python3
"""
Advanced Auto Blog Generator - Humanized Version
Generates structured financial education articles with reduced AI footprint
"""

import sys
import os
import random
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from file_manager import FileManager


# ----------------------------
# Enhanced Topic generation with more variety
# ----------------------------

business_keywords = [
    "capital allocation strategies",
    "business growth frameworks",
    "corporate financial planning systems",
    "cash flow optimization techniques",
    "raising capital for expansion",
    "business risk management approaches",
    "merger integration planning",
    "corporate restructuring methods",
    "strategic financial forecasting"
]

investor_keywords = [
    "portfolio diversification methods",
    "long term wealth building",
    "retirement planning strategies",
    "stock market analysis techniques",
    "financial risk management",
    "asset allocation models",
    "dividend growth investing",
    "value investing principles",
    "market cycle analysis"
]

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
    "Beyond Basics: {}"
]


def generate_topic():
    """Generate varied topics with seasonal awareness"""
    
    # Add seasonal topics based on current month
    current_month = datetime.now().month
    if current_month == 3:  # Financial year end
        seasonal_keywords = [
            "tax planning before March 31",
            "financial year end portfolio review",
            "last minute investment strategies"
        ]
        if random.random() < 0.3:  # 30% chance of seasonal topic
            keyword = random.choice(seasonal_keywords)
            category_display = "Seasonal Planning"
            title = random.choice(title_patterns).format(keyword.title())
            description = f"As the financial year ends, understanding {keyword} becomes crucial for smart financial planning."
            return title, description, category_display

    category = random.choice(["business", "investor"])

    if category == "business":
        keyword = random.choice(business_keywords)
        category_display = "Business Strategy"
    else:
        keyword = random.choice(investor_keywords)
        category_display = "Investment Education"

    # More varied title construction
    pattern = random.choice(title_patterns)
    if "{}" in pattern:
        title = pattern.format(keyword.title())
    else:
        title = f"{keyword.title()}: A Practical Guide"

    # Varied descriptions
    descriptions = [
        f"This guide explores the fundamentals of {keyword} and how successful practitioners apply these principles.",
        f"Discover practical insights on {keyword} that can help you make better financial decisions.",
        f"A comprehensive look at {keyword} and its role in modern financial planning.",
        f"Learn how {keyword} can transform your approach to financial management."
    ]
    description = random.choice(descriptions)

    return title, description, category_display


# ----------------------------
# Expanded frameworks with more variety
# ----------------------------

frameworks = [
    """
    <div class="knowledge-box">
    <strong>Framework: 60-30-10 Diversification Model</strong>
    <ul>
    <li>60% Core assets such as diversified equities or index funds</li>
    <li>30% Stability assets like bonds or income generating instruments</li>
    <li>10% Opportunistic investments for higher growth potential</li>
    </ul>
    </div>
    """,
    
    """
    <div class="knowledge-box">
    <strong>Framework: Core Satellite Investment Strategy</strong>
    <ul>
    <li>Core holdings provide stability and long term growth</li>
    <li>Satellite investments capture tactical opportunities</li>
    <li>Periodic rebalancing maintains portfolio discipline</li>
    </ul>
    </div>
    """,
    
    """
    <div class="knowledge-box">
    <strong>Framework: The Bucket Approach</strong>
    <ul>
    <li>Bucket 1: Short-term liquidity (6-12 months expenses)</li>
    <li>Bucket 2: Medium-term growth (3-7 year horizon)</li>
    <li>Bucket 3: Long-term wealth building (10+ years)</li>
    </ul>
    </div>
    """,
    
    """
    <div class="knowledge-box">
    <strong>Framework: Risk-Adjusted Return Model</strong>
    <ul>
    <li>Calculate risk tolerance before allocation</li>
    <li>Match assets to risk capacity</li>
    <li>Monitor Sharpe ratio for efficiency</li>
    </ul>
    </div>
    """,
    
    """
    <div class="knowledge-box">
    <strong>Framework: The Pyramid Principle</strong>
    <ul>
    <li>Base: Safety (fixed deposits, bonds, cash)</li>
    <li>Middle: Growth (equities, mutual funds)</li>
    <li>Top: Speculative (high-risk opportunities)</li>
    </ul>
    </div>
    """
]

# Multiple author perspectives to rotate
author_perspectives = [
    """
    <p><strong>Experience Perspective:</strong> Based on more than 14 years of
    market observation, one pattern stands out: the investors who succeed long-term
    aren't the ones who chase quick returns, but those who maintain discipline
    through market cycles.</p>
    """,
    
    """
    <p><strong>What I've Learned:</strong> After advising over 200 clients through
    multiple market cycles, I've found that the biggest gap between theory and
    practice is emotional discipline. The best strategy fails if you can't stick
    to it during volatility.</p>
    """,
    
    """
    <p><strong>From the Trenches:</strong> A common thread among successful
    investors I've worked with is their focus on process over outcome. They
    consistently apply their framework and let results follow naturally.</p>
    """,
    
    """
    <p><strong>Market Wisdom:</strong> In 15+ years of navigating Indian markets,
    I've learned that patience beats prediction. The investors who try to time
    the market rarely beat those who stay invested through cycles.</p>
    """
]

# Multiple example variations
example_variations = [
    """
    <h2>{example_head}</h2>
    <p>Consider a professional earning ₹15 lakhs annually, looking to build long-term wealth.</p>
    <ul>
    <li>₹6,00,000 in diversified equity funds (growth focus)</li>
    <li>₹3,00,000 in debt instruments (stability)</li>
    <li>₹1,50,000 in international ETFs (geographic diversification)</li>
    <li>₹50,000 in liquid funds (emergency access)</li>
    </ul>
    <p>This allocation provides growth potential while maintaining stability.</p>
    """,
    
    """
    <h2>{example_head}</h2>
    <p>A mid-sized manufacturing company with ₹2 crore surplus needed a capital allocation strategy.</p>
    <ul>
    <li>₹80 lakhs in business expansion (CAPEX)</li>
    <li>₹50 lakhs in liquid reserves (working capital)</li>
    <li>₹40 lakhs in diversified investments</li>
    <li>₹30 lakhs in debt reduction</li>
    </ul>
    <p>The balanced approach supported growth while maintaining safety.</p>
    """,
    
    """
    <h2>{example_head}</h2>
    <p>A family office with ₹5 crore to deploy used this structured approach:</p>
    <ul>
    <li>₹2 crore in blue-chip equities (core holdings)</li>
    <li>₹1.5 crore in real estate investment trusts</li>
    <li>₹1 crore in fixed income instruments</li>
    <li>₹50 lakhs in alternative investments</li>
    </ul>
    <p>Multi-asset diversification reduced overall portfolio volatility.</p>
    """
]

# Mistake variations
mistake_variations = [
    [
        "Concentrating too much capital in a single asset",
        "Chasing past performance without research",
        "Ignoring risk management fundamentals",
        "Making emotional decisions during volatility"
    ],
    [
        "Starting without a clear financial plan",
        "Overlooking tax implications",
        "Neglecting regular portfolio reviews",
        "Following market rumors without verification"
    ],
    [
        "Investing without understanding the asset",
        "Trying to time market peaks and bottoms",
        "Ignoring the impact of inflation",
        "Taking excessive leverage"
    ]
]

# ----------------------------
# Article generator with more variation
# ----------------------------

def generate_educational_content(title, description, category):
    """Generate varied, human-like educational content"""
    
    # More varied heading options
    intro_heads = [
        "Introduction",
        "Understanding the Landscape",
        f"What You Need to Know About {title}",
        "Setting the Context",
        "Why This Matters Now"
    ]
    
    concept_heads = [
        "The Core Concept",
        f"What Is {title}?",
        "Understanding the Fundamentals",
        "Key Principles Explained",
        "Breaking It Down"
    ]
    
    importance_heads = [
        "Why This Matters",
        "The Strategic Importance",
        "Impact on Financial Decisions",
        "Real-World Relevance",
        "What's at Stake"
    ]
    
    strategy_heads = [
        "Practical Approaches",
        "How to Apply This",
        "Implementation Strategies",
        "Making It Work",
        "Actionable Steps"
    ]
    
    example_heads = [
        "Real-World Example",
        "Practical Scenario",
        "Case Study",
        "How It Works in Practice",
        "A Concrete Illustration"
    ]
    
    mistake_heads = [
        "Common Pitfalls to Avoid",
        "Mistakes People Make",
        "What Not to Do",
        "Avoiding Common Errors",
        "Learning from Others"
    ]
    
    conclusion_heads = [
        "Key Takeaways",
        "Moving Forward",
        "Final Thoughts",
        "Putting It All Together",
        "Next Steps"
    ]
    
    # Get current date for freshness
    current_year = datetime.now().year
    current_month = datetime.now().strftime("%B")
    
    # Dynamic intro based on category
    if category == "Business Strategy":
        intro = f"""
        <h2>{random.choice(intro_heads)}</h2>
        <p>{description}</p>
        <p>In {current_month} {current_year}, businesses face unique challenges in {title.lower()}. 
        Market conditions, regulatory changes, and economic shifts all play a role in shaping 
        effective strategies.</p>
        """
    else:
        intro = f"""
        <h2>{random.choice(intro_heads)}</h2>
        <p>{description}</p>
        <p>As we navigate {current_month} {current_year}, investors are increasingly focused on 
        {title.lower()}. Understanding these concepts helps build long-term financial resilience.</p>
        """
    
    concept = f"""
    <h2>{random.choice(concept_heads)}</h2>
    <p>{title} refers to a structured approach used by experienced professionals when making 
    financial decisions. Rather than relying on intuition alone, it involves systematic evaluation 
    of multiple factors including market conditions, risk tolerance, and long-term objectives.</p>
    """
    
    importance = f"""
    <h2>{random.choice(importance_heads)}</h2>
    <ul>
    <li>Helps reduce unnecessary financial risk exposure</li>
    <li>Improves long-term portfolio resilience</li>
    <li>Encourages disciplined, systematic planning</li>
    <li>Supports better capital allocation decisions</li>
    </ul>
    """
    
    strategies = f"""
    <h2>{random.choice(strategy_heads)}</h2>
    <p>Successful professionals apply structured frameworks rather than relying on guesswork. 
    Here's a proven approach used by many in the field:</p>
    {random.choice(frameworks)}
    """
    
    # Pick a random example variation
    example_template = random.choice(example_variations)
    example = example_template.format(example_head=random.choice(example_heads))
    
    # Pick random mistake list
    mistake_list = random.choice(mistake_variations)
    mistakes_html = ""
    for mistake in mistake_list:
        mistakes_html += f"<li>{mistake}</li>"
    
    mistakes = f"""
    <h2>{random.choice(mistake_heads)}</h2>
    <ul>
    {mistakes_html}
    </ul>
    """
    
    # Rotate author perspectives
    perspective = f"""
    <h2>From Experience</h2>
    {random.choice(author_perspectives)}
    """
    
    conclusion = f"""
    <h2>{random.choice(conclusion_heads)}</h2>
    <p>{title} remains relevant for both individual investors and business decision makers. 
    Developing a structured understanding of these principles can improve long-term outcomes.</p>
    <p>Remember that while educational content provides valuable frameworks, each financial 
    decision should be evaluated within its specific context and personal circumstances.</p>
    """
    
    # Dynamic FAQ
    faq = f"""
    <h2>Frequently Asked Questions</h2>
    
    <h3>How does {title.lower()} apply to my situation?</h3>
    <p>The principles of {title.lower()} can be adapted to various financial situations. 
    The key is understanding your specific goals, risk tolerance, and time horizon.</p>
    
    <h3>What's the biggest misconception about {title.lower()}?</h3>
    <p>Many people think it's about finding a perfect formula, but in reality, it's about 
    maintaining consistency and discipline through market cycles.</p>
    
    <h3>How often should I review my {title.lower()} approach?</h3>
    <p>Most professionals recommend quarterly reviews for active strategies and annual reviews 
    for longer-term passive approaches. However, major life changes warrant immediate review.</p>
    """
    
    # Assemble sections in varied order
    sections = [
        intro,
        concept,
        importance,
        strategies,
        example,
        mistakes,
        perspective,
        conclusion,
        faq
    ]
    
    # Shuffle but keep intro and conclusion at ends? Let's shuffle fully for more variety
    random.shuffle(sections)
    
    # But ensure FAQ isn't first (optional)
    if sections[0] == faq:
        sections[0] = intro
        sections[-1] = faq
    
    return "".join(sections)


# ----------------------------
# Main runner - unchanged
# ----------------------------

def main():

    fm = FileManager()

    articles_per_run = 3

    print(f"🚀 Generating {articles_per_run} articles")

    for i in range(articles_per_run):

        try:

            title, description, category = generate_topic()

            print(f"📝 Creating article: {title}")

            content = generate_educational_content(title, description, category)

            read_time = random.randint(6, 9)

            slug = fm.save_blog_post(
                title=title,
                content=content,
                category=category,
                read_time=read_time,
                author_specialization="Business Advisory"
            )

            print(f"✅ Generated: {slug}.html")

        except Exception as e:

            print(f"⚠️ Error: {str(e)}")

    fm.generate_sitemap()

    print("✅ Blog generation complete")


if __name__ == "__main__":
    main()
