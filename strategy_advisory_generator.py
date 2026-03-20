import os
import requests
import google.generativeai as genai
from datetime import datetime
from file_manager import FileManager

# Configuration
NEWS_API_KEY = "ec71777c7d0447d78c92ef7c431cd39b"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def fetch_market_news():
    """Gets real-time hot news about the Indian Economy."""
    url = f"https://newsapi.org/v2/everything?q=Indian+Stock+Market+OR+Business+Finance+India&sortBy=publishedAt&apiKey={NEWS_API_KEY}&pageSize=1"
    try:
        data = requests.get(url).json()
        article = data['articles'][0]
        return article['title'], article['description']
    except Exception:
        return "Strategic Capital Management in 2026", "Focusing on business sustainability and automated growth in the current economic climate."

def generate_strategy_advisory():
    """Uses AI to turn news into a 'Strategic Advisory' article and saves it."""
    news_title, news_desc = fetch_market_news()
    
    prompt = f"""
    Write a high-authority business advisory article for TRFSK Omkar Services.
    Topic: {news_title}
    Context: {news_desc}
    
    Structure:
    1. <h3>Market Impact</h3> (How this affects Indian Business Directors)
    2. <h3>Strategic Capital Allocation</h3> (Allocation advice for this condition)
    3. <h3>Automation Edge</h3> (How tech/AI can help manage this)
    
    Tone: Premium, Corporate, Institutional.
    Compliance: End with 'This is for educational purposes only. Not RBI/SEBI advice.'
    """
    
    try:
        response = model.generate_content(prompt)
        content = response.text
        
        fm = FileManager()
        # This automatically uses your template.html and updates sitemap/categories
        slug = fm.save_blog_post(
            title=f"Strategy: {news_title}",
            content=content,
            category="Business Strategy", 
            read_time=5,
            author_specialization="Strategic Advisory"
        )
        return slug
    except Exception as e:
        print(f"Error in Gemini Generation: {e}")
        return None

if __name__ == "__main__":
    generate_strategy_advisory()
