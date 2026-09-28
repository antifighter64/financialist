#!/usr/bin/env python3
"""Regenerate news/feed.xml from news/articles.json after each daily publish."""
import json, html, sys, os
from email.utils import format_datetime
from datetime import datetime, timezone, timedelta
os.chdir(os.path.dirname(os.path.abspath(__file__)))
arts=json.load(open('articles.json'))
items=[]
for a in arts:
    try:
        dt=datetime.fromisoformat(a['date_published'])
        if dt.tzinfo is None: dt=dt.replace(tzinfo=timezone(timedelta(hours=-4)))
    except Exception:
        dt=datetime.now(timezone.utc)
    slug=a['slug']
    items.append(f'''  <item>\n   <title>{html.escape(a['title'])}</title>\n   <link>https://financialist.com/news/{slug}</link>\n   <guid isPermaLink="true">https://financialist.com/news/{slug}</guid>\n   <description>{html.escape(a.get('description',''))}</description>\n   <author>{html.escape(a.get('author','Financialist'))}</author>\n   <pubDate>{format_datetime(dt)}</pubDate>\n  </item>''')
feed=f'''<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n <channel>\n  <title>Financialist News</title>\n  <link>https://financialist.com/news</link>\n  <atom:link href="https://financialist.com/news/feed.xml" rel="self" type="application/rss+xml"/>\n  <description>Daily money news from Financialist: debt relief, consumer rights, insurance, banking and your money.</description>\n  <language>en-us</language>\n{chr(10).join(items)}\n </channel>\n</rss>'''
open('feed.xml','w').write(feed)
print('feed.xml regenerated:',len(items),'items')
