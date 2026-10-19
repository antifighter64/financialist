#!/usr/bin/env python3
"""Batch: Mortgage sub-pages (11 pages)."""
import sys
sys.path.insert(0, '.')
from generate import write_page, aff
from page_helpers import match, by_vertical, pick_from_program, curated_pick, rated, std_methodology

MONTH = "October 2026"

def base_crumbs(sub, sub_label):
    return [("/", "Home"), ("/mortgage", "Mortgages"), (sub, sub_label)]

def mortgage_picks(keywords, n=6, exclude=None):
    progs = match(keywords, exclude=exclude, limit=n)
    picks = []
    for p in progs:
        picks.append(pick_from_program(p, rating=rated(p['name'])))
    return picks, [p['name'] for p in progs]

USED = set()

def pg(url_path, file_path, title, h1, lead, meta, compare_title, compare_sub, intro,
       keywords, faqs, method_extra=None, n_picks=6, curated=None):
    global USED
    picks, names = mortgage_picks(keywords, n=n_picks, exclude=USED)
    USED.update(names)
    if curated:
        picks = curated + picks
    data = {
        "title": title, "url": url_path, "vertical": "mortgage",
        "crumbs": base_crumbs(url_path, h1.split(" of ")[0].replace("Best ", "")[:30]),
        "h1": h1, "lead": lead, "meta": meta,
        "compare_title": compare_title, "compare_sub": compare_sub, "intro": intro,
        "picks": picks,
        "methodology": std_methodology(method_extra or []),
        "faqs": faqs,
    }
    write_page(file_path, data)

# 1.2 purchase
pg("/mortgage/purchase", "mortgage/purchase.html",
   f"Best Mortgage Lenders for Home Purchase of {MONTH}",
   f"Best Mortgage Lenders for Home Purchase of {MONTH}",
   "Buying a home? These lenders offer competitive purchase rates, low fees, and fast closings for first-time and repeat buyers.",
   f"Compare the best mortgage lenders for home purchase of {MONTH}. Independent ratings on rates, fees, and closing speed.",
   "the best purchase mortgage lenders",
   "Top-rated lenders for buying a home this month.",
   "Whether it's your first home or your fifth, the right lender saves you thousands. These are our top picks for purchase mortgages.",
   ["credible", "lendingtree", "rocket mortgage", "loanDepot", "better.com"],
   [("What's the difference between pre-approval and pre-qualification?",
     "Pre-qualification is a rough estimate based on self-reported info. Pre-approval involves a credit check and document review — sellers take it much more seriously."),
    ("How much down payment do I need?",
     "Conventional loans can go as low as 3% down; FHA allows 3.5%. Putting 20% down avoids private mortgage insurance (PMI)."),
    ("How long does closing take?",
     "Typically 30-45 days from accepted offer. Digital lenders can close faster; complex loans take longer.")],
   n_picks=6)

# 1.3 refinance
pg("/mortgage/refinance", "mortgage/refinance.html",
   f"Best Mortgage Refinance Lenders of {MONTH}",
   f"Best Mortgage Refinance Lenders of {MONTH}",
   "Refinancing can lower your rate, shorten your term, or pull cash out. These lenders offer the best refinance rates and lowest closing costs.",
   f"Compare the best mortgage refinance lenders of {MONTH}. Independent ratings on rates, fees, and closing timelines.",
   "the best refinance lenders",
   "Lower your rate or tap equity — ranked by real refinance value.",
   "A good refinance pays for itself. These lenders make it easy to compare offers and lock a better deal.",
   ["refinance", "refi.com", "quicken", "credible", "lendingtree"],
   [("When does refinancing make sense?",
     "Generally when you can drop your rate by at least 0.75-1%, plan to stay long enough to break even on closing costs, or need to tap equity."),
    ("What does refinancing cost?",
     "Closing costs typically run 2-5% of the loan amount. Some lenders offer no-closing-cost refis with a slightly higher rate."),
    ("How long is a rate lock good for?",
     "Usually 30-60 days. Make sure your lock covers your expected closing date.")],
   n_picks=6)

# 1.4 fha
pg("/mortgage/fha", "mortgage/fha.html",
   f"Best FHA Loan Lenders of {MONTH}",
   f"Best FHA Loan Lenders of {MONTH}",
   "FHA loans allow down payments as low as 3.5% with credit scores from 580. These lenders specialize in FHA mortgages.",
   f"Compare the best FHA loan lenders of {MONTH}. Low down payments, flexible credit requirements, independent ratings.",
   "the best FHA lenders",
   "Low down payment, flexible credit — the best FHA specialists.",
   "FHA loans open homeownership to buyers with smaller down payments. These lenders know the program inside and out.",
   ["fha", "freedom mortgage", "rocket mortgage", "loanDepot", "credible"],
   [("What credit score do I need for an FHA loan?",
     "580+ qualifies for 3.5% down. Scores 500-579 can qualify with 10% down, though fewer lenders offer this."),
    ("What is MIP on an FHA loan?",
     "Mortgage Insurance Premium — required on all FHA loans. There's an upfront premium (1.75%) plus annual MIP, which lasts for the life of most FHA loans."),
    ("Can I refinance out of an FHA loan?",
     "Yes — many borrowers refinance into conventional loans once they have 20% equity to drop MIP.")],
   n_picks=6)

