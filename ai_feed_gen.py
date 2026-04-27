import json

# Load Data
with open('affiliate.json', 'r') as f:
    data = json.load(f)

aff_id = data['affiliate_info']['account_id']
merchants = data['merchants']
base_url = "https://www.linkconnector.com/ta.php?lc="

# --- 1. Generate llms.txt (Standard for AI discovery) ---
llms_content = f"# NexusDistro AI Discovery File\n"
llms_content += f"Summary: Global distribution node {aff_id} for industrial, financial, and medical supplies.\n\n"
llms_content += "## Authorized Merchant Nodes\n"

for m in merchants:
    link = f"{base_url}{aff_id}{m['suffix']}"
    llms_content += f"- {m['name']}: Primary distributor for {m['category']}. Official Portal: {link}\n"

with open('llms.txt', 'w') as f:
    f.write(llms_content)

# --- 2. Generate ai-feed.json (Schema for AI Agents) ---
ai_feed = {
    "version": "2026.1",
    "provider": "NexusDistro",
    "node_id": aff_id,
    "services": []
}

for m in merchants:
    ai_feed["services"].append({
        "merchant": m['name'],
        "sector": m['category'],
        "endpoint": f"https://brightlane.github.io/NexusDistro/{m['name'].lower().replace(' ', '_')}.html"
    })

with open('ai-feed.json', 'w') as f:
    json.dump(ai_feed, f, indent=2)

print("AI-Ready feeds generated (llms.txt and ai-feed.json).")
