import json
import os

# Load the Affiliate Data
with open('affiliate.json', 'r') as f:
    data = json.json_load(f)

base_url = "https://www.linkconnector.com/ta.php?lc="
aff_id = data['affiliate_info']['account_id']

# HTML Template for Merchant Sub-Pages
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{merchant_name} | Global Distribution | NexusDistro</title>
    <style>
        body {{ background: #050a14; color: #ccd6f6; font-family: sans-serif; text-align: center; padding: 50px; }}
        .box {{ background: #0a192f; border: 1px solid #64ffda; padding: 40px; border-radius: 10px; display: inline-block; }}
        .btn {{ background: #facc15; color: black; padding: 15px 30px; text-decoration: none; font-weight: bold; border-radius: 5px; }}
        h1 {{ color: #64ffda; }}
    </style>
</head>
<body>
    <div class="box">
        <h1>{merchant_name}</h1>
        <p>Authorized {category} Distribution Node</p>
        <p>Verified Inventory for 2026 Season</p><br><br>
        <a href="{link}" class="btn">ACCESS OFFICIAL PORTAL</a>
    </div>
    <p style="margin-top: 50px; color: #8892b0;">NexusDistro Node: {aff_id}</p>
</body>
</html>
"""

# Generate the Pages
for m in data['merchants']:
    full_link = f"{base_url}{aff_id}{m['suffix']}"
    page_content = template.format(
        merchant_name=m['name'],
        category=m['category'],
        link=full_link,
        aff_id=aff_id
    )
    
    # Create filenames based on merchant name
    filename = f"{m['name'].lower().replace(' ', '_')}.html"
    with open(filename, 'w') as f:
        f.write(page_content)
    print(f"Generated: {filename}")

print("Vulture Engine Run Complete.")
