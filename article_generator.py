import random
from datetime import datetime

# ============================================
# FRAMEWORKS FOR DIFFERENT TOPICS
# ============================================

frameworks = [
    """
    <div class="highlight-box">
        <h4>📊 Framework: 60-30-10 Diversification Model</h4>
        <ul>
            <li><strong>60% Core assets</strong> – Diversified equities or index funds for long-term growth</li>
            <li><strong>30% Stability assets</strong> – Bonds, fixed income, or income-generating instruments</li>
            <li><strong>10% Opportunistic</strong> – Higher growth potential with managed risk</li>
        </ul>
        <p class="small">Educational reference only. Not investment advice.</p>
    </div>
    """,
    
    """
    <div class="highlight-box">
        <h4>📊 Framework: Core-Satellite Investment Strategy</h4>
        <ul>
            <li><strong>Core holdings</strong> – Provide stability and long-term growth (60-70%)</li>
            <li><strong>Satellite investments</strong> – Capture tactical opportunities (30-40%)</li>
            <li><strong>Periodic rebalancing</strong> – Maintains portfolio discipline</li>
        </ul>
        <p class="small">Educational reference only. Not investment advice.</p>
    </div>
    """,
    
    """
    <div class="highlight-box">
        <h4>📊 Framework: The Bucket Approach</h4>
        <ul>
            <li><strong>Bucket 1:</strong> Short-term liquidity (6-12 months expenses)</li>
            <li><strong>Bucket 2:</strong> Medium-term growth (3-7 year horizon)</li>
            <li><strong>Bucket 3:</strong> Long-term wealth building (10+ years)</li>
        </ul>
        <p class="small">Educational reference only. Not investment advice.</p>
    </div>
    """,
    
    """
    <div class="highlight-box">
        <h4>📊 Framework: Risk-Adjusted Return Model</h4>
        <ul>
            <li><strong>Step 1:</strong> Calculate risk tolerance before allocation</li>
            <li><strong>Step 2:</strong> Match assets to risk capacity</li>
            <li><strong>Step 3:</strong> Monitor Sharpe ratio for efficiency</li>
        </ul>
        <p class="small">Educational reference only. Not investment advice.</p>
    </div>
    """,
    
    """
    <div class="highlight-box">
        <h4>📊 Framework: The Pyramid Principle</h4>
        <ul>
            <li><strong>Base:</strong> Safety (fixed deposits, bonds, cash)</li>
            <li><strong>Middle:</strong> Growth (equities, mutual funds)</li>
            <li><strong>Top:</strong> Speculative (high-risk opportunities)</li>
        </ul>
        <p class="small">Educational reference only. Not investment advice.</p>
    </div>
    """
]

# ============================================
# AUTHOR PERSPECTIVES
# ============================================

author_perspectives = [
    """
    <div class="note-box">
        <p><i class="fas fa-quote-left" style="color: #d4af37;"></i> 
        Based on market observation, one pattern stands out: investors who succeed long-term 
        aren't those who chase quick returns, but those who maintain discipline through market cycles.
        This is an educational observation, not advice.
        </p>
    </div>
    """,
    
    """
    <div class="note-box">
        <p><i class="fas fa-quote-left" style="color: #d4af37;"></i> 
        After observing multiple market cycles, the biggest gap between theory and practice 
        is emotional discipline. The best strategy fails if you can't stick to it during volatility.
        For educational reference only.
        </p>
    </div>
    """,
    
    """
    <div class="note-box">
        <p><i class="fas fa-quote-left" style="color: #d4af37;"></i> 
        A common thread among successful investors is their focus on process over outcome. 
        They consistently apply their framework and let results follow naturally.
        Educational perspective only.
        </p>
    </div>
    """,
    
    """
    <div class="note-box">
        <p><i class="fas fa-quote-left" style="color: #d4af37;"></i> 
        In observing markets, patience often beats prediction. Investors who try to time 
        the market rarely beat those who stay invested through cycles.
        For learning purposes only.
        </p>
    </div>
    """
]

# ============================================
# EXAMPLE VARIATIONS
# ============================================

example_variations = [
    """
    <h3>📝 Educational Example</h3>
    <p>Consider a professional earning ₹15 lakhs annually, looking to build long-term wealth through understanding.</p>
    <ul>
        <li>Allocating across different asset classes for educational understanding</li>
        <li>Maintaining liquidity for opportunities and emergencies</li>
        <li>Regular review of allocation based on goals</li>
    </ul>
    <p class="small">This is an illustrative example for educational purposes only.</p>
    """,
    
    """
    <h3>📝 Educational Example</h3>
    <p>A mid-sized manufacturing company with surplus needed to understand capital allocation concepts.</p>
    <ul>
        <li>Evaluating expansion vs. reserve building</li>
        <li>Understanding working capital requirements</li>
        <li>Considering different investment options</li>
    </ul>
    <p class="small">This is an illustrative example for educational purposes only.</p>
    """,
    
    """
    <h3>📝 Educational Example</h3>
    <p>A family office exploring diversification concepts might consider:</p>
    <ul>
        <li>Core holdings in established businesses</li>
        <li>Income-generating instruments</li>
        <li>Alternative investment structures</li>
    </ul>
    <p class="small">This is an illustrative example for educational purposes only.</p>
    """
]

