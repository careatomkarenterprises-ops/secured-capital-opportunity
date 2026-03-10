#!/usr/bin/env python3
"""
Advanced auto blog generator
Generates educational financial articles automatically
"""

import sys
import os
import random
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from file_manager import FileManager


# Topic generator (no manual topics needed)
business_keywords = [
    "business strategy",
    "capital allocation",
    "corporate growth planning",
    "cash flow management",
    "raising capital for business",
    "business risk management",
]

investor_keywords = [
    "long term investing",
    "portfolio diversification",
    "wealth building strategies",
    "stock market investment planning",
    "financial risk management",
]

question_patterns = [
    "Complete Guide to {}",
    "How Entrepreneurs Use {}",
    "Common Mistakes in {}",
    "Understanding {} for Beginners",
    "Why {} Matters for Financial Growth"
]


def generate_topic():

    category = random.choice(["business", "investor"])

    if category == "business":
        keyword = random.choice(business_keywords)
        category_display = "Business Strategy"
    else:
        keyword = random.choice(investor_keywords)
        category_display = "Investment Education"

    pattern = random.choice(question_patterns)

    title = pattern.format(keyword.title())

    description = f"This educational guide explains key concepts behind {keyword} and how individuals or businesses can better understand these principles."

    return title, description, category_display


def generate_educational_content(title, description, category):

    intro = f"""
    <h2>Introduction</h2>
    <p>{description}</p>

    <p>This article provides general educational information intended to help readers better understand financial and business concepts.</p>

    <div class="note" style="background:#f1f5f9;padding:20px;border-radius:8px;margin:20px 0;">
    <strong>Educational Purpose:</strong> The information presented here is general in nature and should not be interpreted as financial or investment advice.
    </div>
    """

    body = ""

    sections = [
        "Understanding the Core Concept",
        "Why This Topic Matters",
        "Key Principles and Frameworks",
        "Practical Business Considerations",
        "Common Mistakes People Make",
        "Long Term Strategic Thinking"
    ]

    for section in sections:

        body += f"""
        <h2>{section}</h2>

        <p>{title} is a topic that affects how individuals and organizations make financial decisions. Understanding the principles behind this concept helps people evaluate opportunities more carefully and avoid common mistakes.</p>

        <p>Professionals in finance and business strategy often analyze historical patterns, economic conditions, and long term objectives when considering these decisions.</p>

        <p>Developing a structured understanding of these ideas can help individuals and businesses improve their decision making processes and better manage risk.</p>
        """ * 2

    conclusion = f"""
    <h2>Conclusion</h2>

    <p>Understanding {title.lower()} can help individuals and business owners develop stronger financial awareness and better long term planning strategies.</p>

    <p>However, every financial decision should be evaluated within its own context. Professional guidance may be necessary depending on the complexity of the situation.</p>

    <p>Educational content like this is intended to improve awareness and understanding of important financial concepts.</p>
    """

    return intro + body + conclusion


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
