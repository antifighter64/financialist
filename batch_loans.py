#!/usr/bin/env python3
"""Batch: Loans sub-pages (11 pages)."""
import sys
sys.path.insert(0, '.')
from generate import write_page
from page_helpers import PROGS, pick_from_program, curated_pick, rated, std_methodology

MONTH = "October 2026"

LOAN_BRANDS = [
    ("Fiona (Even Financial)", "4.5", "Compare personal loan offers",
     [("Loan", "$1k-$100k"), ("Payout", "$50-$150/lead"), ("Check", "Soft pull")],
     ["One form, multiple offers", "Soft pull to compare"],
     ["Not a direct lender"],
     "fiona", "READY-TO-APPLY", "direct"),
    ("LendingClub", "4.3", "Peer-to-peer personal loans",
     [("Loan", "$1k-$40k"), ("Payout", "$100/referral"), ("Members", "4M+")],
     ["NYSE-listed", "Debt consolidation focus"],
     ["Origination fees"],
     "lendingclub", "READY-TO-APPLY", "via Impact"),
    ("Upstart", "4.2", "AI-based approvals",
     [("Loan", "$1k-$50k"), ("Best for", "Thin credit"), ("Check", "Soft pull")],
     ["Approves thin files", "Fast funding"],
     ["Origination fees up to 12%"],
     "upstart", "READY-TO-APPLY", "affiliate program"),
    ("SoFi", "4.5", "No-fee personal loans",
     [("Loan", "$5k-$100k"), ("Fees", "$0"), ("Best for", "Good credit")],
     ["No fees at all", "Unemployment protection"],
     ["Higher minimums"],
     "sofi-loans", "READY-TO-APPLY", "affiliate program"),
    ("Upgrade", "4.3", "Personal loans + cards",
     [("Loan", "$1k-$50k"), ("Best for", "Fair credit"), ("Funding", "Fast")],
     ["Accepts fair credit", "Joint applications"],
     ["Origination fees"],
     "upgrade", "PENDING", "via FlexOffers"),
    ("National Funding", "4.2", "Business loans",
     [("Loan", "$5k-$500k"), ("Best for", "Small business"), ("Speed", "Fast")],
     ["Fast business funding", "Simple application"],
     ["Higher rates than banks"],
     "national-funding", "READY-TO-APPLY", "direct"),
    ("PersonalLoans.com", "4.1", "Loan marketplace",
     [("Loan", "$1k-$35k"), ("Payout", "$110/lead"), ("Best for", "Comparison")],
     ["Multiple lenders", "$110/lead payout"],
     ["Not a direct lender"],
     "personalloans-com", "READY-TO-APPLY", "direct"),
]

def bp(b):
    n, r, bf, sp, pr, co, sl, st, nt = b
    return curated_pick(n, r, bf, sp, pr, co, sl, st, nt)

BRANDS = [bp(b) for b in LOAN_BRANDS]

def loan_progs(keywords, n=4):
    picks, seen = [], set()
    for kw in keywords:
        for p in PROGS:
            if p['name'] in seen: continue
            blob = (p['name'] + ' ' + p['notes']).lower()
            if kw.lower() in blob and any(x in blob for x in ['loan', 'lending', 'credit']):
                if 'credit card' in blob: continue
                picks.append(pick_from_program(p, rating=rated(p['name'])))
                seen.add(p['name'])
                if len(picks) >= n: return picks
    return picks

def C(*a):
    return [("/", "Home"), ("/loans", "Loans")] + list(a)

def make(url_path, file_path, crumbs, title, h1, lead, meta, ct, cs, intro, picks, faqs):
    write_page(file_path, {
        "title": title, "url": url_path, "vertical": "loans",
        "crumbs": crumbs, "h1": h1, "lead": lead, "meta": meta,
        "compare_title": ct, "compare_sub": cs, "intro": intro,
        "picks": picks, "methodology": std_methodology([]), "faqs": faqs,
    })