# ============================================
# MISTAKE VARIATIONS
# ============================================

mistake_variations = [
    [
        "Concentrating too much in a single area without diversification",
        "Making decisions based on short-term market movements",
        "Ignoring basic risk management principles",
        "Letting emotions drive financial decisions"
    ],
    [
        "Starting without a clear understanding of goals",
        "Overlooking the impact of inflation",
        "Neglecting regular portfolio review",
        "Following market rumors without verification"
    ],
    [
        "Investing without understanding the underlying concepts",
        "Trying to time market peaks and bottoms",
        "Taking excessive leverage without understanding risks",
        "Ignoring the importance of liquidity"
    ]
]

# ============================================
# FAQ GENERATOR
# ============================================

def generate_faqs(title, category):
    """Generate SEO-optimized FAQ section"""
    
    base_questions = [
        {
            "q": f"What is {title.lower()}?",
            "a": f"This refers to concepts in {category.lower()}. For educational purposes, it's important to understand the basic principles before making any financial decisions."
        },
        {
            "q": f"Why is {title.lower()} important?",
            "a": f"Understanding these concepts helps in making informed decisions. This is for educational awareness only."
        },
        {
            "q": "How can I learn more about financial concepts?",
            "a": "Our educational blog provides resources on various financial topics. Always consult qualified advisors before making decisions."
        }
    ]
    
    # Category-specific FAQs
    if "Business" in category:
        specific_faqs = [
            {
                "q": "How do businesses approach financial planning?",
                "a": "Businesses typically use structured frameworks for planning. This is an educational overview only."
            },
            {
                "q": "What are common business structures in India?",
                "a": "Common structures include private limited, partnership, and proprietorship. Each has different implications."
            }
        ]
    elif "Investment" in category or "Market" in category:
        specific_faqs = [
            {
                "q": "What is the difference between investing and trading?",
                "a": "Investing typically involves longer time horizons, while trading involves shorter-term positions. Educational perspective only."
            },
            {
                "q": "How do I start learning about markets?",
                "a": "Begin with basic concepts and gradually build understanding. Our educational blog is a good starting point."
            }
        ]
    else:
        specific_faqs = []
    
    all_faqs = base_questions + specific_faqs
    
    html = '<div class="faq-section">\n'
    html += '<h3>❓ Frequently Asked Questions</h3>\n'
    
    for faq in all_faqs[:4]:  # Limit to 4 FAQs
        html += f'''
        <div class="faq-item">
            <h4><i class="fas fa-question-circle"></i> {faq['q']}</h4>
            <p>{faq['a']}</p>
        </div>
        '''
    
    html += '</div>\n'
    return html

# ============================================
# MAIN CONTENT GENERATOR
# ============================================

def generate_educational_content(title, description, category):
    """Generate complete educational article content"""
    
    current_year = datetime.now().year
    current_month = datetime.now().strftime("%B")
    
    # Introduction
    intro = f"""
    <h2>Introduction</h2>
    <p>{description}</p>
    <p>This educational article provides an overview of key concepts in {category.lower()}. All information is for general awareness and learning purposes only.</p>
    """
    
    # Core Concepts
    concepts = f"""
    <h2>Understanding the Basics</h2>
    <p>{title} involves several fundamental concepts that are important to understand from an educational perspective. This section provides a high-level overview for learning purposes.</p>
    
    <h3>Key Principles</h3>
    <ul>
        <li><strong>Principle 1:</strong> Understanding the underlying concepts before making decisions</li>
        <li><strong>Principle 2:</strong> Recognizing that all financial decisions involve trade-offs</li>
        <li><strong>Principle 3:</strong> The importance of long-term thinking in financial planning</li>
        <li><strong>Principle 4:</strong> Basic risk management concepts</li>
    </ul>
    """
    
    # Framework
    framework = random.choice(frameworks)
    
    # Example
    example = random.choice(example_variations)
    
    # Common Mistakes
    mistakes_list = random.choice(mistake_variations)
    mistakes_html = ""
    for mistake in mistakes_list:
        mistakes_html += f"<li>{mistake}</li>"
    
    mistakes = f"""
    <h2>Common Mistakes to Avoid (Educational Perspective)</h2>
    <ul>
        {mistakes_html}
    </ul>
    <p class="small">Learning from common mistakes can help in understanding what to avoid. This is for educational purposes only.</p>
    """
    
    # Author Perspective
    perspective = random.choice(author_perspectives)
    
    # FAQs
    faqs = generate_faqs(title, category)
    
    # Conclusion
    conclusion = f"""
    <h2>Conclusion</h2>
    <p>Understanding {title.lower()} is an important part of financial education. This article provides a basic overview for learning purposes. Always conduct your own research and consult qualified professionals before making any financial decisions.</p>
    
    <div class="educational-notice">
        <i class="fas fa-graduation-cap"></i>
        <strong>Educational Purpose Only:</strong> This content is for general awareness and learning. It does not constitute financial advice or recommendations.
    </div>
    """
    
    # Assemble all sections
    sections = [
        intro,
        concepts,
        framework,
        example,
        mistakes,
        perspective,
        faqs,
        conclusion
    ]
    
    return "".join(sections)
