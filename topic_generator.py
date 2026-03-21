import os
import random
import google.generativeai as genai

# Setup Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_topic():
    """Generates a fresh, unique topic using AI to avoid repetition."""
    
    prompt = """
    Suggest ONE unique educational blog post title for a financial services website.
    The topic should be about either 'Business Strategy', 'Capital Allocation', or 'Indian Stock Market Education'.
    
    Rules:
    - Avoid generic titles like "Understanding X".
    - Make it highly specific to Indian business owners or investors.
    - Ensure it sounds professional and helpful.
    
    Output exactly in this format:
    TITLE: [Title Here]
    DESC: [Short 1-sentence description]
    CAT: [Category Name]
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        # Parse the AI response
        lines = text.split('\n')
        topic_data = {}
        for line in lines:
            if "TITLE:" in line: topic_data['title'] = line.replace("TITLE:", "").strip()
            if "DESC:" in line: topic_data['description'] = line.replace("DESC:", "").strip()
            if "CAT:" in line: topic_data['category'] = line.replace("CAT:", "").strip()
            
        return topic_data
    except Exception as e:
        # Fallback to a safe default if AI fails
        return {
            "title": "Strategic Risk Management for Indian SMEs",
            "description": "How to protect your business assets in a volatile market.",
            "category": "Business Strategy"
        }
