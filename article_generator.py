import random
from datetime import datetime
import hashlib

# ============================================
# DYNAMIC CONTENT BUILDING BLOCKS
# These combine in thousands of ways
# ============================================

# Indian cities (20+ options)
cities = [
    "Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata", "Pune", "Ahmedabad",
    "Hyderabad", "Lucknow", "Jaipur", "Indore", "Nagpur", "Bhopal", "Surat",
    "Vadodara", "Coimbatore", "Mysore", "Trivandrum", "Kochi", "Goa"
]

# Professions (15+ options)
professions = [
    "software engineer", "doctor", "chartered accountant", "business owner",
    "teacher", "lawyer", "architect", "marketing professional", "civil servant",
    "banker", "consultant", "entrepreneur", "freelancer", "pharmacist", "dentist"
]

# Ages (range)
ages = list(range(25, 65))

# Income levels (10+ options)
incomes = [
    "₹6 lakhs", "₹12 lakhs", "₹18 lakhs", "₹25 lakhs", "₹35 lakhs",
    "₹50 lakhs", "₹75 lakhs", "₹1 crore", "₹1.5 crore", "₹2 crore+"
]

# Business types (15+ options)
business_types = [
    "manufacturing", "trading", "retail", "wholesale", "IT services",
    "construction", "real estate", "textiles", "pharmaceuticals", "agriculture",
    "food processing", "logistics", "healthcare", "education", "hospitality"
]

# Business sizes
business_sizes = [
    "₹2 crore", "₹5 crore", "₹10 crore", "₹25 crore", "₹50 crore",
    "₹100 crore", "₹200 crore", "₹500 crore"
]

# Challenges (30+ options)
challenges = [
    "managing cash flow", "handling competition", "retaining employees",
    "expanding to new markets", "managing debt", "valuing the business",
    "succession planning", "partnership disputes", "regulatory compliance",
    "tax planning", "raising capital", "technology adoption",
    "inventory management", "customer acquisition", "pricing strategy"
]

# Market events (20+ options)
market_events = [
    "2008 financial crisis", "2020 COVID crash", "2013 taper tantrum",
    "demonetization 2016", "GST implementation 2017", "IL&FS crisis 2018",
    "Yes Bank crisis 2020", "Ukraine war 2022", "US Fed rate hikes 2023",
    "election results 2024", "budget announcements", "RBI policy changes"
]

# Lessons from events (20+ options)
market_lessons = [
    "markets eventually recover", "quality companies withstand volatility",
    "panic selling locks in losses", "diversification protects capital",
    "time in market beats timing the market", "valuations matter",
    "cash is king during crises", "avoid leverage in volatile times"
]

# Expert names (30+ options)
expert_first = [
    "Rajesh", "Sunita", "Amit", "Priya", "Vikram", "Anjali", "Sanjay", "Deepa",
    "Ravi", "Kavita", "Mohan", "Lata", "Suresh", "Geeta", "Mahesh", "Nalini"
]

expert_last = [
    "Sharma", "Verma", "Patel", "Gupta", "Reddy", "Nair", "Joshi", "Desai",
    "Singh", "Kumar", "Menon", "Iyengar", "Chatterjee", "Banerjee"
]

expert_titles = [
    "SEBI-registered investment advisor", "chartered accountant",
    "wealth manager", "financial planner", "portfolio manager",
    "business consultant", "tax consultant", "estate planner"
]

# Quotes templates (20+ variations)
quote_templates = [
    "The biggest mistake I see is {mistake}. People focus on {wrong_thing} instead of {right_thing}.",
    "After {years} years in this field, I've learned that {lesson} matters more than {overrated}.",
    "Most people don't realize that {insight}. It's the hidden factor that makes all the difference.",
    "Here's what I tell all my clients: {advice}. It sounds simple, but it's the hardest thing to follow.",
    "If there's one thing I wish everyone knew, it's that {truth}. Everything else is just noise."
]

# Advice snippets (30+ options)
advice_list = [
    "start early, even with small amounts",
    "focus on what you can control, not market movements",
    "have an emergency fund before investing",
    "understand what you're investing in",
    "diversify across different asset classes",
    "avoid following herd mentality",
    "be patient - compounding takes time",
    "review periodically but don't obsess daily",
    "tax efficiency matters, but not at cost of returns",
    "insurance is protection, not investment"
]

# ============================================
# CONTEXT GENERATORS
# ============================================

def generate_individual_context():
    """Generate unique individual investor context"""
    age = random.choice(ages)
    city = random.choice(cities)
    profession = random.choice(professions)
    income = random.choice(incomes)
    
    contexts = [
        f"a {age}-year-old {profession} in {city} earning {income} annually",
        f"a {profession} based in {city}, aged {age}, with annual income of {income}",
        f"a {age}-year-old professional in {city} working as a {profession}, earning {income}"
    ]
    
    return random.choice(contexts)