# 1.5 va
pg("/mortgage/va", "mortgage/va.html",
   f"Best VA Loan Lenders of {MONTH}",
   f"Best VA Loan Lenders of {MONTH}",
   "VA loans offer 0% down, no PMI, and competitive rates for veterans and active-duty service members. These are the best VA lenders.",
   f"Compare the best VA loan lenders of {MONTH}. Zero down payment, no PMI, independent ratings for veterans.",
   "the best VA loan lenders",
   "Zero down, no PMI — the best lenders for those who served.",
   "VA loans are one of the best benefits of military service. These lenders specialize in getting veterans the best deal.",
   ["veterans united", "mortgage research center", "va ", "ifreedome", "credible"],
   [("Who qualifies for a VA loan?",
     "Veterans, active-duty service members, National Guard/Reserve members, and some surviving spouses. You'll need a Certificate of Eligibility (COE)."),
    ("Is there a down payment on VA loans?",
     "No — VA loans allow 0% down with no PMI, one of the biggest advantages of the program."),
    ("What is the VA funding fee?",
     "A one-time fee (typically 2.15% for first use) that can be rolled into the loan. Disabled veterans are exempt.")],
   n_picks=6)

# 1.6 jumbo
pg("/mortgage/jumbo", "mortgage/jumbo.html",
   f"Best Jumbo Loan Lenders of {MONTH}",
   f"Best Jumbo Loan Lenders of {MONTH}",
   "Buying above the conforming loan limit? Jumbo loans cover high-value homes. These lenders offer competitive jumbo rates.",
   f"Compare the best jumbo loan lenders of {MONTH}. High-value home financing with independent ratings.",
   "the best jumbo lenders",
   "Above the conforming limit — competitive jumbo specialists.",
   "Jumbo loans need bigger down payments and stronger credit. These lenders offer the best terms for luxury and high-cost markets.",
   ["jumbo", "sofi", "credible", "lendingtree", "rocket mortgage"],
   [("What is the conforming loan limit?",
     "For 2026 it's $832,750 in most areas (higher in high-cost markets). Loans above this are jumbo."),
    ("What down payment do jumbo loans need?",
     "Typically 10-20%. Some lenders go lower with strong credit and reserves."),
    ("Are jumbo rates higher?",
     "Usually slightly higher than conforming rates, though the gap narrows in competitive markets.")],
   n_picks=6)

# 1.7 first-time-buyer
pg("/mortgage/first-time-buyer", "mortgage/first-time-buyer.html",
   f"Best First-Time Home Buyer Programs of {MONTH}",
   f"Best First-Time Home Buyer Programs of {MONTH}",
   "First-time buyers get special programs: low down payments, down payment assistance, and favorable rates. Start here.",
   f"Compare the best first-time home buyer programs of {MONTH}. Down payment assistance, low-down options, independent ratings.",
   "the best first-time buyer programs",
   "Low down payments and assistance — built for first-timers.",
   "You don't need 20% down to buy your first home. These programs and lenders make it achievable.",
   ["first-time", "fha", "credible", "emortgage", "lendingtree"],
   [("What counts as a first-time buyer?",
     "Generally someone who hasn't owned a home in the past 3 years. Many programs use this definition."),
    ("Are there down payment assistance programs?",
     "Yes — thousands of state and local programs offer grants or low-interest second loans. Check your state's housing finance agency."),
    ("Should I use an FHA or conventional loan as a first-time buyer?",
     "FHA is easier to qualify for with lower credit; conventional avoids lifetime MIP and may be cheaper if you have 620+ credit and 5% down.")],
   n_picks=6)

# 1.8 rates
pg("/mortgage/rates", "mortgage/rates.html",
   f"Today's Mortgage Rates Compared — {MONTH}",
   f"Today's Mortgage Rates Compared — {MONTH}",
   "Compare today's mortgage rates from top lenders. See 30-year, 15-year, FHA, and VA rates side by side.",
   f"Compare today's mortgage rates from top lenders. 30-year, 15-year, FHA, VA rates updated for {MONTH}.",
   "today's mortgage rates",
   "Live rate shopping — compare before you lock.",
   "Rates move daily. Comparing multiple lenders is the single best way to get a lower rate.",
   ["credible", "lendingtree", "rocket mortgage", "loanDepot", "better.com"],
   [("What affects my mortgage rate?",
     "Credit score, down payment, loan type, loan term, and market conditions. Even your ZIP code matters."),
    ("Should I lock my rate?",
     "If you're happy with the quote and closing within the lock period, yes. Float-down options let you benefit if rates drop."),
    ("What's the difference between rate and APR?",
     "The rate is your interest cost; APR includes fees, giving a truer cost comparison between lenders.")],
   n_picks=6)

