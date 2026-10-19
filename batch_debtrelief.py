#!/usr/bin/env python3
"""Batch: Debt relief sub-pages (8 pages)."""
import sys
sys.path.insert(0, '.')
from generate import write_page
from page_helpers import PROGS, pick_from_program, curated_pick, rated, std_methodology

MONTH = "October 2026"

DR_BRANDS = [
    ("National Debt Relief", "4.4", "Largest debt settlement firm",
     [("Clients", "600k+"), ("BBB", "A+"), ("Lead", "$27.50")],
     ["Largest in the US", "BBB A+", "Free consultation"],
     ["Fees 15-25% of enrolled debt", "Not in all states"],
     "national-debt-relief", "READY-TO-APPLY", "via ShareASale/Awin"),
    ("Freedom Debt Relief", "4.3", "Established settlement company",
     [("Founded", "2002"), ("Reviews", "4.7 stars"), ("Min debt", "$7,500")],
     ["Long track record", "700+ reviews at 4.7"],
     ["Settlement fees apply", "Credit impact during program"],
     "freedom-debt-relief", "READY-TO-APPLY", "via FlexOffers"),
    ("Guardian Debt Relief", "4.2", "Settlement + consultation",
     [("Lead", "$32"), ("Consult", "$45"), ("Best for", "Consultation")],
     ["$45 per qualified consultation", "Free evaluation"],
     ["Smaller than leaders"],
     "guardian-debt-relief", "READY-TO-APPLY", "via ShareASale/FlexOffers"),
    ("American Debt Enders", "4.1", "Counseling + settlement",
     [("Lead", "$20"), ("Call", "$40"), ("Cookie", "Lifetime")],
     ["Lifetime cookie", "Counseling focus"],
     ["Smaller operation"],
     "american-debt-enders", "READY-TO-APPLY", "via ShareASale"),
    ("Round Sky", "4.0", "Debt consolidation leads",
     [("Lead", "$20"), ("Min debt", "$10k cards"), ("Payout", "Weekly")],
     ["Weekly payouts", "Low $10k threshold"],
     ["Lead gen, not direct service"],
     "round-sky", "READY-TO-APPLY", "direct"),
]

def bp(b):
    n, r, bf, sp, pr, co, sl, st, nt = b
    return curated_pick(n, r, bf, sp, pr, co, sl, st, nt)

BRANDS = [bp(b) for b in DR_BRANDS]

def dr_progs(keywords, n=4):
    picks, seen = [], set()
    for kw in keywords:
        for p in PROGS:
            if p['name'] in seen: continue
            blob = (p['name'] + ' ' + p['notes']).lower()
            if kw.lower() in blob and any(x in blob for x in ['debt', 'settlement', 'consolidation']):
                if 'credit card' in p['name'].lower() and 'debt' not in blob: continue
                picks.append(pick_from_program(p, rating=rated(p['name'])))
                seen.add(p['name'])
                if len(picks) >= n: return picks
    return picks

def C(*a):
    return [("/", "Home"), ("/debt-relief", "Debt Relief")] + list(a)

def make(url_path, file_path, crumbs, title, h1, lead, meta, ct, cs, intro, picks, faqs):
    write_page(file_path, {
        "title": title, "url": url_path, "vertical": "debt-relief",
        "crumbs": crumbs, "h1": h1, "lead": lead, "meta": meta,
        "compare_title": ct, "compare_sub": cs, "intro": intro,
        "picks": picks, "methodology": std_methodology([]), "faqs": faqs,
    })

