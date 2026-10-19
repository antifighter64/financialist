#!/usr/bin/env python3
"""Batch: Mortgage sub-pages (11 pages) — v2 with guaranteed minimum picks."""
import sys
sys.path.insert(0, '.')
from generate import write_page, aff
from page_helpers import PROGS, pick_from_program, curated_pick, rated, std_methodology
import re

MONTH = "October 2026"

# Curated major mortgage brands with honest ratings
MORTGAGE_BRANDS = [
    ("Credible", "4.8", "Comparing multiple lenders at once",
     [("Loan types", "Conventional, FHA, VA, jumbo"), ("Min. credit", "Varies by lender"), ("Cost to compare", "Free")],
     ["One form, quotes from multiple vetted lenders", "No credit impact to compare", "Covers purchase and refinance"],
     ["Not a direct lender — matched to partners"],
     "credible", "PENDING", "via Credible — application submitted Oct 18"),
    ("LendingTree", "4.7", "Side-by-side lender competition",
     [("Loan types", "Conventional, FHA, VA, USDA, jumbo"), ("Offers", "Up to 5 competing"), ("Cost", "Free")],
     ["Multiple lenders compete for your business", "Wide loan type coverage", "Free to use"],
     ["Expect calls from matched lenders"],
     "lendingtree", "PENDING", "via CJ — application in flight"),
    ("Rocket Mortgage", "4.6", "Fully digital application",
     [("Loan types", "Conventional, FHA, VA, jumbo"), ("Min. credit", "620"), ("Closing", "As fast as ~3 weeks")],
     ["Best-in-class digital experience", "Fast closings", "Strong customer service reputation"],
     ["Rates not always the lowest"],
     "rocket-mortgage", "PENDING", "via CJ — $15-20 per lead"),
    ("loanDepot", "4.4", "Large lender with local branches",
     [("Loan types", "Conventional, FHA, VA, jumbo"), ("Min. credit", "620"), ("Branches", "Nationwide")],
     ["Digital + in-person options", "Wide product range"],
     ["Mixed customer reviews"],
     "loandepot", "READY-TO-APPLY", "unverified — confirm in dashboard"),
    ("Better.com", "4.3", "Online-first, no commissions",
     [("Loan types", "Conventional, FHA, VA"), ("Min. credit", "620"), ("Fees", "No lender commission")],
     ["Transparent online process", "No loan officer commissions"],
     ["Limited loan products vs. big banks"],
     "better-com", "READY-TO-APPLY", "unverified — confirm in dashboard"),
    ("Freedom Mortgage", "4.1", "FHA/VA specialist",
     [("Loan types", "FHA, VA, conventional"), ("Min. credit", "580"), ("Focus", "Government loans")],
     ["Strong FHA/VA expertise", "Serves lower-credit borrowers"],
     ["Higher fees on some products"],
     "freedom-mortgage", "READY-TO-APPLY", "unverified"),
    ("SoFi", "4.5", "Member benefits, no lender fees",
     [("Loan types", "Conventional, jumbo"), ("Min. credit", "620"), ("Lender fees", "$0")],
     ["No lender fees", "Member perks (career coaching, events)"],
     ["Limited government loan options"],
     "sofi-mortgage", "READY-TO-APPLY", "unverified"),
    ("AmeriSave Mortgage", "4.2", "Competitive online rates",
     [("Loan types", "Conventional, FHA, VA, jumbo"), ("Min. credit", "600"), ("Process", "Mostly online")],
     ["Competitive rates", "Multiple loan options"],
     ["Mixed reviews on communication"],
     "amerisave", "READY-TO-APPLY", "via CPA network"),
]

def brand_pick(b):
    name, rating, bf, specs, pros, cons, slug, status, note = b
    return curated_pick(name, rating, bf, specs, pros, cons, slug, status, note)

def prog_picks(keywords, n=4, exclude_names=None):
    """Get program picks matching keywords."""
    exclude_names = exclude_names or set()
    picks = []
    seen = set()
    for kw in keywords:
        for p in PROGS:
            if p['name'] in seen or p['name'] in exclude_names:
                continue
            blob = (p['name'] + ' ' + p['notes']).lower()
            if kw.lower() in blob and 'mortgage' in blob or kw.lower() in p['name'].lower():
                if any(x in blob for x in ['mortgage', 'home loan', 'refi', 'heloc', 'dscr', 'va ', 'fha']):
                    picks.append(pick_from_program(p, rating=rated(p['name'])))
                    seen.add(p['name'])
                    if len(picks) >= n:
                        return picks
    return picks

