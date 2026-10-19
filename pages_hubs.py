#!/usr/bin/env python3
"""Priority 1: mortgage hub + Priority 2: credit cards hub."""
from generate import write_page, aff

# ============================ 1. MORTGAGE HUB ============================
mortgage = {
    "title": "Best Mortgage Lenders of October 2026",
    "url": "/mortgage",
    "vertical": "mortgage",
    "crumbs": [("/", "Home"), ("/mortgage", "Mortgages")],
    "h1": "Best Mortgage Lenders of October 2026",
    "lead": "We compared dozens of mortgage lenders on rates, fees, loan options, and how fast they close — so you can shop with confidence whether you're buying your first home or refinancing.",
    "meta": "Compare the best mortgage lenders of October 2026. Independent ratings on rates, fees, and closing speed for purchase and refinance loans.",
    "compare_title": "the best mortgage lenders",
    "compare_sub": "Short on time? These are our top-rated lenders for most borrowers this month.",
    "intro": "Every lender below was evaluated on the same criteria: advertised rates, lender fees, range of loan products, digital experience, and customer reviews. Click through to compare live rates.",
    "picks": [
        {
            "name": "Credible", "rating": "4.8", "best_for": "Comparing multiple lenders at once",
            "specs": [("Loan types", "Conventional, FHA, VA, jumbo"), ("Min. credit score", "Varies by lender"), ("Rate lock", "Varies by lender")],
            "pros": ["One form, quotes from multiple vetted lenders", "No impact to credit score to compare", "Covers purchase and refinance"],
            "cons": ["Not a direct lender — you're matched to partners", "Partner availability varies by state"],
            "affiliate": aff("credible-mortgage", "Credible mortgage marketplace", "Compare rates",
                             "PENDING", note="submitted 2026-10-18 via credible.com/partners; awaiting approval"),
        },
        {
            "name": "LendingTree", "rating": "4.7", "best_for": "Side-by-side lender competition",
            "specs": [("Loan types", "Conventional, FHA, VA, USDA, jumbo"), ("Min. credit score", "Varies by lender"), ("Offers", "Up to 5 competing offers")],
            "pros": ["Lenders compete for your business", "Huge lender network", "Free credit score included"],
            "cons": ["Expect calls and emails from matched lenders", "Not all lenders participate"],
            "affiliate": aff("lendingtree-mortgage", "LendingTree mortgage marketplace", "Get competing quotes",
                             "PENDING", note="join via CJ publisher account (8090336); awaiting advertiser approval"),
        },
        {
            "name": "Rocket Mortgage", "rating": "4.6", "best_for": "Fully digital application",
            "specs": [("Loan types", "Conventional, FHA, VA, jumbo"), ("Min. credit score", "620"), ("Closing time", "As fast as ~3 weeks")],
            "pros": ["Best-in-class online experience", "Fast preapproval", "Large servicing portfolio"],
            "cons": ["Rates aren't always the lowest", "Limited branch presence"],
            "affiliate": aff("rocket-mortgage", "Rocket Mortgage", "Check your rate",
                             "PENDING", note="applied via CJ; awaiting advertiser approval"),
        },
        {
            "name": "Veterans United (via Mortgage Research Center)", "rating": "4.6", "best_for": "VA loans",
            "specs": [("Loan types", "VA purchase & refinance"), ("Min. credit score", "620"), ("Specialty", "Military borrowers")],
            "pros": ["#1 VA purchase lender by volume", "Dedicated VA loan expertise", "Strong borrower education"],
            "cons": ["VA loans only — not for conventional borrowers", "Must meet VA eligibility"],
            "affiliate": aff("veterans-united", "Mortgage Research Center / Veterans United", "Check VA eligibility",
                             "PENDING", note="MaxBounty CPL offer; confirm payout in dashboard"),
        },
        {
            "name": "Visio Lending", "rating": "4.4", "best_for": "Real estate investors (DSCR loans)",
            "specs": [("Loan types", "DSCR rental loans"), ("Coverage", "38 states + DC"), ("Min. credit score", "660")],
            "pros": ["No personal income verification", "Built for rental investors", "Fast investor closings"],
            "cons": ["Investor loans only", "Higher rates than owner-occupied"],
            "affiliate": aff("visio-lending", "Visio Lending", "Get investor rates",
                             "PENDING", note="Impact program; requires Impact approval"),
        },
    ],
    "methodology": [
        "We reviewed 20+ mortgage lenders and marketplaces available to US borrowers in October 2026.",
        "Ratings weigh advertised rates and APRs (30%), lender fees and closing costs (25%), product range (20%), digital experience (15%), and verified customer reviews (10%).",
        "We prioritize lenders and marketplaces with live affiliate programs so our guides stay free — this never changes our ratings.",
        "Rates shown are illustrative; your actual rate depends on credit score, down payment, loan type, and market conditions.",
    ],
    "faqs": [
        ("How much does a mortgage cost per month?",
         "It depends on the loan amount, rate, and term. A $400,000 30-year loan at 6.5% is about $2,528/month before taxes and insurance. Use our mortgage calculator to run your numbers."),
        ("What credit score do I need to buy a house?",
         "Conventional loans typically want 620+, FHA loans can go to 580 (or 500 with 10% down), and VA/USDA loans have no official minimum — though most lenders want 620."),
        ("Should I use a mortgage marketplace or go direct to a lender?",
         "Marketplaces like Credible and LendingTree let you compare multiple offers with one application — great for rate shopping. Going direct can make sense if you already have a banking relationship with perks."),
        ("How many lenders should I compare?",
         "At least three. Comparing multiple lenders is the single highest-ROI hour in home buying — even a 0.25% rate difference saves tens of thousands over 30 years."),
    ],
}