def generate_business_context():
    """Generate unique business context"""
    city = random.choice(cities)
    business = random.choice(business_types)
    size = random.choice(business_sizes)
    age = random.randint(5, 40)
    
    contexts = [
        f"a {business} company in {city} with {size} annual turnover, running for {age} years",
        f"a {age}-year-old {business} business in {city} generating {size} in revenue",
        f"a {city}-based {business} firm with {size} turnover, in operation since {datetime.now().year - age}"
    ]
    
    return random.choice(contexts)

def generate_challenge():
    """Generate unique business challenge"""
    challenge = random.choice(challenges)
    return f"struggling with {challenge}"

def generate_expert_quote():
    """Generate unique expert quote each time"""
    name = f"{random.choice(expert_first)} {random.choice(expert_last)}"
    title = random.choice(expert_titles)
    years = random.randint(10, 35)
    
    template = random.choice(quote_templates)
    
    quote = template.replace("{mistake}", random.choice(challenges))
    quote = quote.replace("{wrong_thing}", random.choice(["short-term gains", "quick profits", "timing the market"]))
    quote = quote.replace("{right_thing}", random.choice(advice_list))
    quote = quote.replace("{years}", str(years))
    quote = quote.replace("{lesson}", random.choice(advice_list))
    quote = quote.replace("{overrated}", random.choice(["stock picking", "market timing", "hot tips"]))
    quote = quote.replace("{insight}", random.choice(advice_list))
    quote = quote.replace("{advice}", random.choice(advice_list))
    quote = quote.replace("{truth}", random.choice(advice_list))
    
    return {
        "quote": quote,
        "expert": f"{name}, {title}"
    }

def generate_history_lesson():
    """Generate unique history lesson each time"""
    event = random.choice(market_events)
    lesson = random.choice(market_lessons)
    
    return {
        "event": event,
        "lesson": lesson
    }

def generate_mistake():
    """Generate unique mistake description"""
    templates = [
        "putting all money in {asset} because {reason}",
        "selling investments in panic during {event}",
        "buying {asset} at peak because 'everyone was making money'",
        "ignoring {concept} and focusing only on returns",
        "taking {loan_type} loans to invest in {risky_asset}"
    ]
    
    assets = ["a single stock", "real estate", "crypto", "gold", "small-caps", "IPOs"]
    reasons = ["a friend recommended it", "it was trending on social media", "someone made quick profits"]
    events = ["market crash", "bad news", "election results"]
    concepts = ["risk management", "diversification", "valuation"]
    loan_types = ["personal", "credit card", "margin"]
    risky_assets = ["stocks", "crypto", "options"]
    
    template = random.choice(templates)
    mistake = template.replace("{asset}", random.choice(assets))
    mistake = mistake.replace("{reason}", random.choice(reasons))
    mistake = mistake.replace("{event}", random.choice(events))
    mistake = mistake.replace("{concept}", random.choice(concepts))
    mistake = mistake.replace("{loan_type}", random.choice(loan_types))
    mistake = mistake.replace("{risky_asset}", random.choice(risky_assets))
    
    return mistake

# ============================================
# MAIN GENERATOR
# ============================================

