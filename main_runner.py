#!/usr/bin/env python3
"""
Main runner for auto-blog generation
Run this script to generate new blog posts
"""

import sys
import os
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from file_manager import FileManager

def main():
    """Main function to generate blog posts"""
    
    # Initialize file manager
    fm = FileManager()
    
    # Example: Generate a sample blog post
    # You can replace this with your actual content generation logic
    
    title = "Understanding Corporate Governance in 2026"
    
    content = """
    <h2>Introduction</h2>
    <p>Corporate governance continues to evolve in 2026 with new regulations and best practices emerging. This article explores the key principles that every business should understand.</p>
    
    <h2>Key Principles of Corporate Governance</h2>
    <ul>
        <li><strong>Transparency:</strong> Clear disclosure of material matters to stakeholders</li>
        <li><strong>Accountability:</strong> Clear lines of responsibility and decision-making</li>
        <li><strong>Fairness:</strong> Equal treatment of all stakeholders including minority shareholders</li>
        <li><strong>Responsibility:</strong> Ethical business conduct and compliance with laws</li>
    </ul>
    
    <h2>Why Governance Matters for Private Companies</h2>
    <p>Even private companies benefit from strong governance practices. Good governance:</p>
    <ul>
        <li>Builds credibility with banks and investors</li>
        <li>Improves decision-making processes</li>
        <li>Reduces risk of disputes and compliance issues</li>
        <li>Attracts quality talent and partners</li>
    </ul>
    
    <h2>Implementing Governance in Your Business</h2>
    <p>Start with these fundamental steps:</p>
    <ol>
        <li>Document key policies and procedures</li>
        <li>Establish regular board meetings with proper minutes</li>
        <li>Separate ownership from management roles</li>
        <li>Implement internal controls and audits</li>
    </ol>
    
    <div class="note">
        <p><strong>Important:</strong> Governance requirements vary based on company size and structure. Consult with professionals to determine what applies to your business.</p>
    </div>
    
    <h2>Conclusion</h2>
    <p>Good governance is not just about compliance—it's about building a sustainable, trustworthy business that can grow with confidence. Start implementing basic governance practices today, and evolve them as your company grows.</p>
    """
    
    # Save the blog post
    slug = fm.save_blog_post(
        title=title,
        content=content,
        category="Corporate Advisory",
        read_time=4,
        author_specialization="corporate governance and compliance"
    )
    
    print(f"✅ Blog post generated successfully: {slug}.html")
    print("✅ Sitemap updated")

if __name__ == "__main__":
    main()
