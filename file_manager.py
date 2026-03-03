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
        
        # Save the file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"✅ Saved blog post: {filename}")
        
        # Update blog index
        self.update_blog_index(title, slug, category, display_date)
        
        # Update homepage preview
        self.update_homepage_preview(title, slug)
        
        # Generate sitemap
        self.generate_sitemap()
        
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
        """Generate sitemap.xml for all blog posts"""
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
        
        for post in blog_posts:
            sitemap_content += f'''  <url>
    <loc>{post['url']}</loc>
    <priority>0.8</priority>
    <lastmod>{post['date']}</lastmod>
    <changefreq>monthly</changefreq>
  </url>
'''
        
        # Add service pages
        service_pages = [
            "services/corporate-advisory.html",
            "services/business-consulting.html", 
            "services/partnership-structuring.html",
            "services/compliance-advisory.html",
            "technology/analytics-platform.html"
        ]
        
        for page in service_pages:
            sitemap_content += f'''  <url>
    <loc>https://omkarservices.in/{page}</loc>
    <priority>0.8</priority>
    <changefreq>monthly</changefreq>
  </url>
'''
        
        # Add legal pages
        legal_pages = [
            "privacy-policy.html",
            "terms-of-service.html", 
            "cookie-policy.html"
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
        
        print(f"✅ Generated sitemap.xml with {len(blog_posts)} posts")
    
    def _get_fallback_template(self):
        """Fallback template if template.html doesn't exist"""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}} | TRFSK OMKAR SERVICES</title>
    <link rel="icon" type="image/x-icon" href="../../assets/favicon.ico">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; max-width: 800px; margin: 50px auto; padding: 0 20px; color: #1e293b; }
        h1 { color: #0f172a; }
        .back-link { color: #d4af37; text-decoration: none; }
    </style>
</head>
<body>
    <h1>{{TITLE}}</h1>
    <p><strong>{{DISPLAY_DATE}}</strong> • {{CATEGORY}}</p>
    {{CONTENT}}
    <hr>
    <a href="../index.html" class="back-link">← Back to Blog</a>
</body>
</html>'''