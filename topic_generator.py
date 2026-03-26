import os
import requests
import google.generativeai as genai

# Configuration
NEWS_API_KEY = "ec71777c7d0447d78c92ef7c431cd39b" # Your provided key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_automated_topic():
    """Fetches real-time news and converts it into a high-SEO blog topic."""
    
    # 1. Fetch Real-time Resources via News API
    query = "Indian Economy OR Nifty 50 OR BSE Sensex OR SEBI News"
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={NEWS_API_KEY}&pageSize=5"
    
    try:
        news_data = requests.get(url).json()
        articles = news_data.get('articles', [])
        
        # 2. Feed the raw news resources into Gemini to pick the best topic
        news_context = "\n".join([f"Headline: {a['title']} - {a['description']}" for a in articles])
        
        prompt = f"""
        Based on these real-time Indian market news resources:
        {news_context}
        
        Task:
        1. Select the ONE most impactful news item for an educational blog.
        2. Create a catchy, high-traffic SEO Title.
        3. Create 3 'People Also Ask' style questions for the FAQ section.
        
        Output format:
        TITLE: [Title]
        DESC: [Description]
        CAT: [Category]
        FAQS: [Q1|A1], [Q2|A2], [Q3|A3]
        """
        
        response = model.generate_content(prompt)
        # (Parsing logic here to return a dictionary)
        return response.text 
        
    except Exception as e:
        print(f"Automation Error: {e}")
        return None