def all_mortgage_progs(n=8):
    picks = []
    seen = set()
    for p in PROGS:
        blob = (p['name'] + ' ' + p['notes']).lower()
        if p['name'] in seen:
            continue
        if any(x in blob for x in ['mortgage', 'home loan', 'refinance', 'heloc', 'dscr']):
            if 'credit card' in blob or 'debt settlement' in blob:
                continue
            picks.append(pick_from_program(p, rating=rated(p['name'])))
            seen.add(p['name'])
            if len(picks) >= n:
                break
    return picks

def make_page(url_path, file_path, vertical, crumbs, title, h1, lead, meta,
              compare_title, compare_sub, intro, picks, faqs, method_extra=None):
    data = {
        "title": title, "url": url_path, "vertical": vertical,
        "crumbs": crumbs, "h1": h1, "lead": lead, "meta": meta,
        "compare_title": compare_title, "compare_sub": compare_sub, "intro": intro,
        "picks": picks,
        "methodology": std_methodology(method_extra or []),
        "faqs": faqs,
    }
    write_page(file_path, data)

def C(*a):
    return [("/", "Home"), ("/mortgage", "Mortgages")] + list(a)

BRANDS = [brand_pick(b) for b in MORTGAGE_BRANDS]

# --- 1.2 purchase ---
picks = BRANDS[:5] + all_mortgage_progs(3)
make_page("/mortgage/purchase", "mortgage/purchase.html", "mortgage",
    C(("/mortgage/purchase", "Purchase")),
    f"Best Mortgage Lenders for Home Purchase of {MONTH}",
    f"Best Mortgage Lenders for Home Purchase of {MONTH}",
    "Buying a home? These lenders offer competitive purchase rates, low fees, and fast closings.",
    f"Compare the best mortgage lenders for home purchase of {MONTH}. Independent ratings on rates and fees.",
    "the best purchase mortgage lenders", "Top-rated lenders for buying a home.",
    "The right lender saves you thousands. These are our top picks for purchase mortgages.",
    picks,
    [("What's the difference between pre-approval and pre-qualification?",
      "Pre-qualification is a rough estimate. Pre-approval involves a credit check and document review — sellers take it seriously."),
     ("How much down payment do I need?",
      "Conventional loans can go as low as 3% down; FHA allows 3.5%. Putting 20% down avoids PMI."),
     ("How long does closing take?", "Typically 30-45 days. Digital lenders can close faster.")])


# --- 1.3 refinance ---
picks = BRANDS[:4] + prog_picks(["refi", "quicken", "lower"], n=4)
make_page("/mortgage/refinance", "mortgage/refinance.html", "mortgage",
    C(("/mortgage/refinance", "Refinance")),
    f"Best Mortgage Refinance Lenders of {MONTH}",
    f"Best Mortgage Refinance Lenders of {MONTH}",
    "Refinancing can lower your rate, shorten your term, or pull cash out. Best refinance rates and lowest closing costs.",
    f"Compare the best mortgage refinance lenders of {MONTH}. Independent ratings on rates and fees.",
    "the best refinance lenders", "Lower your rate or tap equity.",
    "A good refinance pays for itself. These lenders make it easy to compare offers.",
    picks,
    [("When does refinancing make sense?",
      "When you can drop your rate by 0.75-1%, plan to stay long enough to break even, or need to tap equity."),
     ("What does refinancing cost?", "Closing costs run 2-5% of the loan. Some lenders offer no-closing-cost refis at a slightly higher rate."),
     ("How long is a rate lock good for?", "Usually 30-60 days. Make sure it covers your closing date.")])

# --- 1.4 fha ---
picks = [BRANDS[5]] + BRANDS[:3] + prog_picks(["fha", "freedom"], n=3)
make_page("/mortgage/fha", "mortgage/fha.html", "mortgage",
    C(("/mortgage/fha", "FHA Loans")),
    f"Best FHA Loan Lenders of {MONTH}",
    f"Best FHA Loan Lenders of {MONTH}",
    "FHA loans allow 3.5% down with credit scores from 580. Lenders that specialize in FHA mortgages.",
    f"Compare the best FHA loan lenders of {MONTH}. Low down payments, flexible credit, independent ratings.",
    "the best FHA lenders", "Low down payment, flexible credit.",
    "FHA loans open homeownership to buyers with smaller down payments.",
    picks,
    [("What credit score for an FHA loan?", "580+ qualifies for 3.5% down. Scores 500-579 can qualify with 10% down."),
     ("What is MIP?", "Mortgage Insurance Premium — required on FHA loans. Upfront 1.75% plus annual MIP for most loans."),
     ("Can I refinance out of FHA?", "Yes — many refinance to conventional at 20% equity to drop MIP.")])

