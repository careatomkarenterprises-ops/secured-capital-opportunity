#!/usr/bin/env python3
"""
Advanced Auto Blog Generator - Full Integration
OMKAR SERVICES - Version 2.0
"""

import sys
import os
import random
from datetime import datetime

# Ensure the script can find the local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import existing modules
from file_manager import FileManager
from topic_generator import generate_topic, reset_topic_tracker
from article_generator import generate_educational_content
from market_report_generator import generate_market_report_file

# NEW INTEGRATION: Strategic Advisory (News-Based)
try:
    from strategy_advisory_generator import generate_strategy_advisory
except ImportError:
    # Fallback to prevent crash if the file is missing
    print("⚠️ Warning: strategy_advisory_generator.py not found.")
    def generate_strategy_advisory(): return None

def main():
    """Main execution function for the blog automation"""
    
    # Initialize session
    reset_topic_tracker()
    
    print("=" * 50)
    print("🚀 OMKAR SERVICES AUTO-BLOG SYSTEM")
    print("=" * 50)
    print(f"📅 Run Date: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
    print("-" * 50)
    
    fm = FileManager()
    
    # Configuration - Adjust numbers as needed
    educational_articles = 3  
    generate_market = True      
    generate_strategy = True  # Flag for Strategic Advisory
    
    articles_generated = 0

    # 1. 🎯 PART ONE: Generate Daily Strategic Advisory (News-Based)
    if generate_strategy:
        print("🎯 Task 1: Generating Daily Strategic Advisory...")
        try:
            advisory_slug = generate_strategy_advisory()
            if advisory_slug:
                print(f"   ✅ Saved Advisory: {advisory_slug}.html")
                articles_generated += 1
            else:
                print("   ℹ️ No advisory generated (Check API/News source)")
        except Exception as e:
            print(f"   ⚠️ Advisory Error: {str(e)}")

    # 2. 📚 PART TWO: Generate Educational Content
    print(f"\n📚 Task 2: Generating {educational_articles} Educational Articles...")
    for i in range(educational_articles):
        try:
            topic = generate_topic()
            content = generate_educational_content(
                title=topic['title'],
                description=topic['description'],
                category=topic['category']
            )
            
            # Save post and update the internal index automatically
            slug = fm.save_blog_post(
                title=topic['title'],
                content=content,
                category=topic['category'],
                read_time=random.randint(6, 10),
                author_specialization="Market Analysis"
            )
            
            articles_generated += 1
            print(f"   ✅ Saved Article: {slug}.html")
        except Exception as e:
            print(f"   ⚠️ Educational Article Error: {str(e)}")
    
    # 3. 📊 PART THREE: Generate Daily Market Report
    if generate_market:
        print("\n📊 Task 3: Generating Daily Market Report...")
        try:
            market_file = generate_market_report_file()
            market_filename = os.path.basename(market_file)
            market_slug = market_filename.replace('.html', '')
            
            # CRITICAL: Manually update the blog index for the Market Report
            # because market_report_generator often bypasses standard saving logic
            fm.update_blog_index(
                title=f"Daily Market Wrap: {datetime.now().strftime('%B %d, %Y')}",
                slug=market_slug,
                category="Market Analysis"
            )
            
            articles_generated += 1
            print(f"   ✅ Saved Market Report: {market_filename}")
        except Exception as e:
            print(f"   ⚠️ Market Report Error: {str(e)}")
    
    # 4. 🔄 PART FOUR: Finalize System
    print("\n" + "=" * 50)
    print("🔄 Finalizing System Updates...")
    
    try:
        # Update sitemap.xml for Google/Bing SEO
        fm.generate_sitemap()
        print("✅ Sitemap updated successfully")
    except Exception as e:
        print(f"   ⚠️ Sitemap Error: {str(e)}")

    print("-" * 50)
    print(f"🎉 SUCCESS: {articles_generated} total posts processed.")
    print(f"🚀 System deployment ready for GitHub Actions.")
    print("=" * 50)

if __name__ == "__main__":
    main()