PAGES = [
 ("/loans", "loans/index.html", C(),
  f"Best Loans of {MONTH}", f"Best Loans of {MONTH}",
  "Personal, auto, business, and more — the best loans compared by rate and terms.",
  f"Best loans of {MONTH}. Personal, auto, and business loans compared.",
  "the best loans", "Borrow smart.",
  "The right loan has the lowest total cost, not just the lowest payment. Best across types.",
  BRANDS[:5] + loan_progs(["personal loan"], 2),
  [("How to compare loans?", "APR first, then fees, then term. Lowest APR usually wins."),
   ("Soft vs hard pull?", "Prequalification = soft (no impact). Formal application = hard pull."),
   ("How fast?", "Online lenders fund in 1-3 days; banks take longer.")] ),
 ("/loans/auto", "loans/auto.html", C(("/loans/auto","Auto Loans")),
  f"Best Auto Loans of {MONTH}", f"Best Auto Loans of {MONTH}",
  "Get pre-approved before the dealership. The best auto loan rates compared.",
  f"Best auto loans of {MONTH}. Low rates for new and used cars compared.",
  "the best auto loans", "Don't let the dealer pick your loan.",
  "Dealer financing is convenient — and usually pricier. Get pre-approved first.",
  BRANDS[3:4] + BRANDS[:1] + loan_progs(["auto loan", "myautoloan"], 3),
  [("Pre-approval?", "Yes — walk in with a rate and make the dealer beat it."),
   ("New vs used rates?", "Used rates run 1-2% higher typically."),
   ("How long a term?", "60 months max ideally; 84-month loans cost far more.")] ),
 ("/loans/student", "loans/student.html", C(("/loans/student","Student Loans")),
  f"Best Student Loans of {MONTH}", f"Best Student Loans of {MONTH}",
  "Federal first, then private. The best private student loans compared.",
  f"Best student loans of {MONTH}. Federal and private options compared.",
  "the best student loans", "Borrow as little as possible.",
  "Always max federal loans first — then compare private lenders for the rest.",
  BRANDS[:1] + loan_progs(["student loan", "earnest"], 4),
  [("Federal or private?", "Federal: fixed rates, protections, forgiveness options. Private: sometimes lower rates for strong credit."),
   ("Cosigner?", "Most undergrads need one for private loans."),
   ("When to borrow?", "After grants, scholarships, and federal loans.")] ),
 ("/loans/debt-consolidation", "loans/debt-consolidation.html", C(("/loans/debt-consolidation","Debt Consolidation")),
  f"Best Debt Consolidation Loans of {MONTH}", f"Best Debt Consolidation Loans of {MONTH}",
  "One payment, lower rate. The best debt consolidation loans compared.",
  f"Best debt consolidation loans of {MONTH}. Lower rates, one payment compared.",
  "the best debt consolidation loans", "One payment, less interest.",
  "Consolidation works when the rate is lower and you stop adding debt. Best options here.",
  BRANDS[:3] + BRANDS[4:5] + loan_progs(["debt consolidation"], 2),
  [("Does it save money?", "Only if the new APR beats your current weighted average."),
   ("Balance transfer instead?", "0% cards work for smaller balances you can clear in 12-18 months."),
   ("Credit impact?", "Hard inquiry dip, then improvement as utilization drops.")] ),
 ("/loans/home-equity", "loans/home-equity.html", C(("/loans/home-equity","Home Equity")),
  f"Best Home Equity Loans of {MONTH} — See Mortgage Rates", "Best Home Equity Loans",
  "Compare home equity options — see our dedicated home equity guide.",
  f"Best home equity loans {MONTH}. See our full home equity comparison.",
  "home equity options", "See the full guide.",
  "We cover home equity in depth in our mortgage section.",
  BRANDS[:2],
  [("Where's the full guide?", "See financialist.com/mortgage/home-equity for the complete comparison.")] ),
 ("/loans/business", "loans/business.html", C(("/loans/business","Business Loans")),
  f"Best Business Loans of {MONTH}", f"Best Business Loans of {MONTH}",
  "Fund growth, cover gaps, buy equipment. The best small business loans.",
  f"Best business loans of {MONTH}. Small business financing compared.",
  "the best business loans", "Fuel growth.",
  "The right business loan funds growth without strangling cash flow.",
  BRANDS[5:6] + BRANDS[:2] + loan_progs(["business loan"], 3),
  [("Bank or online?", "Banks cheaper but slower; online lenders fund in days at higher rates."),
   ("What do lenders want?", "Revenue history, time in business, credit score."),
   ("SBA loans?", "Lowest rates, but slow. Worth it for large needs.")] ),
 ("/loans/bad-credit", "loans/bad-credit.html", C(("/loans/bad-credit","Bad Credit")),
  f"Best Bad-Credit Loans of {MONTH}", f"Best Bad-Credit Loans of {MONTH}",
  "Options for scores under 630 — without predatory rates. Honest picks.",
  f"Best bad-credit loans of {MONTH}. Fair options for low scores compared.",
  "the best bad-credit loans", "Rebuild, don't get ripped off.",
  "Bad credit limits options but doesn't eliminate them. These are the fair ones.",
  BRANDS[4:5] + loan_progs(["bad credit loan"], 4) + BRANDS[1:2],
  [("What APR is fair?", "Under 36% is the honest ceiling. Above that, walk away."),
   ("Guaranteed approval?", "No legitimate lender guarantees approval — that's a scam flag."),
   ("Improve first?", "Even 3 months of on-time payments can lift your options.")] ),
 ("/loans/payday-alternatives", "loans/payday-alternatives.html", C(("/loans/payday-alternatives","Payday Alternatives")),
  f"Payday Loan Alternatives — Better Options {MONTH}", "Payday Loan Alternatives",
  "Skip the 400% APR trap. Better ways to get fast cash.",
  f"Payday loan alternatives {MONTH}. Better fast-cash options than 400% APR.",
  "better fast-cash options", "Never pay 400% APR.",
  "Payday loans are a debt trap. These alternatives get you cash without the trap.",
  loan_progs(["payday alternative", "earnin", "cash advance"], 4) + BRANDS[:1],
  [("Why not payday?", "400%+ APRs trap borrowers in renewals. Almost always a net loss."),
   ("Fastest alternative?", "Earned-wage apps, credit union PALs, or 0%-APR card advances."),
   ("Credit union PALs?", "Payday Alternative Loans: $200-$2,000 at capped 28% APR.")] ),
 ("/loans/student-refinance", "loans/student-refinance.html", C(("/loans/student-refinance","Student Refinance")),
  f"Best Student Loan Refinance of {MONTH}", f"Best Student Loan Refinance of {MONTH}",
  "Lower your student loan rate. The best refinance lenders compared.",
  f"Best student loan refinance of {MONTH}. Lower rates compared.",
  "the best student refinance lenders", "Pay less interest.",
  "Refinancing federal loans forfeits protections — but can save thousands for private loans.",
  BRANDS[3:4] + loan_progs(["refinance", "earnest", "student"], 4),
  [("Refinance federal loans?", "Only if you're sure — you lose income-driven plans and forgiveness."),
   ("When?", "With stable income and 650+ credit, when rates beat your current."),
   ("How much saved?", "Even 1% on $50k saves ~$3,000 over 10 years.")] ),
 ("/loans/auto-refinance", "loans/auto-refinance.html", C(("/loans/auto-refinance","Auto Refinance")),
  f"Best Auto Refinance of {MONTH}", f"Best Auto Refinance of {MONTH}",
  "Lower your car payment. The best auto refinance lenders.",
  f"Best auto refinance of {MONTH}. Lower car payments compared.",
  "the best auto refinance lenders", "Pay less for the same car.",
  "If rates dropped or your credit improved, refinancing your auto loan pays.",
  BRANDS[:2] + loan_progs(["auto refinance"], 3),
  [("When to refinance?", "When rates are 1%+ lower or your credit jumped a tier."),
   ("Fees?", "Usually minimal — watch for prepayment penalties on the old loan."),
   ("Upside-down?", "Harder; some lenders allow 125% LTV.")] ),
 ("/loans/no-credit-check", "loans/no-credit-check.html", C(("/loans/no-credit-check","No Credit Check")),
  f"No-Credit-Check Loans — Honest Guide {MONTH}", "No-Credit-Check Loans — Honest Guide",
  "What 'no credit check' really means — and safer alternatives.",
  f"No-credit-check loans {MONTH}. Honest guide and safer alternatives.",
  "no-credit-check realities", "Read this first.",
  "'No credit check' usually means sky-high rates. Know the real cost — and alternatives.",
  loan_progs(["no credit check", "stilt"], 3) + BRANDS[4:5],
  [("Are they legit?", "Some are; many charge 100%+ APR. Read every fee."),
   ("Better option?", "Secured cards, credit-builder loans, or a co-signed loan."),
   ("Tribal lenders?", "They claim sovereign immunity from rate caps — extreme caution.")] ),
]

for p in PAGES:
    make(*p)
print("DONE loans batch")
