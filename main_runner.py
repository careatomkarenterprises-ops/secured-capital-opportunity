#!/usr/bin/env python3
"""
Advanced Auto Blog Generator - Humanized Version
Generates structured financial education articles with reduced AI footprint
Includes daily market report generation
"""

import sys
import os
import random
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from file_manager import FileManager
from topic_generator import generate_topic, get_seasonal_topics
from article_generator import generate_educational_content
from market_report_generator import generate_market_report_file
import json

# ============================================
# ENHANCED TOPIC GENERATION
# ============================================

def generate_market_update():
    """Generate daily market update with real data"""
    today = datetime.now().strftime("%B %d, %Y")
    return {
        "title": f"Daily Market Wrap: {today} - Educational Analysis",
        "content": "Market analysis content will be generated separately",
        "category": "Market Education"
    }

def generate_trending_topic():
    """Generate trending topic based on current events"""
    
    # Get current month for seasonal topics
    current_month = datetime.now().month
    
    # Trending topics based on time of year
    if current_month == 3:  # March - Financial year end
        topics = [
            {
                "title": "Tax Planning Before March 31: Complete Educational Guide",
                "category": "Seasonal Planning",
                "keywords": ["tax planning", "financial year end", "investment deadlines"]
            },
            {
                "title": "FY26 Budget Impact: Sector-wise Educational Analysis",
                "category": "Budget Analysis",
                "keywords": ["budget 2026", "tax changes", "economic policy"]
            }
        ]
    elif current_month in [10, 11, 12]:  # Q3 results season
        topics = [
            {
                "title": "Q3 Earnings Season: What Investors Should Know",
                "category": "Market Analysis",
                "keywords": ["earnings", "corporate results", "profit analysis"]
            },
            {
                "title": "Festive Season Market Trends: Historical Perspective",
                "category": "Market Education",
                "keywords": ["diwali investing", "seasonal trends", "market patterns"]
            }
        ]
    else:
        # Generic trending topics
        topics = [
            {
                "title": "Why Retail Investors Lose Money: Educational Analysis",
                "category": "Trading Psychology",
                "keywords": ["trading mistakes", "investor psychology", "risk management"]
            },
            {
                "title": "FII vs DII: Understanding Institutional Flows",
                "category": "Market Education",
                "keywords": ["fii data", "dii activity", "institutional investors"]
            }
        ]
    
    return random.choice(topics)

# ============================================
# MAIN RUNNER
# ============================================

def main():
    """Main function to generate all blog content"""
    
    print("=" * 50)
    print("🚀 AUTO BLOG GENERATOR STARTING")
    print("=" * 50)
    print(f"📅 Date: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
    print()
    
    fm = FileManager()
    
    # Configuration
    educational_articles = 3  # Number of educational articles to generate
    trending_articles = 1      # Number of trending topic articles
    generate_market = True      # Generate daily market report
    
    total_articles = educational_articles + trending_articles
    if generate_market:
        total_articles += 1
    
    print(f"📊 Generating {total_articles} articles today:")
    print(f"   • {educational_articles} Educational articles")
    print(f"   • {trending_articles} Trending topic articles")
    if generate_market:
        print(f"   • 1 Daily Market Report")
    print()
    
    articles_generated = 0
    
    # Generate educational articles
    for i in range(educational_articles):
        try:
            print(f"📝 [{i+1}/{educational_articles}] Generating educational article...")
            
            topic = generate_topic()
            
            content = generate_educational_content(
                title=topic['title'],
                description=topic['description'],
                category=topic['category']
            )
            
            read_time = random.randint(7, 12)
            
            slug = fm.save_blog_post(
                title=topic['title'],
                content=content,
                category=topic['category'],
                read_time=read_time,
                author_specialization="Business & Market Education"
            )
            
            articles_generated += 1
            print(f"   ✅ Saved: {slug}.html")
            
        except Exception as e:
            print(f"   ⚠️ Error: {str(e)}")
    
    print()
    
    # Generate trending articles
    for i in range(trending_articles):
        try:
            print(f"📈 [{i+1}/{trending_articles}] Generating trending article...")
            
            topic = generate_trending_topic()
            
            # Create description from topic
            description = f"Educational analysis of {topic['title'].lower()}. For learning purposes only."
            
            content = generate_educational_content(
                title=topic['title'],
                description=description,
                category=topic['category']
            )
            
            read_time = random.randint(6, 10)
            
            slug = fm.save_blog_post(
                title=topic['title'],
                content=content,
                category=topic['category'],
                read_time=read_time,
                author_specialization="Market Analysis"
            )
            
            articles_generated += 1
            print(f"   ✅ Saved: {slug}.html")
            
        except Exception as e:
            print(f"   ⚠️ Error: {str(e)}")
    
    print()
    
    # Generate daily market report
    if generate_market:
        try:
            print("📊 Generating Daily Market Report...")
            
            # Call the market report generator
            market_file = generate_market_report_file()
            
            articles_generated += 1
            print(f"   ✅ Saved: {os.path.basename(market_file)}")
            
        except Exception as e:
            print(f"   ⚠️ Error generating market report: {str(e)}")
            print("   Continuing with other articles...")
    
    print()
    print("=" * 50)
    print(f"✅ GENERATION COMPLETE")
    print(f"📊 Total articles generated: {articles_generated}")
    print("=" * 50)
    
    # Generate sitemap
    print("\n🔄 Generating sitemap...")
    fm.generate_sitemap()
    print("✅ Sitemap updated")
    
    print("\n🎉 All done! Your blog is updated.")


if __name__ == "__main__":
    main()