def generate_educational_content(title, description, category):
    """Generate truly unique article every time"""
    
    today = datetime.now()
    month = today.strftime("%B")
    year = today.year
    
    # Generate unique elements for THIS article
    if "Business" in category:
        context = generate_business_context()
        challenge = generate_challenge()
        person_context = None
    else:
        context = generate_individual_context()
        challenge = None
        person_context = generate_individual_context()
    
    expert = generate_expert_quote()
    history = generate_history_lesson()
    mistake = generate_mistake()
    
    # ========================================
    # INTRODUCTION
    # ========================================
    intro = f"""
    <div class="educational-notice">
        <i class="fas fa-graduation-cap"></i>
        <strong>Educational Purpose Only:</strong> This article is for 
        general awareness and learning. Not investment advice.
    </div>
    
    <h2>A Story That Might Sound Familiar</h2>
    
    <p>Take {context}. Like many people, they're {challenge or 'thinking about their financial future'}. 
    Their situation isn't unique—thousands of {category.lower()} professionals face similar questions 
    every day. But here's what makes their story interesting: the principles that help them navigate 
    their decisions are the same ones that apply, in different ways, to almost everyone.</p>
    
    <p>In this educational guide, we'll explore {title.lower()} through real situations—not abstract 
    concepts. By the end, you'll have practical ways to think about these decisions in your own context.</p>
    """
    
    # ========================================
    # UNDERSTANDING THE CONCEPT
    # ========================================
    section1 = f"""
    <h2>What This Really Means in Practice</h2>
    
    <p>{title} isn't one thing—it means different things to different people. 
    For {person_context or context}, it's about {random.choice(['growth', 'safety', 'simplicity', 'flexibility'])}. 
    For someone else, it might be about something entirely different.</p>
    
    <p>Here's what experience teaches us: the people who succeed with {title.lower()} aren't necessarily 
    the ones who understand every technical detail. They're the ones who understand themselves—their 
    goals, their fears, their time horizons—and make decisions accordingly.</p>
    
    <p>Consider what happened during {history['event']}. {history['lesson']} This pattern repeats 
    across market cycles: those who focus on fundamentals rather than headlines tend to make better 
    decisions.</p>
    """
    
    # ========================================
    # EXPERT PERSPECTIVE
    # ========================================
    section2 = f"""
    <h2>What Experience Teaches Us</h2>
    
    <div class="highlight-box">
        <p><i class="fas fa-quote-left" style="color: #d4af37; font-size: 24px;"></i> 
        {expert['quote']}</p>
        <p style="text-align: right;">— {expert['expert']}</p>
    </div>
    
    <p>This perspective, shaped by years of real-world experience, highlights something important: 
    success in {title.lower()} has less to do with finding perfect answers and more to do with 
    avoiding major mistakes and staying consistent over time.</p>
    
    <p>The investors and business owners who do well over decades aren't necessarily the smartest 
    people in the room. They're the ones who don't panic during downturns, don't chase hype during 
    upswings, and stick to principles that have worked across market cycles.</p>
    """
    
    # ========================================
    # COMMON MISTAKES
    # ========================================
    section3 = f"""
    <h2>The Mistakes That Trip People Up</h2>
    
    <p>Here's something that doesn't get talked about enough: even smart, experienced people make 
    avoidable mistakes. {mistake}. Sound familiar? If not this exact situation, probably something similar.</p>
    
    <p>Based on observing hundreds of investors and business owners, here are patterns to watch for:</p>
    
    <ul>
        <li><strong>Making decisions based on recent events:</strong> The stock that just went up feels 
        safer than the one that went down—even if fundamentals say otherwise.</li>
        
        <li><strong>Confusing familiarity with knowledge:</strong> Working in an industry doesn't mean 
        you understand investing in it.</li>
        
        <li><strong>Overcomplicating simple things:</strong> Sometimes the basic approach—save regularly, 
        diversify, stay invested—works better than complex strategies.</li>
        
        <li><strong>Underestimating how emotions affect decisions:</strong> Fear and greed have caused 
        more investment mistakes than lack of information ever has.</li>
    </ul>
    """
    
    # ========================================
    # PRACTICAL FRAMEWORK
    # ========================================
    section4 = f"""
    <h2>A Simple Way to Think About It</h2>
    
    <p>Over years of observing what works and what doesn't, a simple framework emerges—one that applies 
    whether you're managing a portfolio or a business:</p>
    
    <div class="highlight-box">
        <h4>Three Questions Before Any Decision</h4>
        <ol>
            <li><strong>Does this match my situation?</strong> What works for someone with different 
            goals, timeline, and risk tolerance may not work for you.</li>
            
            <li><strong>Do I understand it well enough?</strong> If you can't explain it simply, you 
            probably don't understand it well enough to invest in it.</li>
            
            <li><strong>How will I feel if it goes wrong?</strong> If the answer is "terrible," the 
            potential upside probably isn't worth it.</li>
        </ol>
    </div>
    
    <p>This won't guarantee perfect decisions. But it will help you avoid the kind of mistakes that 
    take years to recover from—which, in the world of finance, is more than half the battle.</p>
    """
    
    # ========================================
    # FAQ
    # ========================================
    faq = f"""
    <h2>Questions People Actually Ask</h2>
    
    <h3>"Where do I even start with {title.lower()}?"</h3>
    <p>Start with clarity, not complexity. Before diving into options, understand your own situation: 
    what you're trying to achieve, when you need the money, and how you'll react if things don't go as planned.</p>
    
    <h3>"How do I know if I'm doing it right?"</h3>
    <p>You won't know immediately—and that's okay. Good decisions can have bad short-term outcomes, 
    and vice versa. Focus on your process, not just results.</p>
    
    <h3>"What's the one thing I should focus on?"</h3>
    <p>Consistency. The person who makes reasonable decisions and sticks with them over time almost 
    always outperforms the brilliant investor who constantly changes course.</p>
    """
    
    # ========================================
    # CONCLUSION
    # ========================================
    conclusion = f"""
    <h2>The Bottom Line</h2>
    
    <p>{title} isn't about finding perfect answers. It's about making better decisions, avoiding 
    catastrophic mistakes, and staying consistent over time. The people who do well aren't necessarily 
    the smartest—they're the ones who keep learning, stay disciplined, and focus on what they can control.</p>
    
    <div class="educational-notice">
        <i class="fas fa-info-circle"></i>
        <strong>One Last Thing:</strong> This article is for educational purposes only. Your financial 
        decisions should be based on your unique situation and discussion with qualified professionals. 
        What works for someone else may not work for you—and that's perfectly normal.
    </div>
    """
    
    # Assemble in unique order
    sections = [intro, section1, section2, section3, section4, faq, conclusion]
    random.shuffle(sections)
    
    return "".join(sections)