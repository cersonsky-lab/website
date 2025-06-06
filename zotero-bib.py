import requests
import os
from datetime import datetime

# Configuration from environment or hardcoded fallback
ZOTERO_GROUP_ID = 5070826
ZOTERO_API_KEY = os.environ["ZOTERO_API_KEY"]  # This must be provided via GitHub Actions secret
OUTPUT_FILE = "publications/index.md"

from pyzotero import zotero
zot = zotero.Zotero(ZOTERO_GROUP_ID, "group", ZOTERO_API_KEY) # local=True for read access to local Zotero
items = zot.top()

def format_name(c):
    if c.get('lastName', '') == 'Cersonsky' and not c.get('firstName', '').startswith('T'):
        return f"_**RKC**_"
    return f"{c.get('firstName','')} {c.get('lastName', '')}"

def read_date(date):
    date = str(date).replace('-','/')
    if len(date)==0:
        return 'N/A'
    return tuple(int(x) for x in str(date).split('/'))

def check_key(data, key):
    return key in data and data[key]!=''
ytoday = datetime.now().year

entries = {k: [] for k in range(2014, ytoday+1)}
for item in reversed(sorted(items, key=lambda item: read_date(item.get('date', 0)))):
    data = item.get("data", {})
    if check_key(data, 'date'):
        year = int(read_date(data.get('date'))[0])
        title = data.get("title", "No title")
        creators = data.get("creators", [])
        authors = ", ".join(format_name(c) for c in creators)
        s = f"- **{title}** – {authors}"
        if check_key(data, 'publicationTitle'):
            s += f', _{data["publicationTitle"]}_'
        if check_key(data, 'volume'):
            s += f' _{data["volume"]}_'
        if check_key(data, 'issue'):
            s += f' ({data["issue"]})'
        if check_key(data, 'pages'):
            s += f', {data["pages"]}'
        if check_key(data, 'itemType'):
            if data['itemType'] == 'dataset':
                s = '- **Open Dataset** ' + s
        if check_key(data, 'url'):
            if 'arxiv' in data['url']:
                s+= ', _Preprint_'
            s += f' [Link]({data["url"]})'

        s+= '.\n'
        
        entries[year].append(s)

with open(OUTPUT_FILE, 'w') as outf:
    outf.write('---\nlayout: default\n---\n# Publication List\n')
    for k in reversed(range(2017, ytoday+1)):
        if len(entries[k])>0:
            print(k)
            outf.write(f'\n{k}\n----\n')
            outf.write(''.join(entries[k]))


