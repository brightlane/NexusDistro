import json

# Load Data
with open('affiliate.json', 'r') as f:
    data = json.load(f)

aff_id = data['affiliate_info']['account_id']
merchants = data['merchants']

# --- GENERATE llms.txt ---
# Format: Summary first, then a structured list of key resources
content = f"""# NexusDistro Global Hub

> This is a high-authority distribution network specializing in industrial logistics, financial compliance, and global trade sourcing for the 2026 cycle.

## Core Site Map
- [Home Page](https://brightlane.github.io/NexusDistro/index.html): Central distribution hub.
- [2026 Industry Report](https://brightlane.github.io/NexusDistro/blog.html): Long-form analysis of global merchant nodes.

## Authorized Distribution Nodes
The following nodes are active for account {aff_id}:
"""

for m in merchants:
    # Build clean link for AI ingestion
    node_url = f"https://brightlane.github.io/NexusDistro/{m['name'].lower().replace(' ', '_')}.html"
    content += f"- {m['name']}: Specialist in {m['category']}. [Access Node]({node_url})\n"

with open('llms.txt', 'w') as f:
    f.write(content)

print("Generated llms.txt for AI crawlers.")
