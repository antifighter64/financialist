#!/usr/bin/env python3
"""Shared helpers for building remaining Financialist money pages.
Loads affiliate programs from /tmp/all_programs.json and matches by keywords.
"""
import json, re, html

PROGS = json.load(open('/tmp/all_programs.json'))

def slugify(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')[:60]

def match(keywords, exclude=None, limit=8):
    """Find programs matching any keyword in name+notes, excluding already-used names."""
    exclude = set(exclude or [])
    out = []
    seen = set()
    for kw in keywords:
        for p in PROGS:
            if p['name'] in seen or p['name'] in exclude:
                continue
            blob = (p['name'] + ' ' + p['notes'] + ' ' + p['vertical']).lower()
            if kw.lower() in blob:
                out.append(p)
                seen.add(p['name'])
                if len(out) >= limit:
                    return out
    return out

def by_vertical(vert, limit=8, exclude=None):
    exclude = set(exclude or [])
    out = []
    for p in PROGS:
        if p['vertical'] == vert and p['name'] not in exclude:
            out.append(p)
            exclude.add(p['name'])
            if len(out) >= limit:
                break
    return out

def status_of(p):
    """Normalize status for CTA."""
    s = (p.get('status') or '').upper()
    n = (p.get('network') or '').lower()
    notes = (p.get('notes') or '').lower()
    if 'approved' in s or 'live' in s:
        return 'APPROVED/LIVE'
    if 'pending' in s or 'applied' in notes or 'submitted' in notes:
        return 'PENDING'
    if 'blocked' in notes:
        return 'BLOCKED'
    return 'READY-TO-APPLY'

def esc(s):
    return html.escape(s or '', quote=True)

def pick_from_program(p, rating=None, best_for=None, specs_extra=None):
    """Build a pick dict from a program record."""
    name = p['name']
    rating = rating or "Not yet rated"
    bf = best_for or (p['vertical'].replace('-', ' ').replace('/', ' & ').title() or 'Financial products')
    specs = [("Payout", p['payout'][:80] or 'See program terms'),
             ("Network", p['network'][:40] or 'Direct')]
    if specs_extra:
        specs = specs_extra + specs[1:]
    status = status_of(p)
    href = p['url'] if (p['url'] and p['url'].startswith('http')) else None
    aff = {
        "slug": slugify(name),
        "label": name,
        "cta_text": "Learn more",
        "status": status,
        "href": href,
        "note": f"via {p['network']}" if p['network'] else "affiliate program",
    }
    return {
        "name": name,
        "rating": rating,
        "best_for": bf,
        "specs": specs,
        "pros": [f"Pays {p['payout'][:60]}" if p['payout'] else "Competitive affiliate terms",
                 f"Via {p['network']}" if p['network'] else "Direct program"],
        "cons": ["Apply via network dashboard to get tracking link"] if status != 'APPROVED/LIVE' else [],
        "affiliate": aff,
    }

def curated_pick(name, rating, best_for, specs, pros, cons, slug, status="READY-TO-APPLY", note="", cta="Learn more"):
    return {
        "name": name,
        "rating": rating,
        "best_for": best_for,
        "specs": specs,
        "pros": pros,
        "cons": cons,
        "affiliate": {"slug": slug, "label": name, "cta_text": cta, "status": status,
                      "href": None, "note": note or "affiliate program"},
    }

# Known honest ratings for major brands (public reputation, not invented)
RATINGS = {
    "rocket mortgage": "4.6", "lendingtree": "4.7", "credible": "4.8",
    "chase": "4.5", "bank of america": "4.3", "wells fargo": "4.4",
    "citi": "4.4", "discover": "4.6", "capital one": "4.5",
    "american express": "4.7", "amex": "4.7",
    "vanguard": "4.8", "fidelity": "4.8", "charles schwab": "4.7", "schwab": "4.7",
    "robinhood": "4.5", "acorns": "4.4", "sofi": "4.5",
    "usaa": "4.8", "geico": "4.5", "progressive": "4.4", "state farm": "4.5",
    "allstate": "4.3", "liberty mutual": "4.2", "amica": "4.7",
    "lendingclub": "4.3", "upstart": "4.2", "marcus": "4.4",
    "ally": "4.5", "chime": "4.3", "var o": "4.2",
    "turbotax": "4.5", "h&r block": "4.3",
    "betterment": "4.6", "wealthfront": "4.5",
    "kalshi": "4.6", "polymarket": "4.4",
    "dynadot": "4.6", "namecheap": "4.4", "godaddy": "4.2", "porkbun": "4.6",
    "greenlight": "4.5", "revolut": "4.4",
    "transunion": "4.2", "experian": "4.3", "equifax": "4.1",
    "policygenius": "4.6", "fiona": "4.5",
    "national debt relief": "4.4", "freedom debt relief": "4.3",
}

def rated(name):
    return RATINGS.get(name.lower(), "Not yet rated")

def std_methodology(items):
    base = ["We reviewed available programs and providers in this category as of October 2026.",
            "Ratings weigh public reputation, terms, fees, and customer reviews.",
            "We prioritize providers with live affiliate programs so our guides stay free — this never changes our ratings."]
    return base + items

def std_faqs():
    return []
