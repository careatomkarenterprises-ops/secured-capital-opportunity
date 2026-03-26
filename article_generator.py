import os
import re
import json
import google.generativeai as genai

def generate_educational_content(title, description, category):
    """Generates a massive 3000+ word article, SEO FAQs, and Schema."""
    
    # Configure Gemini
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')

    # The Power Prompt for 3000+ Words and SEO
    prompt = f"""
    Write a massive, high-authority educational blog article (3000+ words).
    Title: {title}
    Focus: {description}
    Category: {category}
    Target Audience: Indian Business Owners, Institutional Investors, and Founders.

    STRICT TASK 1: ARTICLE CONTENT
    - Provide at least 10-12 deep-dive sections.
    - Use HTML tags: <h3> for subheadings, <p> for long paragraphs, <ul>/<li> for lists.
    - Include a 'Key Takeaways' and 'Common Pitfalls' section.
    - Use Indian market context: Mention SEBI norms, RBI policies, NSE/BSE dynamics, and GST impacts where relevant.
    - Avoid AI filler; use professional, corporate tone (Omkar Enterprises Style).

    STRICT TASK 2: FAQ SECTION (Q&A)
    - Provide 5 high-volume "People Also Ask" style questions.
    - Format as: 
      <h4>Q: [Question]?</h4>
      <p>A: [Detailed Answer]</p>

    STRICT TASK 3: SEO KEYWORDS
    - Provide 15 long-tail, high-intent keywords separated by commas.

    OUTPUT FORMAT:
    You MUST wrap the sections exactly like this:
    [CONTENT_START]
    (Article HTML here)
    [CONTENT_END]
    [FAQ_START]
    (5 Q&A pairs in HTML format)
    [FAQ_END]
    [KEYWORDS_START]
    (Comma separated keywords)
    [KEYWORDS_END]
    """
    
    try:
        response = model.generate_content(prompt)
        raw_text = response.text
        
        # Robust Parsing Logic
        content = raw_text.split("[CONTENT_START]")[1].split("[CONTENT_END]")[0].strip()
        faq_html = raw_text.split("[FAQ_START]")[1].split("[FAQ_END]")[0].strip()
        keywords = raw_text.split("[KEYWORDS_START]")[1].split("[KEYWORDS_END]")[0].strip()
        
        # Generate the JSON-LD Schema for Google SEO
        schema = generate_faq_schema(faq_html)

        # Wrap everything with the Omkar Enterprises educational headers/footers
        final_html = f"""
        <div class="educational-notice">
            <i class="fas fa-graduation-cap"></i>
            <strong>Institutional Education:</strong> This 3,000+ word deep-dive is part of our commitment to transparency in the Indian market.
        </div>

        <article class="main-article-content">
            {content}
        </article>

        <section class="faq-section" style="margin-top: 50px; padding: 20px; background: #f9f9f9; border-radius: 8px;">
            <h2 style="color: #c5a059;"><i class="fas fa-question-circle"></i> Frequently Asked Questions</h2>
            {faq_html}
        </section>

        <div class="educational-notice" style="margin-top: 30px;">
            <i class="fas fa-info-circle"></i>
            <strong>Note:</strong> Strategic outcomes vary by business scale. Consult TRFSK Omkar Services Private Limited for registered advisory.
        </div>

        <script type="application/ld+json">
        {json.dumps(schema)}
        </script>
        """

        return {
            "content": final_html,
            "faq_html": faq_html,
            "keywords": keywords,
            "title": title
        }
        
    except Exception as e:
        print(f"CRITICAL GENERATION ERROR: {e}")
        return None

def generate_faq_schema(faq_html):
    """
    Automated Schema Generator.
    Extracts Questions and Answers from HTML to build Google-ready JSON-LD.
    """
    try:
        # Simple regex to find the Q and A from the HTML generated above
        questions = re.findall(r"<h4>Q: (.*?)\?</h4>", faq_html)
        answers = re.findall(r"<p>A: (.*?)</p>", faq_html)
        
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": []
        }
        
        for q, a in zip(questions, answers):
            schema["mainEntity"].append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            })
        return schema
    except:
        return {}
