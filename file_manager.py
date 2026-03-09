import os
import re
from datetime import datetime
from slugify import slugify

class FileManager:
    """Manages blog post files and updates blog index automatically"""
    
    def __init__(self):
        self.blog_post_folder = "blog/post"
        self.blog_index_path = "blog/index.html"
        self.homepage_path = "index.html"
        
        # Create folders if they don't exist
        if not os.path.exists(self.blog_post_folder):
            os.makedirs(self.blog_post_folder)
    
    def save_blog_post(self, title, content, category="Corporate Advisory", read_time=5, author_specialization="corporate advisory"):
        """
        Save a blog post as an HTML file and update indexes
        """
        # Generate slug from title
        slug = slugify(title)
        filename = f"{self.blog_post_folder}/{slug}.html"
        
        # Get current date
        now = datetime.now()
        display_date = now.strftime("%B %d, %Y")
        iso_date = now.strftime("%Y-%m-%d")
        
        # Determine category slug
        category_slug = slugify(category)
        
        # Create description from first 160 chars of content (strip HTML)
        plain_text = re.sub('<[^<]+?>', '', content)
        description = plain_text[:157] + "..." if len(plain_text) > 160 else plain_text
        
        # Load template
        template_path = "blog/post/template.html"
        if os.path.exists(template_path):
            with open(template_path, "r", encoding="utf-8") as f:
                html_template = f.read()
        else:
            # Fallback if template doesn't exist
            html_template = self._get_fallback_template()
        
        # Replace placeholders
        html_content = html_template
        html_content = html_content.replace("{{TITLE}}", title)
        html_content = html_content.replace("{{DESCRIPTION}}", description)
        html_content = html_content.replace("{{KEYWORDS}}", f"{category}, business advisory, {category.lower()}, India")
        html_content = html_content.replace("{{SLUG}}", slug)
        html_content = html_content.replace("{{DATE}}", iso_date)
        html_content = html_content.replace("{{DISPLAY_DATE}}", display_date)
        html_content = html_content.replace("{{CATEGORY}}", category)
        html_content = html_content.replace("{{CATEGORY_SLUG}}", category_slug)
        html_content = html_content.replace("{{READ_TIME}}", str(read_time))
        html_content = html_content.replace("{{AUTHOR_SPECIALIZATION}}", author_specialization)
        html_content = html_content.replace("{{CONTENT}}", content)
        
        # Add lead generation CTA at the end if not present
        if "FREE BUSINESS CONSULTATION" not in html_content:
            lead_cta = """
            <div style="margin-top: 50px; padding: 30px; background: #f8fafc; border-radius: 12px; border: 1px solid #d4af37;">
                <h3 style="color: #0f172a; margin-bottom: 15px;">📞 FREE BUSINESS CONSULTATION</h3>
                <p style="margin-bottom: 20px;">Speak directly with founder Santosh Shendkar about your business needs.</p>
                <div style="display: flex; gap: 20px; flex-wrap: wrap;">
                    <div>
                        <i class="fas fa-envelope" style="color: #d4af37;"></i> 
                        <a href="mailto:consult@omkarservices.in" style="color: #0f172a; text-decoration: none;">consult@omkarservices.in</a>
                    </div>
                    <div>
                        <i class="fas fa-phone" style="color: #d4af37;"></i> 
                        <a href="tel:+917066393830" style="color: #0f172a; text-decoration: none;">+91 70663 93830</a>
                    </div>
                    <div>
                        <i class="fab fa-whatsapp" style="color: #25D366;"></i> 
                        <a href="https://wa.me/917066393830" style="color: #0f172a; text-decoration: none;">WhatsApp</a>
                    </div>
                </div>
                <p style="margin-top: 15px; font-size: 12px; color: #64748b;">Initial consultation is complimentary and creates no obligation.</p>
            </div>
            """
            html_content = html_content.replace("</article>", lead_cta + "\n</article>")
        
        # Save the file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"✅ Saved blog post: {filename}")
        
        # Update blog index
        self.update_blog_index(title, slug, category, display_date)
        
        # Update homepage preview
        self.update_homepage_preview(title, slug)
        
        return slug
    
    def update_blog_index(self, title, slug, category, date):
        """Update blog/index.html with new post"""
        if not os.path.exists(self.blog_index_path):
            print(f"⚠️ Blog index not found: {self.blog_index_path}")
            return
        
        with open(self.blog_index_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Create new blog entry HTML
        new_entry = f'''
                <a href="post/{slug}.html" class="service-card">
                    <h3>{title}</h3>
                    <p>Educational insights and structured advisory analysis.</p>
                    <div class="blog-meta">{date} • {category}</div>
                    <span style="color: #d4af37;">Read More →</span>
                </a>
                
                <!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->'''
        
        # Replace the marker with new entry + marker
        if "<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->" in content:
            updated_content = content.replace("<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->", new_entry)
            
            with open(self.blog_index_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            
            print(f"✅ Updated blog index with: {title}")
        else:
            print("⚠️ AUTO BLOG INSERT marker not found in blog/index.html")
    
    def update_homepage_preview(self, title, slug):
        """Update homepage with latest post preview"""
        if not os.path.exists(self.homepage_path):
            return
        
        with open(self.homepage_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if homepage has the auto insert marker
        if "<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->" in content:
            new_preview = f'''
                <a href="blog/post/{slug}.html" class="service-card">
                    <h3>{title}</h3>
                    <p>Educational insights and structured advisory analysis.</p>
                </a>
                
                <!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->'''
            
            updated_content = content.replace("<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->", new_preview)
            
            with open(self.homepage_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            
            print(f"✅ Updated homepage preview with: {title}")
    
    def generate_sitemap(self):
        """Generate sitemap.xml for all blog posts and pages"""
        sitemap_path = "sitemap.xml"
        
        # Get all blog posts
        blog_posts = []
        if os.path.exists(self.blog_post_folder):
            for filename in os.listdir(self.blog_post_folder):
                if filename.endswith(".html") and filename != "template.html":
                    slug = filename.replace(".html", "")
                    blog_posts.append({
                        "slug": slug,
                        "url": f"https://omkarservices.in/blog/post/{slug}.html",
                        "date": datetime.now().strftime("%Y-%m-%d")
                    })
        
        # Get all service pages
        service_pages = [
            "services/corporate-advisory.html",
            "services/business-consulting.html",
            "services/partnership-structuring.html",
            "services/compliance-advisory.html"
        ]
        
        # Get all pillar pages
        pillar_pages = [
            "capital-deployment-model.html",
            "documentation-process.html",
            "transparency-compliance.html",
            "about-founder.html",
            "case-studies.html",
            "faq.html",
            "contact.html"
        ]
        
        # Generate sitemap XML
        sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://omkarservices.in/</loc>
    <priority>1.0</priority>
    <changefreq>daily</changefreq>
  </url>
  <url>
    <loc>https://omkarservices.in/blog/index.html</loc>
    <priority>0.9</priority>
    <changefreq>daily</changefreq>
  </url>
'''
        
        # Add pillar pages
        for page in pillar_pages:
            sitemap_content += f'''  <url>
    <loc>https://omkarservices.in/{page}</loc>
    <priority>0.9</priority>
    <changefreq>weekly</changefreq>
  </url>
'''
        
        # Add service pages
        for page in service_pages:
            sitemap_content += f'''  <url>
    <loc>https://omkarservices.in/{page}</loc>
    <priority>0.8</priority>
    <changefreq>weekly</changefreq>
  </url>
'''
        
        # Add blog posts
        for post in blog_posts:
            sitemap_content += f'''  <url>
    <loc>{post['url']}</loc>
    <priority>0.8</priority>
    <lastmod>{post['date']}</lastmod>
    <changefreq>monthly</changefreq>
  </url>
'''
        
        # Add legal pages
        legal_pages = [
            "privacy-policy.html",
            "terms-of-service.html",
            "cookie-policy.html",
            "kyc-policy.html",
            "risk-disclosure.html"
        ]
        
        for page in legal_pages:
            sitemap_content += f'''  <url>
    <loc>https://omkarservices.in/{page}</loc>
    <priority>0.5</priority>
    <changefreq>yearly</changefreq>
  </url>
'''
        
        sitemap_content += '''</urlset>'''
        
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
        
        print(f"✅ Generated sitemap.xml with {len(blog_posts)} posts and {len(pillar_pages) + len(service_pages) + len(legal_pages)} pages")
    
    def _get_fallback_template(self):
        """Fallback template if template.html doesn't exist"""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}} | TRFSK OMKAR SERVICES</title>
    <meta name="description" content="{{DESCRIPTION}}">
    <meta name="keywords" content="{{KEYWORDS}}">
    <meta name="author" content="Santosh Shendkar">
    <link rel="canonical" href="https://omkarservices.in/blog/post/{{SLUG}}.html">
    <link rel="icon" type="image/x-icon" href="../../assets/favicon.ico">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* Include your global styles here */
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; max-width: 900px; margin: 50px auto; padding: 0 20px; color: #1e293b; background: #f8fafc; }
        h1 { color: #0f172a; }
        h2 { color: #1e293b; margin-top: 40px; }
        .note { background: #fef3c7; border-left: 4px solid #d4af37; padding: 20px; border-radius: 8px; margin: 30px 0; }
        .back-link { color: #d4af37; text-decoration: none; font-weight: 600; }
        blockquote { background: #f1f5f9; border-left: 4px solid #d4af37; padding: 20px; margin: 30px 0; border-radius: 0 8px 8px 0; }
    </style>
</head>
<body>
    <h1>{{TITLE}}</h1>
    <p><strong>{{DISPLAY_DATE}}</strong> • {{CATEGORY}} • {{READ_TIME}} min read</p>
    {{CONTENT}}
    <hr>
    <a href="../index.html" class="back-link">← Back to Blog</a>
</body>
</html>'''
