import os
import requests
import google.generativeai as genai

# Configuration
NEWS_API_KEY = "ec71777c7d0447d78c92ef7c431cd39b" 
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_topic():
    """
    Fetches real-time Indian business news and generates a 
    high-authority educational topic for the blog.
    """
    # Search for trending Indian financial topics
    query = "Indian Economy OR Nifty 50 OR RBI Policy OR SEBI"
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={NEWS_API_KEY}&pageSize=5"
    
    try:
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get('articles', [])
        
        # Combine headlines to give Gemini context
        context = "\n".join([f"- {a['title']}" for a in articles])
        
        prompt = f"""
        Based on these current Indian market headlines:
        {context}
        
        Suggest ONE unique, high-authority educational blog topic for Omkar Enterprises.
        Target: Indian Business Owners and Investors.
        
        Output format:
        TITLE: [SEO Optimized Title]
        DESC: [Short description of the article's goal]
        CAT: [Business Strategy, Capital Deployment, or Corporate Advisory]
        """
        
        ai_response = model.generate_content(prompt)
        text = ai_response.text.strip()
        
        # Parse result into a dictionary
        topic_data = {}
        for line in text.split('\n'):
            if "TITLE:" in line: topic_data['title'] = line.replace("TITLE:", "").strip()
            if "DESC:" in line: topic_data['description'] = line.replace("DESC:", "").strip()
            if "CAT:" in line: topic_data['category'] = line.replace("CAT:", "").strip()
            
        return topic_data

    except Exception as e:
        print(f"Topic Generation Error: {e}")
        # Reliable fallback topic if API fails
        return {
            "title": "Strategic Capital Allocation in Volatile Markets",
            "description": "An institutional guide to protecting and growing business capital.",
            "category": "Capital Deployment"
        }

def reset_topic_tracker():
    """Placeholder to maintain compatibility with main_runner.py"""
    pass
