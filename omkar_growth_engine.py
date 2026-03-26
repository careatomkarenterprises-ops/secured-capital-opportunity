import os
import requests
import google.generativeai as genai
from datetime import datetime
from file_manager import FileManager

# ==========================================
# 1. CONFIGURATION (Updated with your keys)
# ==========================================
NEWS_API_KEY = "ec71777c7d0447d78c92ef7c431cd39b"
GEMINI_API_KEY = "AIzaSyA4K7s9rS4I_hvWh6M59M70v6FGu9dROp8" 
FORMSPREE_ID = "mdkqpkqp" # Your specific ID

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def fetch_market_pulse():
    """Gets real-time hot news about Indian Economy & Stock Market."""
    query = "Indian Stock Market OR Nifty 50 OR RBI Policy"
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={NEWS_API_KEY}&pageSize=1"
    try:
        data = requests.get(url).json()
        article = data['articles'][0]
        return article['title'], article['description']
    except:
        return "Strategic Capital Allocation for 2026", "Focusing on business sustainability and automated growth."

def generate_expert_article(title, context):
    """Uses AI to turn news into a 'Strategic Advisory' for your business."""
    prompt = f"""
    Write a high-authority business advisory article for 'Omkar Enterprises'.
    Current News Topic: {title}
    Context: {context}
    
    Target: Indian Investors and Business Owners looking for passive income and automation.
    Requirements:
    1. Discuss how daily market volatility (current news) requires automation like our 'Scanner Tools'.
    2. Explain that we provide 'Structured Capital Approaches' secured by 'Private Agreements' (PDCs and Notarized Contracts).
    3. The tone must be professional, institutional, and high-trust.
    4. Mention that Omkar Enterprises helps bridge the gap between market data and passive cash flow.
    5. End with: 'This is for educational purposes only. Not SEBI/RBI advice.'
    """
    response = model.generate_content(prompt)
    return response.text

def create_lead_gen_page(title, content):
    """Saves the article into your blog system with your lead capture form."""
    fm = FileManager()
    # This automatically uses your blog template and updates your index
    slug = fm.save_blog_post(
        title=f"Strategic Advisory: {title}",
        content=content,
        category="Capital Deployment",
        read_time=7,
        author_specialization="Director, Omkar Enterprises"
    )
    return slug

if __name__ == "__main__":
    print("--- OMKAR GROWTH ENGINE STARTING ---")
    news_title, news_desc = fetch_market_pulse()
    print(f"Generating advisory for: {news_title}")
    
    article_content = generate_expert_article(news_title, news_desc)
    slug = create_lead_gen_page(news_title, article_content)
    print(f"✅ Success! Strategic Advisory posted: {slug}")
