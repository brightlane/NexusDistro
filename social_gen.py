import json
import random

# Load Merchant Data
with open('affiliate.json', 'r') as f:
    data = json.load(f)

merchants = data['merchants']
aff_id = data['affiliate_info']['account_id']
base_url = "https://www.linkconnector.com/ta.php?lc="

# Social Media Templates
templates = [
    "Looking for verified {category} solutions in 2026? NexusDistro has authorized access to {name}. #SupplyChain #GlobalTrade",
    "Scaling your operations? Our {category} node for {name} is live with updated 2026 inventory. Check it here:",
    "Industry Alert: {name} is currently a top-tier provider for {category} compliance and supplies. #Logistics #Business",
    "Authorized Distribution Update: {name} portal is now synced for the 2026 season. Node {aff_id}."
]

social_posts = []

# Generate 3 random posts per day
daily_selection = random.sample(merchants, 3)

for m in daily_selection:
    link = f"{base_url}{aff_id}{m['suffix']}"
    post = random.choice(templates).format(
        category=m['category'], 
        name=m['name'], 
        aff_id=aff_id
    )
    social_posts.append(f"{post} {link}")

# Save to a file for your automation tools to read
with open('social_queue.txt', 'w') as f:
    f.write("\n---\n".join(social_posts))

print("Daily social media queue generated.")
