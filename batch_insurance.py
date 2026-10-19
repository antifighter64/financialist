#!/usr/bin/env python3
"""Batch: Insurance sub-pages (11 pages)."""
import sys
sys.path.insert(0, '.')
from generate import write_page
from page_helpers import PROGS, pick_from_program, curated_pick, rated, std_methodology

MONTH = "October 2026"

INS_BRANDS = [
    ("Liberty Mutual", "4.2", "Customizable policies",
     [("Auto lead", "$10"), ("Home lead", "$10"), ("Renters", "$3")],
     ["Highly customizable coverage", "Many discounts"],
     ["Customer service varies"],
     "liberty-mutual", "PENDING", "via CJ/FlexOffers"),
    ("Allstate", "4.3", "Agent network + digital",
     [("Auto lead", "~$5-8"), ("Home lead", "$28"), ("Agents", "Nationwide")],
     ["Local agents", "Strong digital tools"],
     ["Prices vary widely"],
     "allstate", "PENDING", "via Impact/CJ"),
    ("Esurance", "4.3", "Allstate-owned, online-first",
     [("Lead", "$10"), ("Best for", "Digital shoppers"), ("Parent", "Allstate")],
     ["Fully online quotes", "Competitive rates"],
     ["No local agents"],
     "esurance", "PENDING", "via FlexOffers"),
    ("USAA", "4.8", "Military families",
     [("Best for", "Military"), ("Service", "Top-rated"), ("Rates", "Excellent")],
     ["Best customer satisfaction", "Great rates for eligible"],
     ["Military affiliation required"],
     "usaa", "READY-TO-APPLY", "military eligibility required"),
    ("GEICO", "4.5", "Low rates, gecko",
     [("Best for", "Low rates"), ("Discounts", "Many"), ("App", "Highly rated")],
     ["Consistently cheap", "Easy online experience"],
     ["Fewer local agents"],
     "geico", "READY-TO-APPLY", "affiliate program"),
    ("Progressive", "4.4", "Comparison + Snapshot",
     [("Best for", "High-risk drivers"), ("Tool", "Name Your Price"), ("Snapshot", "Usage discount")],
     ["Good for imperfect records", "Snapshot saves safe drivers"],
     ["Rate hikes reported"],
     "progressive", "READY-TO-APPLY", "affiliate program"),
    ("State Farm", "4.5", "Biggest agent network",
     [("Best for", "In-person service"), ("Agents", "19,000+"), ("Bundling", "Strong")],
     ["Local agents everywhere", "Great bundling discounts"],
     ["Online experience lags"],
     "state-farm", "READY-TO-APPLY", "affiliate program"),
    ("Amica", "4.7", "Top customer satisfaction",
     [("Best for", "Service"), ("Satisfaction", "#1"), ("Dividends", "Possible")],
     ["Highest satisfaction scores", "Dividend policies"],
     ["Higher premiums", "Fewer discounts"],
     "amica", "READY-TO-APPLY", "affiliate program"),
    ("NetQuote", "4.3", "Compare multiple insurers",
     [("Lead", "$24"), ("Best for", "Comparison"), ("Quotes", "Multiple")],
     ["One form, many quotes", "$24/lead payout"],
     ["Expect follow-up calls"],
     "netquote", "READY-TO-APPLY", "direct"),
    ("Policygenius", "4.6", "Insurance marketplace",
     [("Best for", "Comparison"), ("Products", "Life, home, auto"), ("Cost", "Free")],
     ["Compare top insurers", "Unbiased quotes"],
     ["Not an insurer itself"],
     "policygenius", "READY-TO-APPLY", "verify in CJ dashboard"),
]

def bp(b):
    n, r, bf, sp, pr, co, sl, st, nt = b
    return curated_pick(n, r, bf, sp, pr, co, sl, st, nt)

BRANDS = [bp(b) for b in INS_BRANDS]

def ins_progs(keywords, n=4):
    picks, seen = [], set()
    for kw in keywords:
        for p in PROGS:
            if p['name'] in seen: continue
            blob = (p['name'] + ' ' + p['notes']).lower()
            if kw.lower() in blob and 'insurance' in blob:
                picks.append(pick_from_program(p, rating=rated(p['name'])))
                seen.add(p['name'])
                if len(picks) >= n: return picks
    return picks

def C(*a):
    return [("/", "Home"), ("/insurance", "Insurance")] + list(a)

def make(url_path, file_path, crumbs, title, h1, lead, meta, ct, cs, intro, picks, faqs):
    write_page(file_path, {
        "title": title, "url": url_path, "vertical": "insurance",
        "crumbs": crumbs, "h1": h1, "lead": lead, "meta": meta,
        "compare_title": ct, "compare_sub": cs, "intro": intro,
        "picks": picks, "methodology": std_methodology([]), "faqs": faqs,
    })

