#!/usr/bin/env python3
"""
Advanced Auto Blog Generator
Generates structured financial education articles
"""

import sys
import os
import random
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from file_manager import FileManager


# ----------------------------
# Topic generation
# ----------------------------

business_keywords = [
    "capital allocation",
    "business growth strategy",
    "corporate financial planning",
    "cash flow management",
    "raising capital for business",
    "business risk management"
]

investor_keywords = [
    "portfolio diversification",
    "long term investing",
    "wealth building strategies",
    "stock market investment planning",
    "financial risk management",
    "asset allocation strategy"
]

title_patterns = [
    "Complete Guide to {}",
    "Understanding {} for Beginners",
    "How {} Shapes Long Term Financial Success",
    "Common Mistakes in {}",
    "Why {} Matters in Modern Investing"
]


def generate_topic():

    category = random.choice(["business", "investor"])

    if category == "business":
        keyword = random.choice(business_keywords)
        category_display = "Business Strategy"
    else:
        keyword = random.choice(investor_keywords)
        category_display = "Investment Education"

    title = random.choice(title_patterns).format(keyword.title())

    description = f"This guide explores the fundamentals of {keyword} and explains how individuals, investors, and businesses approach this concept in practical financial decision making."

    return title, description, category_display


# ----------------------------
# Article generator
# ----------------------------

def generate_educational_content(title, description, category):

    intro_heads = [
        "Introduction",
        "Overview",
        "Understanding the Background",
        "Context and Importance"
    ]

    concept_heads = [
        "Understanding the Core Concept",
        f"What Is {title}",
        "Key Principles Behind the Idea"
    ]

    importance_heads = [
        "Why This Concept Matters",
        "Importance in Financial Planning",
        "Strategic Relevance"
    ]

    strategy_heads = [
        "Practical Strategies",
        "Implementation Framework",
        "Professional Approaches"
    ]

    example_heads = [
        "Real World Example",
        "Practical Scenario",
        "Illustrative Case Study"
    ]

    mistake_heads = [
        "Common Mistakes Investors Make",
        "Typical Pitfalls",
        "Misconceptions to Avoid"
    ]

    perspective_heads = [
        "Author Perspective",
        "Market Experience Insight",
        "Professional Observation"
    ]

    conclusion_heads = [
        "Conclusion",
        "Key Takeaways",
        "Final Thoughts"
    ]

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
        """

    ]

    author_block = """
    <p><strong>Experience Perspective:</strong> Based on more than 14 years of
    market observation and financial analysis, one of the most common mistakes
    among new investors is concentrating capital in a very limited number of
    assets. While concentrated bets may produce short term gains, long term
    financial stability typically requires structured capital allocation and
    disciplined portfolio planning.</p>
    """

    intro = f"""
    <h2>{random.choice(intro_heads)}</h2>

    <p>{description}</p>

    <p>Financial markets and business environments are constantly evolving.
    Understanding the principles behind this concept allows investors and
    entrepreneurs to make more informed strategic decisions.</p>
    """

    concept = f"""
    <h2>{random.choice(concept_heads)}</h2>

    <p>{title} refers to a structured approach used by investors and business
    leaders when making capital allocation or strategic financial decisions.</p>

    <p>Instead of relying on intuition alone, experienced professionals often
    evaluate multiple factors including market conditions, economic trends,
    risk tolerance, and long term objectives.</p>
    """

    importance = f"""
    <h2>{random.choice(importance_heads)}</h2>

    <ul>
    <li>Helps reduce financial risk exposure</li>
    <li>Improves long term portfolio resilience</li>
    <li>Encourages disciplined financial planning</li>
    <li>Supports strategic capital allocation</li>
    </ul>
    """

    strategies = f"""
    <h2>{random.choice(strategy_heads)}</h2>

    <p>Professionals rarely rely on a single investment decision. Instead,
    they apply structured frameworks when evaluating opportunities.</p>

    {random.choice(frameworks)}
    """

    example = f"""
    <h2>{random.choice(example_heads)}</h2>

    <p>Consider an investor allocating ₹10,00,000 in capital.</p>

    <ul>
    <li>₹5,00,000 diversified equity investments</li>
    <li>₹3,00,000 debt or income generating assets</li>
    <li>₹1,50,000 international exposure</li>
    <li>₹50,000 liquidity reserve</li>
    </ul>

    <p>This diversified structure allows the investor to balance growth,
    stability, and flexibility.</p>
    """

    mistakes = f"""
    <h2>{random.choice(mistake_heads)}</h2>

    <ul>
    <li>Concentrating capital in a single asset</li>
    <li>Following market trends without research</li>
    <li>Ignoring long term risk management</li>
    <li>Failing to periodically review financial strategies</li>
    </ul>
    """

    perspective = f"""
    <h2>{random.choice(perspective_heads)}</h2>
    {author_block}
    """

    conclusion = f"""
    <h2>{random.choice(conclusion_heads)}</h2>

    <p>{title} remains an important concept for both individual investors and
    business decision makers. Developing a structured understanding of these
    principles can improve long term financial outcomes.</p>

    <p>Educational content like this helps build awareness, but each financial
    decision should always be evaluated within its specific context.</p>
    """

    faq = f"""
    <h2>Frequently Asked Questions</h2>

    <h3>Why is this concept important for investors?</h3>
    <p>It helps investors manage financial risk and develop more structured
    long term investment strategies.</p>

    <h3>Is this concept useful for business owners?</h3>
    <p>Yes. Many of the same financial principles apply to corporate capital
    allocation and strategic planning.</p>

    <h3>How often should strategies be reviewed?</h3>
    <p>Many professionals recommend periodic reviews depending on market
    conditions and financial objectives.</p>
    """

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

    random.shuffle(sections)

    return "".join(sections)


# ----------------------------
# Main runner
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
