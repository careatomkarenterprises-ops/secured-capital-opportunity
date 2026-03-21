#!/usr/bin/env python3
"""
Advanced Auto Blog Generator - Full Integration
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
# NEW INTEGRATION
from strategy_advisory_generator import generate_strategy_advisory

def main():
    reset_topic_tracker()
    
    print("=" * 50)
    print("🚀 OMKAR SERVICES AUTO-BLOG SYSTEM")
    print("=" * 50)
    
    fm = FileManager()
    
    educational_articles = 3 
    generate_market = True      
    generate_strategy = True  # New Strategic Advisory flag
    
    articles_generated = 0

    # 1. 🎯 Generate Daily Strategic Advisory (News-Based)
    if generate_strategy:
        print("🎯 Generating Daily Strategic Advisory...")
        try:
            advisory_slug = generate_strategy_advisory()
            if advisory_slug:
                print(f"   ✅ Saved: {advisory_slug}.html")
                articles_generated += 1
        except Exception as e:
            print(f"   ⚠️ Advisory Error: {str(e)}")

    # 2. 📚 Generate Educational Content
    print(f"\n📚 Generating {educational_articles} Educational Articles...")
    for i in range(educational_articles):
        try:
            topic = generate_topic()
            content = generate_educational_content(
                title=topic['title'],
                description=topic['description'],
                category=topic['category']
            )
            slug = fm.save_blog_post(
                title=topic['title'],
                content=content,
                category=topic['category'],
                read_time=random.randint(6, 10),
                author_specialization="Market Analysis"
            )
            articles_generated += 1
            print(f"   ✅ Saved: {slug}.html")
        except Exception as e:
            print(f"   ⚠️ Error: {str(e)}")
    
    # 3. 📊 Generate Daily Market Report
    if generate_market:
        try:
            print("\n📊 Generating Daily Market Report...")
            market_file = generate_market_report_file()
            articles_generated += 1
            print(f"   ✅ Saved: {os.path.basename(market_file)}")
        except Exception as e:
            print(f"   ⚠️ Market Report Error: {str(e)}")
    
    # 4. 🔄 Finalize
    print("\n🔄 Updating sitemap...")
    fm.generate_sitemap()
    print("✅ Sitemap updated")
    print(f"\n🎉 SUCCESS: {articles_generated} posts processed for Omkar Services.")

if __name__ == "__main__":
    main()