# --- 1.5 va ---
picks = BRANDS[:3] + prog_picks(["veteran", "va ", "ifreedome", "mortgage research"], n=4)
make_page("/mortgage/va", "mortgage/va.html", "mortgage",
    C(("/mortgage/va", "VA Loans")),
    f"Best VA Loan Lenders of {MONTH}",
    f"Best VA Loan Lenders of {MONTH}",
    "VA loans offer 0% down, no PMI, and competitive rates for veterans and active-duty members.",
    f"Compare the best VA loan lenders of {MONTH}. Zero down, no PMI, independent ratings.",
    "the best VA loan lenders", "Zero down, no PMI.",
    "VA loans are one of the best military benefits. These lenders specialize in them.",
    picks,
    [("Who qualifies?", "Veterans, active-duty, Guard/Reserve, some surviving spouses. You need a COE."),
     ("Down payment?", "None required — 0% down with no PMI."),
     ("VA funding fee?", "One-time fee (~2.15% first use), can be rolled in. Disabled veterans exempt.")])

# --- 1.6 jumbo ---
picks = [BRANDS[6]] + BRANDS[:3] + prog_picks(["jumbo", "sofi"], n=3)
make_page("/mortgage/jumbo", "mortgage/jumbo.html", "mortgage",
    C(("/mortgage/jumbo", "Jumbo Loans")),
    f"Best Jumbo Loan Lenders of {MONTH}",
    f"Best Jumbo Loan Lenders of {MONTH}",
    "Above the conforming limit? Jumbo loans cover high-value homes with competitive rates.",
    f"Compare the best jumbo loan lenders of {MONTH}. High-value financing, independent ratings.",
    "the best jumbo lenders", "Above the conforming limit.",
    "Jumbo loans need bigger down payments and stronger credit. Best terms for high-cost markets.",
    picks,
    [("Conforming limit?", "For 2026 it's $832,750 in most areas; higher in high-cost markets."),
     ("Down payment?", "Typically 10-20%."),
     ("Higher rates?", "Usually slightly higher than conforming, gap narrows in competitive markets.")])

# --- 1.7 first-time-buyer ---
picks = BRANDS[:5] + prog_picks(["first-time", "emortgage"], n=3)
make_page("/mortgage/first-time-buyer", "mortgage/first-time-buyer.html", "mortgage",
    C(("/mortgage/first-time-buyer", "First-Time Buyers")),
    f"Best First-Time Home Buyer Programs of {MONTH}",
    f"Best First-Time Home Buyer Programs of {MONTH}",
    "Low down payments, assistance programs, favorable rates — start here as a first-time buyer.",
    f"Best first-time home buyer programs of {MONTH}. Down payment assistance, independent ratings.",
    "the best first-time buyer programs", "Built for first-timers.",
    "You don't need 20% down. These programs make homeownership achievable.",
    picks,
    [("What counts as first-time?", "Generally no home ownership in past 3 years."),
     ("Down payment assistance?", "Thousands of state/local programs offer grants or low-interest seconds."),
     ("FHA or conventional?", "FHA easier with lower credit; conventional cheaper at 620+ credit and 5% down.")])

# --- 1.8 rates ---
picks = BRANDS[:6]
make_page("/mortgage/rates", "mortgage/rates.html", "mortgage",
    C(("/mortgage/rates", "Rates")),
    f"Today's Mortgage Rates Compared — {MONTH}",
    f"Today's Mortgage Rates Compared — {MONTH}",
    "Compare today's mortgage rates: 30-year, 15-year, FHA, VA — side by side.",
    f"Today's mortgage rates compared. 30-year, 15-year, FHA, VA rates for {MONTH}.",
    "today's mortgage rates", "Live rate shopping.",
    "Rates move daily. Comparing lenders is the best way to a lower rate.",
    picks,
    [("What affects my rate?", "Credit score, down payment, loan type, term, market conditions, ZIP code."),
     ("Lock or float?", "Lock if happy with the quote and closing in time. Float-downs capture drops."),
     ("Rate vs APR?", "Rate is interest cost; APR includes fees — better for comparing lenders.")])

