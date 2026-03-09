#!/usr/bin/env python3
"""
Main runner for auto-blog generation
Generates EDUCATIONAL content with proper disclaimers
"""

import sys
import os
import json
import random
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from file_manager import FileManager

def load_topics():
    """Load topics from JSON file"""
    try:
        with open('seo_topics.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ seo_topics.json not found")
        return {}

def generate_educational_content(topic_data, category):
    """Generate educational content with proper disclaimers"""
    
    title = topic_data['title']
    description = topic_data['description']
    
    # Educational introduction
    intro = f"""
    <h2>Introduction: Understanding {title}</h2>
    <p>{description}</p>
    
    <p>This article provides general information for business owners and entrepreneurs. It is not intended as specific advice for any individual or company.</p>
    
    <div class="note" style="background: #f8fafc; padding: 20px; border-radius: 8px; margin: 20px 0;">
        <p><strong>Key Concept:</strong> Understanding these principles helps business leaders make more informed decisions within their specific context.</p>
    </div>
    """
    
    # Main educational content
    main_content = f"""
    <h2>Core Concepts in {category}</h2>
    <p>When exploring {title.lower()}, there are several fundamental concepts that business owners should understand:</p>
    
    <ul>
        <li><strong>Context Matters:</strong> Every business situation is unique. What works for one company may not work for another.</li>
        <li><strong>Professional Guidance:</strong> Complex business decisions should involve qualified professionals.</li>
        <li><strong>Due Diligence:</strong> Always conduct thorough research before making business decisions.</li>
        <li><strong>Documentation:</strong> Proper documentation protects all parties in business arrangements.</li>
    </ul>
    
    <h2>Practical Considerations</h2>
    <p>When applying these concepts, consider:</p>
    <ul>
        <li>Your specific business objectives and constraints</li>
        <li>The regulatory environment applicable to your situation</li>
        <li>Consultation with legal and financial professionals</li>
        <li>Documentation of all material agreements</li>
    </ul>
    
    <h2>Industry Perspectives</h2>
    <p>Santosh Shendkar, founder of TRFSK OMKAR SERVICES, notes: "The most successful business owners take time to understand fundamental concepts while recognizing when to seek professional guidance. Education empowers better decisions, but implementation requires expertise."</p>
    
    <h2>Further Reading</h2>
    <p>For more information, explore our other educational articles on business strategy, compliance, and capital structuring. Each article provides general information to help you better understand these complex topics.</p>
    """
    
    # Conclusion (always educational, never promotional)
    conclusion = f"""
    <h2>Conclusion</h2>
    <p>Understanding {title.lower()} is valuable for business owners and entrepreneurs. However, every business situation is unique, and general information should not replace professional advice tailored to your specific circumstances.</p>
    
    <p>We encourage readers to:</p>
    <ul>
        <li>Continue learning about business concepts through reputable sources</li>
        <li>Consult with qualified professionals for specific situations</li>
        <li>Maintain proper documentation for all business arrangements</li>
        <li>Stay informed about regulatory requirements affecting their business</li>
    </ul>
    
    <p>TRFSK OMKAR SERVICES provides corporate advisory and management consultancy services. Our team helps businesses navigate complex decisions through structured advisory engagements.</p>
    """
    
    return intro + main_content + conclusion

def main():
    """Main function to generate educational blog posts"""
    
    fm = FileManager()
    topics_db = load_topics()
    
    if not topics_db:
        print("❌ No topics found. Exiting.")
        return
    
    # Generate 3 articles per run (reduced from 5 for quality focus)
    articles_per_run = 3
    
    print(f"🚀 Generating {articles_per_run} educational articles...")
    
    for i in range(articles_per_run):
        try:
            category_key = random.choice(list(topics_db.keys()))
            category_display = category_key.replace('_', ' ').title()
            
            topic_data = random.choice(topics_db[category_key])
            title = topic_data['title']
            
            print(f"📝 Generating article {i+1}: {title}")
            
            content = generate_educational_content(topic_data, category_display)
            read_time = random.randint(4, 7)  # Shorter for educational content
            
            slug = fm.save_blog_post(
                title=title,
                content=content,
                category=category_display,
                read_time=read_time,
                author_specialization=f"Business Advisory"
            )
            
            print(f"✅ Generated: {slug}.html")
            
        except Exception as e:
            print(f"⚠️ Error: {str(e)}")
            continue
    
    fm.generate_sitemap()
    print(f"\n✅ Generated {articles_per_run} educational articles")

if __name__ == "__main__":
    main()
