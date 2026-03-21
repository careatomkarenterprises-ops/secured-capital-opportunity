import os
import google.generativeai as genai

def generate_educational_content(title, description, category):
    """Generates a full, high-quality unique article using Gemini AI."""
    
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    Write a professional, high-quality educational blog article.
    Title: {title}
    Focus: {description}
    Target Audience: Indian Business Owners and Investors.
    
    Requirements:
    1. Use HTML tags for structure (<h3>, <p>, <ul>, <li>).
    2. Start with a real-world scenario or story to make it human.
    3. Include a 'Key Takeaways' section.
    4. Include a 'Common Pitfalls' section.
    5. Maintain a helpful, expert tone.
    6. Tone should be 'Omkar Enterprises' - professional yet accessible.
    
    DO NOT use generic AI filler words. Use specific Indian market context where relevant.
    """
    
    try:
        response = model.generate_content(prompt)
        content = response.text
        
        # Wrap with your educational notice
        header = f"""
        <div class="educational-notice">
            <i class="fas fa-graduation-cap"></i>
            <strong>Educational Purpose Only:</strong> This article is for 
            general awareness and learning. Not investment advice.
        </div>
        """
        
        footer = f"""
        <div class="educational-notice" style="margin-top: 30px;">
            <i class="fas fa-info-circle"></i>
            <strong>Note:</strong> What works for one business may not work for another. 
            Consult with the team at Omkar Enterprises for personalized strategic guidance.
        </div>
        """
        
        return header + content + footer
        
    except Exception as e:
        return f"<p>Content generation temporarily unavailable. Please check back soon. Error: {str(e)}</p>"
