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
        
        # List of category files to update
        self.category_files = [
            "blog/category/corporate-advisory.html",
            "blog/category/technology-analytics.html",
            "blog/category/compliance.html",
            "blog/category/business-strategy.html",
            "blog/category/stock-market-knowledge.html",
            "blog/category/capital-deployment.html"
        ]
        
        # List of service pages to update
        self.service_pages = [
            "services/corporate-advisory.html",
            "services/business-consulting.html",
            "services/compliance-advisory.html",
            "services/partnership-structuring.html"
        ]
        
        # Create folders if they don't exist
        os.makedirs(self.blog_post_folder, exist_ok=True)
        for file_path in self.category_files:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
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
        
        # Generate keywords from title and category
        keywords = f"{category}, {title}, educational content, financial awareness, business education"
        
        # Load template
        template_path = "blog/post/template.html"
        if os.path.exists(template_path):
            with open(template_path, "r", encoding="utf-8") as f:
                html_template = f.read()
        else:
            print(f"⚠️ Template not found at {template_path}")
            return None
        
        # Replace placeholders
        html_content = html_template
        html_content = html_content.replace("{{TITLE}}", title)
        html_content = html_content.replace("{{DESCRIPTION}}", description)
        html_content = html_content.replace("{{KEYWORDS}}", keywords)
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
        
        # Update all indexes
        self.update_blog_index(title, slug, category, display_date)
        self.update_category_pages(title, slug, category, display_date)
        self.update_service_pages(title, slug, category, display_date)
        self.update_homepage_preview(title, slug)
        
        return slug
    
    def update_blog_index(self, title, slug, category, date):
        """Update blog/index.html with new post at TOP"""
        if not os.path.exists(self.blog_index_path):
            print(f"⚠️ Blog index not found: {self.blog_index_path}")
            return
        
        with open(self.blog_index_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Create new blog entry HTML
        new_entry = f'''
                <!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->
                <article class="blog-card fade-in">
                    <div class="new-badge">NEW</div>
                    <div class="blog-image">
                        <i class="fas fa-file-alt" style="font-size: 60px; color: #d4af37;"></i>
                    </div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <div class="blog-date">
                                <i class="fas fa-calendar-alt"></i> {date}
                            </div>
                            <div class="blog-category">{category}</div>
                        </div>
                        <h3>
                            <a href="post/{slug}.html">{title}</a>
                        </h3>
                        <p class="blog-excerpt">Educational content on {category}. For learning purposes only.</p>
                        <a href="post/{slug}.html" class="read-more">
                            Read Article <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </article>
                
                <!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->'''
        
        # Replace the marker with new entry + marker
        if "<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->" in content:
            updated_content = content.replace("<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->", new_entry)
            
            with open(self.blog_index_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            
            print(f"✅ Updated blog index with: {title}")
        else:
            print("⚠️ AUTO BLOG INSERT marker not found in blog/index.html")
    
    def update_category_pages(self, title, slug, category, date):
        """Update category pages with new post"""
        for cat_file in self.category_files:
            if not os.path.exists(cat_file):
                continue
                
            with open(cat_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Simple entry for category pages
            new_entry = f'''
                <!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->
                <a href="../post/{slug}.html" class="blog-card">
                    <div class="blog-image">
                        <i class="fas fa-file-alt" style="font-size: 48px; color: #d4af37;"></i>
                    </div>
                    <div class="blog-content">
                        <div class="blog-category">{category}</div>
                        <h3>{title}</h3>
                        <p class="blog-excerpt">Educational content. For learning purposes only.</p>
                        <div class="blog-meta">
                            <span><i class="far fa-calendar-alt"></i> {date}</span>
                        </div>
                    </div>
                </a>
                
                <!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->'''
            
            if "<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->" in content:
                updated_content = content.replace("<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->", new_entry)
                
                with open(cat_file, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                
                print(f"✅ Updated {os.path.basename(cat_file)}")
    
    def update_service_pages(self, title, slug, category, date):
        """Update service pages with latest post preview"""
        for service_file in self.service_pages:
            if not os.path.exists(service_file):
                continue
                
            with open(service_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_entry = f'''
                <!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->
                <a href="../blog/post/{slug}.html" class="service-card">
                    <h3>{title}</h3>
                    <p>Educational insights and structured advisory analysis.</p>
                    <div class="blog-meta">{date} • {category}</div>
                    <span style="color: #d4af37;">Read More →</span>
                </a>
                
                <!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->'''
            
            if "<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->" in content:
                updated_content = content.replace("<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->", new_entry)
                
                with open(service_file, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                
                print(f"✅ Updated {os.path.basename(service_file)}")
    
    def update_homepage_preview(self, title, slug):
        """Update homepage with latest post preview"""
        if not os.path.exists(self.homepage_path):
            return
        
        with open(self.homepage_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if homepage has the auto insert marker
        if "<!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->" in content:
            new_preview = f'''
                <!-- AUTO BLOG INSERT - DO NOT REMOVE THIS COMMENT -->
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
        
        # Get current date for lastmod
        today = datetime.now().strftime("%Y-%m-%d")
        
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
        
        # Add category pages
        categories = [
            "corporate-advisory",
            "technology-analytics",
            "compliance",
            "business-strategy",
            "stock-market-knowledge",
            "capital-deployment"
        ]
        
        for cat in categories:
            sitemap_content += f'''  <url>
    <loc>https://omkarservices.in/blog/category/{cat}.html</loc>
    <priority>0.8</priority>
    <changefreq>weekly</changefreq>
  </url>
'''
        
        # Add service pages
        services = [
            "services/corporate-advisory",
            "services/business-consulting",
            "services/compliance-advisory",
            "services/partnership-structuring"
        ]
        
        for service in services:
            sitemap_content += f'''  <url>
    <loc>https://omkarservices.in/{service}.html</loc>
    <priority>0.8</priority>
    <changefreq>weekly</changefreq>
  </url>
'''
        
        # Add technology page
        sitemap_content += f'''  <url>
    <loc>https://omkarservices.in/technology/analytics-platform.html</loc>
    <priority>0.8</priority>
    <changefreq>weekly</changefreq>
  </url>
'''
        
        # Add founder page
        sitemap_content += f'''  <url>
    <loc>https://omkarservices.in/about-founder.html</loc>
    <priority>0.8</priority>
    <changefreq>monthly</changefreq>
  </url>
'''
        
        # Add blog posts
        for post in blog_posts[-50:]:  # Last 50 posts only to keep sitemap manageable
            sitemap_content += f'''  <url>
    <loc>{post['url']}</loc>
    <priority>0.7</priority>
    <lastmod>{post['date']}</lastmod>
    <changefreq>monthly</changefreq>
  </url>
'''
        
        # Add legal pages
        legal_pages = [
            "privacy-policy",
            "terms-of-service",
            "cookie-policy",
            "kyc-policy"
        ]
        
        for page in legal_pages:
            sitemap_content += f'''  <url>
    <loc>https://omkarservices.in/{page}.html</loc>
    <priority>0.5</priority>
    <changefreq>yearly</changefreq>
  </url>
'''
        
        sitemap_content += '''</urlset>'''
        
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
        
        print(f"✅ Generated sitemap.xml with {len(blog_posts)} posts")