# 1.9 calculator
pg("/mortgage/calculator", "mortgage/calculator.html",
   f"Mortgage Calculator — Estimate Your Monthly Payment ({MONTH})",
   f"Mortgage Calculator — Estimate Your Monthly Payment",
   "Estimate your monthly mortgage payment including principal, interest, taxes, and insurance. Then compare lenders.",
   f"Free mortgage calculator for {MONTH}. Estimate monthly payments with taxes and insurance, then compare top lenders.",
   "mortgage payment estimates",
   "Know your number before you shop.",
   "Run the numbers first, then compare lenders with confidence. These marketplaces show you real offers.",
   ["credible", "lendingtree", "loanDepot"],
   [("What goes into a mortgage payment?",
     "Principal + interest, plus property taxes, homeowners insurance, and PMI if your down payment is under 20% (PITI)."),
    ("How much house can I afford?",
     "A common rule: keep housing costs under 28% of gross monthly income. Lenders look at your full debt-to-income ratio too."),
    ("Does the calculator include PMI?",
     "Our guidance covers it — ask each lender for a full PITI quote so you're comparing apples to apples.")],
   n_picks=4)

# 1.10 home-equity
pg("/mortgage/home-equity", "mortgage/home-equity.html",
   f"Best Home Equity Loans & HELOCs of {MONTH}",
   f"Best Home Equity Loans & HELOCs of {MONTH}",
   "Tap your home's equity with a home equity loan or HELOC. Compare the best rates and terms.",
   f"Compare the best home equity loans and HELOCs of {MONTH}. Independent ratings on rates, fees, and draw terms.",
   "the best home equity options",
   "Your equity, working for you — ranked by real cost.",
   "Home equity can fund renovations, consolidate debt, or cover big expenses. These are the best ways to access it.",
   ["point", "splitero", "easyknock", "credible", "lendingtree"],
   [("What's the difference between a home equity loan and HELOC?",
     "A home equity loan is a lump sum with fixed payments. A HELOC is a revolving credit line you draw from as needed."),
    ("How much equity can I borrow?",
     "Most lenders allow up to 80-85% combined loan-to-value, meaning your total borrowing against the home."),
    ("Are home equity interest rates fixed?",
     "Home equity loans are usually fixed; HELOCs are usually variable (though some offer fixed-rate lock options).")],
   n_picks=6)

# 1.11 investor-loans
pg("/mortgage/investor-loans", "mortgage/investor-loans.html",
   f"Best Investment Property Loans (DSCR) of {MONTH}",
   f"Best Investment Property Loans (DSCR) of {MONTH}",
   "DSCR loans qualify on rental income, not your personal income. The best lenders for real estate investors.",
   f"Compare the best DSCR and investor loans of {MONTH}. Rental property financing with independent ratings.",
   "the best investor loans",
   "Qualified on rent, not salary — built for investors.",
   "DSCR loans let investors scale without W-2 income verification. These lenders specialize in rental property financing.",
   ["visio", "new silver", "biggerpockets", "kiavi", "easy street"],
   [("What is a DSCR loan?",
     "Debt Service Coverage Ratio loan — qualifies based on the property's rental income covering its mortgage payment, not your personal income."),
    ("What DSCR ratio do lenders want?",
     "Typically 1.0-1.25x, meaning rent covers 100-125% of the mortgage payment."),
    ("Can I use DSCR loans for short-term rentals?",
     "Some lenders allow it with Airbnb income history; others require long-term leases. Ask before applying.")],
   n_picks=6)

# 1.12 reverse-mortgage
pg("/mortgage/reverse-mortgage", "mortgage/reverse-mortgage.html",
   f"Best Reverse Mortgage Lenders of {MONTH}",
   f"Best Reverse Mortgage Lenders of {MONTH}",
   "Reverse mortgages let homeowners 62+ convert equity to cash. Compare the most reputable reverse mortgage lenders.",
   f"Compare the best reverse mortgage lenders of {MONTH}. HECM options for homeowners 62+, independent ratings.",
   "the best reverse mortgage lenders",
   "Equity to income after 62 — the reputable options.",
   "A reverse mortgage can supplement retirement income, but it's a big decision. These are the most reputable lenders.",
   ["ringpartner", "credible", "lendingtree"],
   [("How does a reverse mortgage work?",
     "Homeowners 62+ borrow against equity; no monthly payments required. The loan is repaid when you sell, move out, or pass away."),
    ("Will I still own my home?",
     "Yes — you retain title. The lender places a lien, like a regular mortgage."),
    ("What are the risks?",
     "Fees are higher than regular mortgages, and it reduces your estate. HUD-approved counseling is required — use it.")],
   n_picks=4)

print("DONE mortgage batch")