PAGES = [
 ("/debt-relief", "debt-relief/index.html", C(),
  f"Debt Relief Options Compared — {MONTH}", "Debt Relief Options Compared",
  "Settlement, consolidation, counseling, bankruptcy — every debt relief path, honestly compared.",
  f"Debt relief options {MONTH}. Settlement, consolidation, and counseling compared honestly.",
  "debt relief options", "Every path, honestly.",
  "Debt relief isn't one product. Here's every legitimate path — with real tradeoffs.",
  BRANDS + dr_progs(["debt relief"], 2),
  [("Which option is right?", "Can pay in full → consolidation loan. Can't → settlement or counseling. Overwhelmed → bankruptcy consult."),
   ("Does debt relief hurt credit?", "Settlement and bankruptcy do. Counseling and consolidation are gentler."),
   ("Scam signs?", "Upfront fees before services, guaranteed results, no physical address.")] ),
 ("/debt-relief/settlement", "debt-relief/settlement.html", C(("/debt-relief/settlement","Settlement")),
  f"Best Debt Settlement Companies of {MONTH}", f"Best Debt Settlement Companies of {MONTH}",
  "Negotiate debts down for less than you owe. The most reputable settlement firms.",
  f"Best debt settlement companies of {MONTH}. Reputable firms compared honestly.",
  "the best debt settlement companies", "Pay less than you owe.",
  "Settlement negotiates balances down — but hurts credit and costs fees. Most reputable firms here.",
  BRANDS[:4] + dr_progs(["settlement"], 2),
  [("How does settlement work?", "You stop paying; the firm negotiates lump-sum payoffs for 40-60% of balances."),
   ("Fees?", "15-25% of enrolled debt, charged as debts settle."),
   ("Taxes?", "Forgiven debt over $600 is taxable income.")] ),
 ("/debt-relief/consolidation", "debt-relief/consolidation.html", C(("/debt-relief/consolidation","Consolidation")),
  f"Best Debt Consolidation Programs of {MONTH}", f"Best Debt Consolidation Programs of {MONTH}",
  "Combine debts into one lower payment. Best consolidation programs and loans.",
  f"Best debt consolidation {MONTH}. Programs and loans compared.",
  "the best debt consolidation options", "One payment, lower rate.",
  "Consolidation simplifies and can cut interest — if the new rate is actually lower.",
  BRANDS[4:5] + dr_progs(["consolidation"], 3) + BRANDS[:1],
  [("Loan or program?", "Loans replace debt at lower rates. Programs (DMPs) negotiate via counseling agencies."),
   ("Credit needed?", "Good rates need 670+; DMPs accept lower."),
   ("Watch out?", "High-fee 'programs' that are just expensive loans.")] ),
 ("/debt-relief/counseling", "debt-relief/counseling.html", C(("/debt-relief/counseling","Counseling")),
  f"Best Credit Counseling Agencies of {MONTH}", f"Best Credit Counseling Agencies of {MONTH}",
  "Nonprofit counselors build debt management plans. The most trusted agencies.",
  f"Best credit counseling {MONTH}. Nonprofit agencies compared.",
  "the best credit counseling agencies", "Free help, real plans.",
  "Nonprofit counselors are the unsung heroes of debt relief — often free to start.",
  BRANDS[3:4] + dr_progs(["counseling"], 3) + BRANDS[:1],
  [("Cost?", "Initial counseling often free; DMPs ~$25-50/month."),
   ("DMP?", "Debt Management Plan: agency negotiates lower rates, you make one payment."),
   ("Nonprofit = legit?", "Check NFCC membership. Nonprofit status alone isn't proof.")] ),
 ("/debt-relief/credit-card-debt", "debt-relief/credit-card-debt.html", C(("/debt-relief/credit-card-debt","Credit Card Debt")),
  f"Credit Card Debt Relief — Best Options {MONTH}", "Credit Card Debt Relief",
  "Drowning in card debt? Every relief option ranked by cost and credit impact.",
  f"Credit card debt relief {MONTH}. Every option ranked honestly.",
  "credit card debt options", "Escape the minimum-payment trap.",
  "Minimum payments are a trap by design. Here are faster, cheaper exits.",
  BRANDS[:3] + dr_progs(["credit card"], 2),
  [("Fastest payoff?", "Avalanche (highest APR first) saves most; snowball (smallest first) motivates most."),
   ("Balance transfer?", "Great for balances clearable in 12-21 months."),
   ("When to get help?", "If minimums exceed 20% of income, talk to a nonprofit counselor.")] ),
 ("/debt-relief/tax-debt", "debt-relief/tax-debt.html", C(("/debt-relief/tax-debt","Tax Debt")),
  f"Tax Debt Relief — IRS Options {MONTH}", "Tax Debt Relief — IRS Options",
  "Owe the IRS? Installment agreements, offers in compromise, and when to get help.",
  f"Tax debt relief {MONTH}. IRS payment options explained honestly.",
  "tax debt options", "The IRS negotiates — really.",
  "The IRS has formal programs for people who can't pay in full. Know them before hiring anyone.",
  BRANDS[4:5] + dr_progs(["tax debt", "tax relief"], 2) + BRANDS[:1],
  [("Offer in compromise?", "Settle for less if you prove inability to pay — hard to get, real when approved."),
   ("Installment agreement?", "Pay over time; easy to set up online for under $50k."),
   ("Beware?", "'Pennies on the dollar' ads oversell. Most people don't qualify for OIC.")] ),
 ("/debt-relief/free-consultation", "debt-relief/free-consultation.html", C(("/debt-relief/free-consultation","Free Consultation")),
  f"Free Debt Consultation — Best Options {MONTH}", "Free Debt Consultation",
  "Talk to a real counselor free. Where to get honest debt advice at no cost.",
  f"Free debt consultation {MONTH}. Honest advice at no cost.",
  "free debt advice", "Start free, decide informed.",
  "Never pay for initial advice. These consultations are genuinely free.",
  BRANDS[2:4] + BRANDS[:1] + dr_progs(["consultation"], 1),
  [("Really free?", "Nonprofit counseling sessions are free. Some firms use 'free' as a sales funnel — watch for pressure."),
   ("What to ask?", "All options including ones they don't sell; total costs; credit impact."),
   ("Then what?", "Sleep on it. Legitimate help doesn't need same-day decisions.")] ),
 ("/debt-relief/bankruptcy-alternatives", "debt-relief/bankruptcy-alternatives.html", C(("/debt-relief/bankruptcy-alternatives","Bankruptcy Alternatives")),
  f"Alternatives to Bankruptcy — {MONTH}", "Alternatives to Bankruptcy",
  "Bankruptcy isn't the only way out. Every alternative, honestly compared.",
  f"Bankruptcy alternatives {MONTH}. Every option compared honestly.",
  "bankruptcy alternatives", "Before the nuclear option.",
  "Bankruptcy helps millions — but alternatives exist. Know them all first.",
  BRANDS[:3] + dr_progs(["bankruptcy"], 1),
  [("When is bankruptcy right?", "When debts exceed realistic repayment ability. It's a legal fresh start, not moral failure."),
   ("Chapter 7 vs 13?", "7 = liquidation, fast. 13 = repayment plan over 3-5 years."),
   ("Alternatives?", "Settlement, DMPs, consolidation — covered across this guide.")] ),
]

for p in PAGES:
    make(*p)
print("DONE debt relief batch")
