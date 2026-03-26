import os
import sys
from datetime import datetime

# Import your local modules
from file_manager import FileManager
from topic_generator import generate_topic
from article_generator import generate_educational_content
from market_report_generator import generate_market_report_file
import omkar_growth_engine # This is the new growth tool

def main():
    print(f"🚀 OMKAR AUTOMATION STARTING: {datetime.now()}")
    fm = FileManager()
    
    # Task 1: Generate the Strategic Advisory (Lead Gen)
    try:
        title, desc = omkar_growth_engine.fetch_market_pulse()
        article = omkar_growth_engine.generate_expert_article(title, desc)
        slug = omkar_growth_engine.create_lead_gen_page(title, article)
        print(f"✅ Part 1: Strategic Lead-Gen Article Created ({slug})")
    except Exception as e:
        print(f"❌ Part 1 Error: {e}")

    # Task 2: Generate Daily Market Wrap (Daily Reports)
    try:
        market_file = generate_market_report_file()
        print(f"✅ Part 2: Daily Market Wrap Created")
    except Exception as e:
        print(f"❌ Part 2 Error: {e}")

    # Task 3: Generate 2 General Educational Articles
    for i in range(2):
        try:
            topic = generate_topic()
            content = generate_educational_content(topic['title'], topic['description'], topic['category'])
            fm.save_blog_post(topic['title'], content, topic['category'])
            print(f"✅ Part 3: Educational Post {i+1} Created")
        except Exception as e:
            print(f"❌ Part 3 Error: {e}")

    # Task 4: Finalize SEO (Sitemap)
    try:
        fm.generate_sitemap()
        print("✅ Part 4: SEO Sitemap Updated")
    except Exception as e:
        print(f"❌ Part 4 Error: {e}")

    print("🎉 All systems updated. Omkar Enterprises is online.")

if __name__ == "__main__":
    main()
