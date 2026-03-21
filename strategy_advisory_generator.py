import os
import requests
import google.generativeai as genai
from datetime import datetime
from file_manager import FileManager

# Configuration - Uses GitHub Secrets for Safety
NEWS_API_KEY = "ec71777c7d0447d78c92ef7c431cd39b"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def fetch_market_news():
    """Fetches real-time business and finance news for India."""
    url = f"https://newsapi.org/v2/everything?q=Indian+Economy+OR+Business+Growth+India&sortBy=publishedAt&apiKey={NEWS_API_KEY}&pageSize=1"
    try:
        data = requests.get(url).json()
        article = data['articles'][0]
        return article['title'], article['description']
    except Exception:
        return "Sustainable Capital Allocation in 2026", "Strategic focus on long-term business sustainability and risk management."

def generate_strategy_advisory():
    """Generates the premium strategy post and saves it via FileManager."""
    news_title, news_desc = fetch_market_news()
    
    prompt = f"""
    Write a high-authority, premium business advisory article.
    Topic: {news_title}
    Context: {news_desc}
    
    The tone should be institutional and corporate. Include:
    1. <h3>Strategic Market Impact</h3> (Business perspective)
    2. <h3>Capital Allocation Advisory</h3> (Actionable financial logic)
    3. <h3>Operational Technology</h3> (How automation helps here)
    
    End with: 'This is for educational purposes only. Not SEBI/RBI advice.'
    """
    
    try:
        response = model.generate_content(prompt)
        content = response.text
        
        fm = FileManager()
        # This saves it into your blog system automatically
        slug = fm.save_blog_post(
            title=f"Strategic Advisory: {news_title}",
            content=content,
            category="Business Strategy", 
            read_time=5,
            author_specialization="Corporate Advisory"
        )
        return slug
    except Exception as e:
        print(f"Error generating advisory: {e}")
        return None