PAGES = [
 ("/insurance", "insurance/index.html", C(),
  f"Best Insurance Companies of {MONTH}", f"Best Insurance Companies of {MONTH}",
  "Auto, home, life, and more — the best insurance companies compared.",
  f"Best insurance companies of {MONTH}. Auto, home, and life insurance compared.",
  "the best insurance companies", "Every coverage, ranked.",
  "The right insurer balances price, coverage, and claims service. Best across categories.",
  BRANDS[:6] + ins_progs(["insurance marketplace"], 2),
  [("How to choose an insurer?", "Compare price AND claims satisfaction — cheap means nothing if claims are denied."),
   ("Bundle discounts?", "Bundling auto+home typically saves 10-25%."),
   ("How often to shop?", "Every 1-2 years, or after major life changes.")] ),
 ("/insurance/life", "insurance/life.html", C(("/insurance/life","Life")),
  f"Best Life Insurance Companies of {MONTH}", f"Best Life Insurance Companies of {MONTH}",
  "Term life from $20/month. The most reputable life insurers compared.",
  f"Best life insurance of {MONTH}. Term life companies with top financial strength.",
  "the best life insurance companies", "Protect what matters.",
  "Term life is cheap peace of mind. These insurers have the strength to pay claims.",
  BRANDS[9:10] + ins_progs(["life insurance", "gerber", "fabric"], 4) + BRANDS[3:4],
  [("How much coverage?", "10-12x annual income is a common rule; use a calculator for precision."),
   ("Term or whole?", "Term for most — cheaper, simpler. Whole life is rarely worth the cost."),
   ("Medical exam?", "Many insurers now offer no-exam term up to $1M+.")] ),
 ("/insurance/renters", "insurance/renters.html", C(("/insurance/renters","Renters")),
  f"Best Renters Insurance of {MONTH}", f"Best Renters Insurance of {MONTH}",
  "Protect your stuff for ~$15/month. The best renters insurance compared.",
  f"Best renters insurance of {MONTH}. Affordable coverage for renters compared.",
  "the best renters insurance", "$15/month peace of mind.",
  "Renters insurance is the best deal in insurance. These are the top picks.",
  BRANDS[:3] + BRANDS[7:8] + ins_progs(["renters"], 2),
  [("What does it cover?", "Your belongings, liability, and temporary housing after covered events."),
   ("Landlord's insurance?", "Covers the building only — not your stuff."),
   ("Cost?", "Typically $15-20/month; often cheaper bundled with auto.")] ),
 ("/insurance/umbrella", "insurance/umbrella.html", C(("/insurance/umbrella","Umbrella")),
  f"Best Umbrella Insurance of {MONTH}", f"Best Umbrella Insurance of {MONTH}",
  "Extra $1M+ liability protection for ~$300/year. Best umbrella policies.",
  f"Best umbrella insurance of {MONTH}. Extra liability protection compared.",
  "the best umbrella insurance", "Sleep better for $300/year.",
  "Umbrella insurance is cheap catastrophic protection. Best options here.",
  BRANDS[:4] + BRANDS[6:7],
  [("What is umbrella?", "Extra liability coverage above auto/home limits — typically $1M+."),
   ("Who needs it?", "Homeowners, high earners, landlords, dog owners, teen drivers."),
   ("Requirements?", "Usually requires underlying auto/home policies at set minimums.")] ),
 ("/insurance/business", "insurance/business.html", C(("/insurance/business","Business")),
  f"Best Business Insurance of {MONTH}", f"Best Business Insurance of {MONTH}",
  "General liability, professional liability, workers' comp — best for small business.",
  f"Best small business insurance of {MONTH}. Liability and workers comp compared.",
  "the best business insurance", "Protect the business.",
  "One lawsuit can end a small business. These insurers cover you right.",
  BRANDS[:3] + ins_progs(["business insurance"], 3),
  [("What coverage first?", "General liability, then professional liability if you give advice/services."),
   ("Cost?", "GL often $30-60/month for small businesses."),
   ("Workers' comp?", "Required in most states once you have employees.")] ),
 ("/insurance/motorcycle", "insurance/motorcycle.html", C(("/insurance/motorcycle","Motorcycle")),
  f"Best Motorcycle Insurance of {MONTH}", f"Best Motorcycle Insurance of {MONTH}",
  "Coverage for your bike at rider-friendly prices. Best motorcycle insurers.",
  f"Best motorcycle insurance of {MONTH}. Rider-friendly coverage compared.",
  "the best motorcycle insurance", "Ride protected.",
  "Motorcycle insurance is cheap — don't ride without it. Top insurers here.",
  BRANDS[1:2] + BRANDS[5:6] + BRANDS[:1] + ins_progs(["motorcycle"], 2),
  [("What's covered?", "Liability, collision, comprehensive, plus gear and accessories options."),
   ("Cost?", "Often $100-500/year depending on bike and record."),
   ("Discounts?", "Safety courses, bundling, and lay-up (winter storage) discounts.")] ),
 ("/insurance/flood", "insurance/flood.html", C(("/insurance/flood","Flood")),
  f"Best Flood Insurance of {MONTH}", f"Best Flood Insurance of {MONTH}",
  "Homeowners insurance doesn't cover floods. Best flood insurance options.",
  f"Best flood insurance of {MONTH}. NFIP and private options compared.",
  "the best flood insurance", "Water wins — be ready.",
  "One inch of water causes $25k+ damage. Flood insurance is essential in risk zones.",
  BRANDS[:3] + ins_progs(["flood"], 2),
  [("Does homeowners cover flood?", "No — never. You need separate flood insurance."),
   ("NFIP or private?", "NFIP caps at $250k; private can cover more with faster payouts."),
   ("Cost?", "$700/year average via NFIP; varies hugely by zone.")] ),
 ("/insurance/compare-quotes", "insurance/compare-quotes.html", C(("/insurance/compare-quotes","Compare Quotes")),
  f"Compare Insurance Quotes — {MONTH}", "Compare Insurance Quotes",
  "One form, multiple quotes. The fastest way to compare insurance prices.",
  f"Compare insurance quotes {MONTH}. Get multiple quotes with one form.",
  "insurance quote comparison", "One form, many prices.",
  "Comparing is the #1 way to save on insurance. These marketplaces do it fast.",
  BRANDS[8:10] + BRANDS[:3] + ins_progs(["quote", "compare"], 2),
  [("How many quotes?", "At least 3-5 for a real picture."),
   ("Will my credit be affected?", "Insurance quotes use soft inquiries — no score impact."),
   ("Same coverage?", "Always compare identical limits and deductibles.")] ),
 ("/insurance/cheap-car-insurance", "insurance/cheap-car-insurance.html", C(("/insurance/cheap-car-insurance","Cheap Car Insurance")),
  f"Cheapest Car Insurance of {MONTH}", f"Cheapest Car Insurance of {MONTH}",
  "The lowest car insurance rates by driver profile. Cheap doesn't mean bad.",
  f"Cheapest car insurance of {MONTH}. Low rates by driver profile compared.",
  "the cheapest car insurance", "Pay less, stay covered.",
  "These insurers consistently quote the lowest rates — without skimping on claims.",
  BRANDS[4:6] + BRANDS[:2] + ins_progs(["cheap", "ameriquote"], 2),
  [("Who's cheapest?", "Varies by profile — GEICO and Progressive often lead for clean records."),
   ("Minimum coverage?", "State minimums are cheap but risky; 100/300/100 is the smart baseline."),
   ("Lower my rate?", "Shop yearly, raise deductibles, bundle, and ask about every discount.")] ),
 ("/insurance/travel", "insurance/travel.html", C(("/insurance/travel","Travel")),
  f"Best Travel Insurance of {MONTH}", f"Best Travel Insurance of {MONTH}",
  "Trip cancellation, medical abroad, lost bags — best travel insurance compared.",
  f"Best travel insurance of {MONTH}. Trip protection and medical coverage compared.",
  "the best travel insurance", "Travel worry-free.",
  "One cancelled trip or ER visit abroad justifies travel insurance. Best picks here.",
  BRANDS[:2] + ins_progs(["travel insurance"], 3),
  [("What does it cover?", "Trip cancellation, interruption, medical emergencies, baggage."),
   ("Credit card coverage?", "Many premium cards include it — check before buying separate."),
   ("When to buy?", "Within 14 days of booking for pre-existing condition coverage.")] ),
 ("/insurance/pet", "insurance/pet.html", C(("/insurance/pet","Pet")),
  f"Best Pet Insurance of {MONTH}", f"Best Pet Insurance of {MONTH}",
  "Vet bills can hit $10k+. The best pet insurance for dogs and cats.",
  f"Best pet insurance of {MONTH}. Dog and cat coverage compared.",
  "the best pet insurance", "Never choose between wallet and whiskers.",
  "Pet insurance turns a $8,000 emergency into a manageable deductible.",
  BRANDS[:2] + ins_progs(["pet insurance"], 3),
  [("What does it cover?", "Accidents, illnesses, sometimes wellness — varies by plan."),
   ("Pre-existing?", "Generally excluded; enroll while pets are young and healthy."),
   ("Cost?", "$30-70/month for dogs, $15-40 for cats typically.")] ),
]

for p in PAGES:
    make(*p)
print("DONE insurance batch")
