import json
import os

# 1. Load Data
with open('affiliate.json', 'r') as f:
    data = json.load(f)

aff_id = data['affiliate_info']['account_id']
merchants = data['merchants']
base_url = "https://www.linkconnector.com/ta.php?lc="

# --- CONFIG & TEMPLATES ---

# Template for the 28 individual Merchant Nodes
MERCHANT_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{name} | NexusDistro Node</title>
    <style>
        body {{ background: #050a14; color: #ccd6f6; font-family: sans-serif; text-align: center; padding: 100px; }}
        .box {{ border: 1px solid #64ffda; padding: 50px; border-radius: 12px; background: #0a192f; display: inline-block; }}
        .btn {{ background: #facc15; color: #000; padding: 20px 40px; text-decoration: none; font-weight: bold; border-radius: 5px; font-size: 1.2rem; }}
        h1 {{ color: #64ffda; margin-bottom: 30px; }}
    </style>
</head>
<body>
    <div class="box">
        <h1>{name}</h1>
        <p>Authorized {category} Distribution Node</p><br><br>
        <a href="{link}" class="btn">ACCESS OFFICIAL PORTAL</a>
    </div>
</body>
</html>
"""

# Template for the Main Home Page (index.html)
INDEX_START = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>NexusDistro | Global Distribution Network</title>
    <style>
        body { background: #050a14; color: #ccd6f6; font-family: sans-serif; margin: 0; }
        header { padding: 50px; text-align: center; background: #0a192f; border-bottom: 1px solid #112240; }
        .nav-links { margin-top: 20px; }
        .nav-links a { color: #64ffda; margin: 0 15px; text-decoration: none; font-weight: bold; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; padding: 40px; max-width: 1200px; margin: auto; }
        .card { background: #0a192f; border: 1px solid #112240; padding: 20px; border-radius: 10px; text-align: center; transition: 0.3s; }
        .card:hover { border-color: #64ffda; transform: translateY(-5px); }
        .card h3 { color: #64ffda; margin: 0 0 10px 0; }
        .btn { color: #facc15; text-decoration: none; font-size: 0.9rem; font-weight: bold; border: 1px solid #facc15; padding: 5px 10px; border-radius: 4px; }
    </style>
</head>
<body>
    <header>
        <h1>NexusDistro</h1>
        <p>Global Affiliate Distribution Node: 007949</p>
        <div class="nav-links">
            <a href="index.html">Home</a>
            <a href="blog.html">2026 Industry Report</a>
        </div>
    </header>
    <div class="grid">
"""

# Template for the Mega-Blog (blog.html)
BLOG_START = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The NexusDistro Authority Blog | 2026 Global Sourcing Guide</title>
    <style>
        body { background: #050a14; color: #ccd6f6; font-family: 'Segoe UI', sans-serif; line-height: 1.8; margin: 0;}
        header { padding: 30px; text-align: center; background: #0a192f; border-bottom: 1px solid #112240; }
        header a { color: #64ffda; text-decoration: none; }
        .content { max-width: 900px; margin: 0 auto; padding: 60px 20px; }
        h1 { color: #64ffda; font-size: 3rem; border-bottom: 2px solid #112240; padding-bottom: 20px; }
        h2 { color: #facc15; margin-top: 50px; font-size: 2rem; }
        .cta-box { background: #0a192f; border-left: 4px solid #64ffda; padding: 20px; margin: 20px 0; }
        .cta-link { color: #64ffda; font-weight: bold; text-decoration: none; border-bottom: 1px solid; }
        p { margin-bottom: 25px; font-size: 1.1rem; color: #8892b0; }
    </style>
</head>
<body>
    <header><a href="index.html">← Back to Global Hub</a></header>
    <div class="content">
        <h1>Global Sourcing & Compliance: The 2026 Master Guide</h1>
        <p>Welcome to the NexusDistro Authority Archive. This comprehensive guide covers the intersection of industrial logistics, financial compliance, and global trade.</p>
"""

# --- PROCESSING LOOP ---

sitemap_urls = [
    '  <url><loc>https://brightlane.github.io/NexusDistro/index.html</loc><priority>1.0</priority></url>',
    '  <url><loc>https://brightlane.github.io/NexusDistro/blog.html</loc><priority>0.9</priority></url>'
]
index_cards = ""
blog_body = ""

for m in merchants:
    full_link = f"{base_url}{aff_id}{m['suffix']}"
    filename = f"{m['name'].lower().replace(' ', '_').replace('.', '_')}.html"
    
    # 1. Create Merchant Page
    with open(filename, 'w') as f:
        f.write(MERCHANT_TEMPLATE.format(name=m['name'], category=m['category'], link=full_link))
    
    # 2. Add to Index Grid
    index_cards += f"""
        <div class="card">
            <h3>{m['name']}</h3>
            <p>{m['category']}</p>
            <a href="{filename}" class="btn">View Portal</a>
        </div>
    """

    # 3. Add to Blog Body
    blog_body += f"""
    <section id="{m['name'].lower()}">
        <h2>Chapter: Understanding {m['category']} with {m['name']}</h2>
        <p>In the evolving landscape of 2026, {m['category']} has become a cornerstone of global operations. 
        When professionals look for reliability in {m['name']}, they are looking for a tradition of excellence 
        and a robust supply chain that can withstand market fluctuations.</p>
        
        <p>Strategic sourcing in the {m['category']} sector requires an understanding of both local regulations 
        and international standards. Whether you are scaling a startup or managing a multinational warehouse, 
        the tools provided by {m['name']} ensure that your technical requirements are met with precision.</p>

        <div class="cta-box">
            <strong>Professional Resource:</strong> Access the full {m['name']} inventory and compliance 
            documentation via our authorized portal: 
            <a href="{full_link}" class="cta-link">Visit {m['name']} Distribution Node</a>
        </div>
    </section>
    <hr style="border: 0; border-top: 1px solid #112240; margin: 60px 0;">
    """
    
    # 4. Add to Sitemap
    sitemap_urls.append(f'  <url><loc>https://brightlane.github.io/NexusDistro/{filename}</loc><priority>0.8</priority></url>')

# --- FINAL FILE WRITING ---

# Save index.html
with open('index.html', 'w') as f:
    f.write(INDEX_START + index_cards + "\n    </div>\n</body>\n</html>")

# Save blog.html
with open('blog.html', 'w') as f:
    f.write(BLOG_START + blog_body + "\n    </div>\n</body>\n</html>")

# Save sitemap.xml
s_header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
with open('sitemap.xml', 'w') as s:
    s.write(s_header + "\n".join(sitemap_urls) + '\n</urlset>')

print(f"Vulture Engine: Successfully built Hub, Blog, and {len(merchants)} Merchant Nodes.")
