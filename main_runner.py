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
from topic_generator import generate_topic, reset_topic_tracker
from article_generator import generate_educational_content
from market_report_generator import generate_market_report_file

# ============================================
# MAIN RUNNER
# ============================================

def main():
    """Main function to generate all blog content"""
    
    # RESET TOPIC TRACKER AT START
    reset_topic_tracker()
    
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
    print(f"   • {trending_articles} Trending topic article")
    if generate_market:
        print(f"   • 1 Daily Market Report")
    print()
    
    articles_generated = 0
    unique_titles = set()  # Track titles in this run
    
    # Generate educational articles
    for i in range(educational_articles):
        try:
            print(f"📝 [{i+1}/{educational_articles}] Generating educational article...")
            
            topic = generate_topic()
            
            # Extra safety - ensure title is unique in this run
            original_title = topic['title']
            counter = 1
            while original_title in unique_titles and counter < 5:
                original_title = f"{topic['title']} - Part {counter}"
                counter += 1
            
            unique_titles.add(original_title)
            
            content = generate_educational_content(
                title=original_title,
                description=topic['description'],
                category=topic['category']
            )
            
            read_time = random.randint(7, 12)
            
            slug = fm.save_blog_post(
                title=original_title,
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
    trending_topics = [
        {
            "title": "Why Retail Investors Lose Money: Educational Analysis",
            "category": "Trading Psychology",
            "description": "An honest look at trading psychology and common mistakes."
        },
        {
            "title": "FII vs DII: Understanding Institutional Money Flows",
            "category": "Market Education",
            "description": "Educational guide to institutional investor activity."
        },
        {
            "title": "Understanding Market Corrections: A Historical Perspective",
            "category": "Market Education",
            "description": "Educational analysis of market corrections."
        },
        {
            "title": "The 17% Factor: Why Most IPO Investors Lose Money",
            "category": "IPO Strategies",
            "description": "Educational analysis of IPO investing."
        },
        {
            "title": "Smart Money vs Retail: Understanding Market Dynamics",
            "category": "Market Psychology",
            "description": "Educational look at market participant behavior."
        }
    ]
    
    # Shuffle to get random selection
    random.shuffle(trending_topics)
    
    for i in range(trending_articles):
        try:
            print(f"📈 [{i+1}/{trending_articles}] Generating trending article...")
            
            topic = trending_topics[i % len(trending_topics)]
            
            # Ensure unique title
            if topic['title'] in unique_titles:
                topic['title'] = f"{topic['title']} - Market Insights"
            unique_titles.add(topic['title'])
            
            content = generate_educational_content(
                title=topic['title'],
                description=topic['description'],
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
            
            market_file = generate_market_report_file()
            
            articles_generated += 1
            print(f"   ✅ Saved: {os.path.basename(market_file)}")
            
        except Exception as e:
            print(f"   ⚠️ Error generating market report: {str(e)}")
    
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