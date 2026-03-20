import os
import json
import requests
import google.generativeai as genai
from datetime import datetime

# ==========================================
# 1. CONFIGURATION
# ==========================================
NEWS_API_KEY = "ec71777c7d0447d78c92ef7c431cd39b"
GEMINI_API_KEY = "AIzaSyA4K7s9rS4I_hvWh6M59M70v6FGu9dROp8" 
FORMSPREE_ID = "YOUR_ID" # <-- Replace with your Formspree ID

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# ==========================================
# 2. INTELLIGENCE ENGINE
# ==========================================

def fetch_market_pulse():
    """Gets real-time hot news about Indian Economy & Stock Market."""
    query = "Indian Stock Market OR Nifty 50 OR RBI Policy"
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={NEWS_API_KEY}&pageSize=1"
    try:
        data = requests.get(url).json()
        article = data['articles'][0]
        return article['title'], article['description']
    except:
        return "Strategic Capital Allocation in 2026", "Focusing on business sustainability and automated growth."

def generate_expert_article(title, context):
    """Uses AI to turn news into a 'Strategic Advisory' article."""
    prompt = f"""
    Write a high-authority business advisory article for TRFSK Omkar Services.
    Topic: {title}
    Context: {context}
    
    Structure:
    1. Economic Impact: How this affects Indian Business Directors.
    2. Capital Strategy: Allocation advice for this market condition.
    3. Automation Edge: How using Python/AI can protect operations.
    
    Tone: Premium, Corporate, Institutional.
    Format: Use HTML tags <h3> and <p>. Max 450 words.
    Compliance: End with 'Educational purposes only. Not RBI/SEBI advice.'
    """
    response = model.generate_content(prompt)
    return response.text

# ==========================================
# 3. WEB & SEO AUTOMATION
# ==========================================

def update_sitemap(new_link):
    """Automatically adds the new page to your sitemap.xml."""
    if not os.path.exists('sitemap.xml'): return
    with open('sitemap.xml', 'r') as f:
        lines = f.readlines()
    
    new_entry = f"  <url>\n    <loc>https://omkarservices.in/{new_link}</loc>\n    <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>\n    <priority>0.8</priority>\n  </url>\n"
    lines.insert(-1, new_entry)
    
    with open('sitemap.xml', 'w') as f:
        f.writelines(lines)

def create_lead_gen_page(title, content):
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = title.lower().replace(" ", "-")[:50].strip("-") + ".html"
    filepath = f"blog/post/{slug}"
    
    os.makedirs("blog/post", exist_ok=True)

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title} | TRFSK Omkar Services</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #f8fafc; color: #0f172a; padding: 20px; line-height: 1.7; }}
            .card {{ max-width: 850px; margin: 40px auto; background: white; padding: 50px; border-radius: 20px; border-top: 6px solid #d4af37; box-shadow: 0 15px 30px rgba(0,0,0,0.05); }}
            h1 {{ color: #0f172a; font-size: 2.2em; }}
            .cta {{ background: #0f172a; color: white; padding: 30px; border-radius: 12px; margin-top: 40px; text-align: center; }}
            .cta input {{ padding: 12px; width: 60%; border-radius: 6px; border: none; margin-bottom: 10px; }}
            .cta button {{ background: #d4af37; color: #0f172a; padding: 12px 25px; border: none; font-weight: bold; border-radius: 6px; cursor: pointer; }}
            footer {{ margin-top: 40px; font-size: 12px; color: #64748b; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="card">
            <p style="color:#d4af37; font-weight:bold;">STRATEGIC PULSE | {date_str}</p>
            <h1>{title}</h1>
            <div class="content">{content}</div>
            <div class="cta">
                <h3>Request Your Strategic Roadmap</h3>
                <p>Private consultation for Capital Deployment & Automation.</p>
                <form action="https://formspree.io/f/{FORMSPREE_ID}" method="POST">
                    <input type="email" name="email" placeholder="Business Email" required>
                    <button type="submit">Connect with Director</button>
                </form>
            </div>
            <footer>
                © 2026 TRFSK OMKAR SERVICES PRIVATE LIMITED | CIN: U70200MH2023PTC407336<br>
                This is an educational advisory. Not an RBI Registered NBFC.
            </footer>
        </div>
    </body>
    </html>
    """
    with open(filepath, "w") as f:
        f.write(html_template)
    return filepath, slug

# ==========================================
# 4. EXECUTION
# ==========================================
if __name__ == "__main__":
    print("--- TRFSK GROWTH ENGINE STARTING ---")
    title, desc = fetch_market_pulse()
    print(f"Targeting: {title}")
    
    article = generate_expert_article(title, desc)
    path, slug = create_lead_gen_page(title, article)
    
    update_sitemap(f"blog/post/{slug}")
    print(f"SUCCESS: Page created and Sitemap updated.")
    print(f"Location: {path}")
