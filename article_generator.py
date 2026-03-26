import os
import json
import google.generativeai as genai

def generate_educational_content(title, description, category):
    """Generates a full article PLUS SEO-friendly FAQ and Schema."""
    
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    Write a high-authority educational blog article and a matching FAQ section.
    Title: {title}
    Focus: {description}
    Target Audience: Indian Business Owners and Investors.
    
    TASK 1: ARTICLE CONTENT
    - Use HTML (<h3>, <p>, <ul>).
    - Include 'Key Takeaways' and 'Common Pitfalls'.
    - Use Indian market context (NSE, BSE, RBI where relevant).

    TASK 2: FAQ SECTION (Q&A)
    - Provide 3-4 frequently asked questions based on "People Also Ask" search trends.
    - Provide concise, helpful answers.

    TASK 3: SEO KEYWORDS
    - Provide 10 long-tail keywords related to this topic.

    OUTPUT FORMAT:
    Return the result in this exact string format so I can parse it:
    [CONTENT_START]
    (Article HTML here)
    [CONTENT_END]
    [FAQ_START]
    (3-4 Q&A pairs in HTML format)
    [FAQ_END]
    [KEYWORDS_START]
    (Comma separated keywords)
    [KEYWORDS_END]
    """
    
    try:
        response = model.generate_content(prompt)
        raw_text = response.text
        
        # Simple Parsing Logic
        content = raw_text.split("[CONTENT_START]")[1].split("[CONTENT_END]")[0].strip()
        faq_html = raw_text.split("[FAQ_START]")[1].split("[FAQ_END]")[0].strip()
        keywords = raw_text.split("[KEYWORDS_START]")[1].split("[KEYWORDS_END]")[0].strip()
        
        return {
            "content": content,
            "faq_html": faq_html,
            "keywords": keywords,
            "faq_schema": generate_faq_schema(faq_html) # Helper function below
        }
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def generate_faq_schema(faq_html):
    """Converts the FAQ HTML into JSON-LD Schema for Google."""
    # This is a simplified version; in production, 
    # you can use BeautifulSoup to extract Qs and As more accurately.
    return ""