# ========================= 2. CREDIT CARDS HUB ============================
cards = {
    "title": "Best Credit Cards of October 2026",
    "url": "/credit-cards",
    "vertical": "credit-cards",
    "crumbs": [("/", "Home"), ("/credit-cards", "Credit Cards")],
    "h1": "Best Credit Cards of October 2026",
    "lead": "The best card is the one that fits how you already spend. We rated dozens of cards across cash back, travel, balance transfers, business, and credit-building — here are the winners.",
    "meta": "Compare the best credit cards of October 2026: cash back, travel, balance transfer, business, student, and secured cards. Independent ratings.",
    "compare_title": "the best credit cards",
    "compare_sub": "Our top-rated cards across every major category this month.",
    "intro": "We score every card on rewards value, fees, welcome offers, APR, and perks — then rank them within their category. Start with the category that matches your spending.",
    "picks": [
        {
            "name": "Wells Fargo Active Cash® Card", "rating": "4.8", "best_for": "Simple flat-rate cash back",
            "specs": [("Rewards", "Unlimited 2% cash back"), ("Annual fee", "$0"), ("APR", "See issuer site")],
            "pros": ["2% on everything — no categories to track", "$0 annual fee", "Cell phone protection"],
            "cons": ["No big bonus categories", "Wells Fargo app gets mixed reviews"],
            "affiliate": aff("cardratings-active-cash", "Wells Fargo Active Cash via CardRatings", "Apply now",
                             "READY-TO-APPLY", note="CardRatings (Red Ventures/QuinStreet) covers dozens of issuers; apply at cardratings.com/affiliate.html"),
        },
        {
            "name": "Chase Sapphire Preferred®", "rating": "4.8", "best_for": "Travel rewards beginners",
            "specs": [("Rewards", "5x travel via Chase, 3x dining"), ("Annual fee", "$95"), ("Welcome offer", "Check current offer")],
            "pros": ["Huge transfer partner network", "Strong travel protections", "$50 hotel credit each year"],
            "cons": ["$95 annual fee", "Best value requires Chase travel portal or transfers"],
            "affiliate": aff("cardratings-sapphire", "Chase Sapphire Preferred via CardRatings", "Apply now",
                             "READY-TO-APPLY", note="via CardRatings publisher program"),
        },
        {
            "name": "Citi® Double Cash Card", "rating": "4.7", "best_for": "Set-it-and-forget-it earners",
            "specs": [("Rewards", "Up to 2% (1% buy + 1% pay)"), ("Annual fee", "$0"), ("Intro APR", "18 months balance transfers")],
            "pros": ["2% effective rate, no annual fee", "Long 0% intro APR on balance transfers", "Simple"],
            "cons": ["Must pay bill to earn the full 2%", "No bonus categories"],
            "affiliate": aff("cardratings-double-cash", "Citi Double Cash via CardRatings", "Apply now",
                             "READY-TO-APPLY", note="via CardRatings publisher program"),
        },
        {
            "name": "Capital One Venture X", "rating": "4.7", "best_for": "Premium travel perks",
            "specs": [("Rewards", "2x on everything, 5x flights"), ("Annual fee", "$395"), ("Credits", "$300 travel + $100 Global Entry")],
            "pros": ["Airport lounge access included", "Annual credits offset most of the fee", "Simple 2x earning"],
            "cons": ["$395 annual fee", "Credits require Capital One Travel booking"],
            "affiliate": aff("capital-one-venture-x", "Capital One Venture X", "Apply now",
                             "PENDING", note="join via CJ dashboard; verify advertiser is live before promoting"),
        },
        {
            "name": "Self Visa® Credit Card", "rating": "4.3", "best_for": "Building credit from scratch",
            "specs": [("Type", "Secured — builds with payments"), ("Annual fee", "See terms"), ("Reports to", "All 3 bureaus")],
            "pros": ["Designed for credit builders", "Reports to all three bureaus", "No hard credit check to start"],
            "cons": ["Requires security deposit or Credit Builder account", "Limited rewards"],
            "affiliate": aff("self-visa", "Self Visa credit-builder card", "Start building",
                             "VERIFIED", note="Impact program verified live ($10/Credit Builder account); confirm card terms in dashboard"),
        },
    ],
    "methodology": [
        "We evaluated 40+ consumer and business cards open to US applicants in October 2026.",
        "Scores weigh rewards value (35%), fees (25%), welcome offers and perks (20%), and APR/terms (20%).",
        "Cards are ranked within their category — a travel card isn't penalized for not earning cash back.",
        "We monetize through CardRatings and issuer affiliate programs; ratings are independent of commissions.",
    ],
    "faqs": [
        ("What is the best credit card for beginners?",
         "A no-annual-fee flat-rate cash back card (like 2% on everything) is the best starter — simple, no categories to game, and it builds history."),
        ("How many credit cards should I have?",
         "Two to three is the sweet spot for most people: one flat-rate card, one bonus-category card, and optionally a travel card. More than that gets hard to manage."),
        ("Does applying hurt my credit score?",
         "A single hard inquiry typically costs a few points for a few months. Rate-shopping multiple cards in a short window counts as one inquiry for scoring purposes in most models."),
        ("Cash back or travel rewards — which is better?",
         "Cash back if you want simplicity and flexibility. Travel rewards if you travel often and will use transfer partners — the value per point is higher but takes effort."),
    ],
}

if __name__ == "__main__":
    write_page("mortgage/index.html", mortgage)
    write_page("credit-cards/index.html", cards)
