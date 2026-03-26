import os
import requests
import google.generativeai as genai

# Setup
NEWS_API_KEY = "ec71777c7d0447d78c92ef7c431cd39b" 
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_topic():  # <--- This name MUST match what main_runner.py imports
    """Fetches real-time news and converts it into a high-SEO blog topic."""
    query = "Indian Economy OR Nifty 50 OR RBI Policy OR Business Growth India"
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={NEWS_API_KEY}&pageSize=5"
    
    try:
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get('articles', [])
        news_context = "\n".join([f"Headline: {a['title']}" for a in articles])
        
        prompt = f"""
        Based on these current Indian market headlines:
        {news_context}
        Provide ONE unique educational blog topic.
        Output EXACTLY in this format:
        TITLE: [SEO Friendly Title]
        DESC: [Short 1-sentence description]
        CAT: [Category Name]
        """
        
        ai_response = model.generate_content(prompt)
        text = ai_response.text.strip()
        
        topic_data = {}
        for line in text.split('\n'):
            if "TITLE:" in line: topic_data['title'] = line.replace("TITLE:", "").strip()
            if "DESC:" in line: topic_data['description'] = line.replace("DESC:", "").strip()
            if "CAT:" in line: topic_data['category'] = line.replace("CAT:", "").strip()
            
        return topic_data
    except Exception as e:
        return {"title": "Strategic Growth 2026", "description": "Automated business scaling.", "category": "Business Strategy"}
