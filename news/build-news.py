#!/usr/bin/env python3
"""Build sourced news records from news/articles.json; no network or unverifiable facts."""
from pathlib import Path
from html import escape
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
import json,re
ROOT=Path(__file__).resolve().parent.parent; N=ROOT/'news'; HOST='https://financialist.com'
articles=json.loads((N/'articles.json').read_text()); assert isinstance(articles,list)
original=(ROOT/'index.html').read_text(); css=re.search(r'<style>(.*?)</style>',original,re.S).group(1)
header=re.search(r'<header class="navbar">.*?</header>',original,re.S).group(); footer=re.search(r'<footer>.*?</footer>',original,re.S).group()
h=lambda x:escape(str(x),quote=True)
def display_time(iso, full=True):
 dt=datetime.fromisoformat(iso).astimezone(ZoneInfo('America/New_York'))
 return dt.strftime('%B %-d, %Y at %-I:%M %p %Z' if full else '%B %-d, %Y')
seen=set()
for a in articles:
 for key in ('slug','title','description','author','date_published','date_modified','body','sources','internal_links'):
  if key not in a:raise ValueError('Missing '+key)
 slug=a['slug']
 if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug) or slug in seen or slug.startswith('example-'):raise ValueError('Bad/duplicate slug: '+slug)
 seen.add(slug)
 for key in ('title','description','author'):
  if not isinstance(a[key],str) or not a[key].strip():raise ValueError('Empty '+key)
 for key in ('date_published','date_modified'):
  if datetime.fromisoformat(a[key]).tzinfo is None:raise ValueError('Timestamp needs timezone')
 if datetime.fromisoformat(a['date_modified'])<datetime.fromisoformat(a['date_published']):raise ValueError('Modified before published')
 if not isinstance(a['body'],list) or len(a['body'])<2 or not all(isinstance(x,str) and x.strip() for x in a['body']):raise ValueError('Need original paragraphs')
 if not a['sources'] or not a['internal_links']:raise ValueError('Need sources and internal links')
 for x in a['sources']:
  if not x.get('label') or urlparse(x.get('url','')).scheme!='https' or not urlparse(x['url']).netloc:raise ValueError('Bad source')
 for x in a['internal_links']:
  path=x.get('path','')
  if not x.get('label') or not re.fullmatch('/[a-z0-9/-]+',path):raise ValueError('Bad internal link')
  if not (ROOT/(path.lstrip('/')+'.html')).exists() and not (ROOT/path.lstrip('/')/'index.html').exists():raise ValueError('Internal link missing: '+path)
articles.sort(key=lambda a:a['date_published'],reverse=True)
for a in articles:
 url=HOST+'/news/'+a['slug']; schema={'@context':'https://schema.org','@type':'NewsArticle','headline':a['title'],'description':a['description'],'datePublished':a['date_published'],'dateModified':a['date_modified'],'author':{'@type':'Person','name':a['author']},'publisher':{'@type':'Organization','name':'Financialist','url':HOST},'mainEntityOfPage':url}
 text=''.join('<p>'+h(p)+'</p>' for p in a['body']); sources=''.join('<li><a href="'+h(s['url'])+'">'+h(s['label'])+'</a></li>' for s in a['sources']); links=''.join('<li><a href="'+h(s['path'])+'">'+h(s['label'])+'</a></li>' for s in a['internal_links'])
 body=f'<div class="hero"><div class="container"><div class="crumbs"><a href="/">Home</a> &rsaquo; <a href="/news">News</a></div><h1>{h(a["title"])}</h1><p class="lead">{h(a["description"])}</p><div class="updated">By {h(a["author"])} · <time datetime="{h(a["date_published"])}">{h(display_time(a["date_published"]))}</time></div></div></div><section class="prose"><div class="container"><article>{text}</article><h2>Original sources</h2><div class="sources"><ul>{sources}</ul></div><h2>Related Financialist guides</h2><ul>{links}</ul><p>News is not personalized legal or financial advice.</p></div></section>'
 schema_json=json.dumps(schema,ensure_ascii=False).replace('<',chr(92)+'u003c')
 page=f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{h(a["title"])} | Financialist News</title><meta name="description" content="{h(a["description"])}"><link rel="canonical" href="{url}"><script type="application/ld+json">{schema_json}</script><style>{css}</style></head><body>{header}<main>{body}</main>{footer}</body></html>'
 (N/(a['slug']+'.html')).write_text(page)
cards=''.join(f'<div class="help-card"><h3><a href="/news/{h(a["slug"])}">{h(a["title"])}</a></h3><p>{h(a["description"])}</p><p class="note">By {h(a["author"])} · {h(display_time(a["date_published"],False))}</p></div>' for a in articles)
if not cards:cards='<p>No Financialist news articles have been published yet. Verified reporting will appear here.</p>'
body=f'<div class="hero"><div class="container"><div class="crumbs"><a href="/">Home</a> &rsaquo; News</div><h1>Financialist <span>News</span></h1><p class="lead">Original financial coverage, sourced and connected to practical guides.</p></div></div><section><div class="container"><h2 class="section-title">Latest reporting</h2><div class="help-grid">{cards}</div><p><a href="/money-rights">Browse money-rights guides</a></p></div></section>'
(N/'index.html').write_text(f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Financialist News | Financialist</title><meta name="description" content="Original sourced financial news."><link rel="canonical" href="{HOST}/news"><style>{css}</style></head><body>{header}<main>{body}</main>{footer}</body></html>')
ns0='http://www.sitemaps.org/schemas/sitemap/0.9'; ns1='http://www.google.com/schemas/sitemap-news/0.9';ET.register_namespace('',ns0);ET.register_namespace('news',ns1)
news=ET.Element('{%s}urlset'%ns0); now=datetime.now(timezone.utc)
for a in articles:
 dt=datetime.fromisoformat(a['date_published'])
 if not now-timedelta(days=2)<=dt<=now:continue
 row=ET.SubElement(news,'{%s}url'%ns0);ET.SubElement(row,'{%s}loc'%ns0).text=HOST+'/news/'+a['slug']
 n=ET.SubElement(row,'{%s}news'%ns1);pub=ET.SubElement(n,'{%s}publication'%ns1);ET.SubElement(pub,'{%s}name'%ns1).text='Financialist';ET.SubElement(pub,'{%s}language'%ns1).text='en';ET.SubElement(n,'{%s}publication_date'%ns1).text=a['date_published'];ET.SubElement(n,'{%s}title'%ns1).text=a['title']
ET.ElementTree(news).write(ROOT/'news-sitemap.xml',encoding='utf-8',xml_declaration=True)
main=ROOT/'sitemap.xml';tree=ET.parse(main);r=tree.getroot()
for row in list(r):
 loc=row.find('{%s}loc'%ns0)
 if loc is not None and loc.text and loc.text.startswith(HOST+'/news/') and loc.text!=HOST+'/news':r.remove(row)
for a in articles:
 row=ET.SubElement(r,'{%s}url'%ns0);ET.SubElement(row,'{%s}loc'%ns0).text=HOST+'/news/'+a['slug'];ET.SubElement(row,'{%s}lastmod'%ns0).text=a['date_modified'][:10]
tree.write(main,encoding='utf-8',xml_declaration=True)
print('Built',len(articles),'articles and',len(news),'recent news sitemap entries')