# --- 1.9 calculator ---
picks = BRANDS[:4]
make_page("/mortgage/calculator", "mortgage/calculator.html", "mortgage",
    C(("/mortgage/calculator", "Calculator")),
    f"Mortgage Calculator — Monthly Payment Estimator ({MONTH})",
    "Mortgage Calculator — Monthly Payment Estimator",
    "Estimate monthly payments with taxes and insurance, then compare lenders.",
    f"Free mortgage calculator for {MONTH}. Estimate payments, then compare top lenders.",
    "mortgage payment estimates", "Know your number.",
    "Run the numbers, then compare lenders with confidence.",
    picks,
    [("What's in a payment?", "Principal + interest, taxes, insurance, PMI if under 20% down (PITI)."),
     ("How much can I afford?", "Keep housing under 28% of gross income as a rule of thumb."),
     ("PMI included?", "Ask each lender for a full PITI quote to compare apples to apples.")])

# --- 1.10 home-equity ---
picks = BRANDS[:3] + prog_picks(["point", "splitero", "easyknock", "heloc", "equity"], n=4)
make_page("/mortgage/home-equity", "mortgage/home-equity.html", "mortgage",
    C(("/mortgage/home-equity", "Home Equity")),
    f"Best Home Equity Loans & HELOCs of {MONTH}",
    f"Best Home Equity Loans & HELOCs of {MONTH}",
    "Tap your equity with a home equity loan or HELOC. Best rates and terms compared.",
    f"Best home equity loans and HELOCs of {MONTH}. Independent ratings on rates and terms.",
    "the best home equity options", "Your equity, working for you.",
    "Fund renovations, consolidate debt, or cover big expenses with your equity.",
    picks,
    [("Loan vs HELOC?", "Loan = lump sum, fixed payments. HELOC = revolving line you draw from."),
     ("How much can I borrow?", "Most lenders allow up to 80-85% combined loan-to-value."),
     ("Fixed or variable?", "Loans usually fixed; HELOCs usually variable.")])

# --- 1.11 investor-loans ---
picks = prog_picks(["visio", "dscr", "new silver", "kiavi", "biggerpockets", "rental"], n=6) + BRANDS[:2]
make_page("/mortgage/investor-loans", "mortgage/investor-loans.html", "mortgage",
    C(("/mortgage/investor-loans", "Investor Loans")),
    f"Best Investment Property Loans (DSCR) of {MONTH}",
    f"Best Investment Property Loans (DSCR) of {MONTH}",
    "DSCR loans qualify on rental income, not personal income. Best lenders for investors.",
    f"Best DSCR and investor loans of {MONTH}. Rental property financing, independent ratings.",
    "the best investor loans", "Qualified on rent, not salary.",
    "Scale your portfolio without W-2 verification.",
    picks,
    [("What is DSCR?", "Loan qualifying on the property's rental income covering its payment."),
     ("What ratio?", "Typically 1.0-1.25x."),
     ("Short-term rentals?", "Some allow with Airbnb history; others require long-term leases.")])

# --- 1.12 reverse-mortgage ---
picks = prog_picks(["reverse", "ringpartner"], n=3) + BRANDS[:3]
make_page("/mortgage/reverse-mortgage", "mortgage/reverse-mortgage.html", "mortgage",
    C(("/mortgage/reverse-mortgage", "Reverse Mortgage")),
    f"Best Reverse Mortgage Lenders of {MONTH}",
    f"Best Reverse Mortgage Lenders of {MONTH}",
    "Homeowners 62+ can convert equity to cash. The most reputable reverse mortgage lenders.",
    f"Best reverse mortgage lenders of {MONTH}. HECM options for 62+, independent ratings.",
    "the best reverse mortgage lenders", "Equity to income after 62.",
    "Supplement retirement income — but understand the tradeoffs first.",
    picks,
    [("How does it work?", "Borrow against equity; no monthly payments. Repaid on sale, move-out, or death."),
     ("Own my home?", "Yes — you retain title."),
     ("Risks?", "Higher fees; reduces estate. HUD counseling required.")])

print("DONE mortgage v2")
