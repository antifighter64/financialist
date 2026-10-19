#!/usr/bin/env python3
"""Batch: Credit card sub-pages (12 pages)."""
import sys
sys.path.insert(0, '.')
from generate import write_page
from page_helpers import PROGS, pick_from_program, curated_pick, rated, std_methodology

MONTH = "October 2026"

CARD_BRANDS = [
    ("Wells Fargo Active Cash® Card", "4.8", "Flat 2% on everything",
     [("Rewards", "Unlimited 2% cash back"), ("Annual fee", "$0"), ("Intro APR", "0% intro")],
     ["2% on every purchase, no caps", "$0 annual fee"], ["No bonus categories"],
     "cardratings-active-cash", "READY-TO-APPLY", "via CardRatings"),
    ("Citi® Double Cash Card", "4.7", "2% for disciplined payers",
     [("Rewards", "1% buy + 1% pay"), ("Annual fee", "$0"), ("Intro APR", "0% 18 mo BT")],
     ["Effective 2% with no annual fee", "Great balance-transfer offer"], ["Must pay in full for full 2%"],
     "cardratings-double-cash", "READY-TO-APPLY", "via CardRatings"),
    ("Chase Freedom Unlimited®", "4.7", "Bonus categories + flat rate",
     [("Rewards", "5% travel, 3% dining, 1.5% else"), ("Annual fee", "$0"), ("Bonus", "$200 cash back")],
     ["Strong categories for no-fee card", "$200 welcome bonus"], ["Top rates need Chase portal"],
     "cardratings-freedom-unlimited", "READY-TO-APPLY", "via CardRatings"),
    ("Chase Sapphire Preferred®", "4.8", "Best starter travel card",
     [("Rewards", "5x travel, 3x dining"), ("Annual fee", "$95"), ("Bonus", "60,000 points")],
     ["Huge welcome bonus", "1:1 transfer partners", "Great travel protections"],
     ["$95 annual fee"],
     "cardratings-sapphire-preferred", "READY-TO-APPLY", "via CardRatings"),
    ("Capital One Venture®", "4.6", "Simple travel rewards",
     [("Rewards", "2x on everything"), ("Annual fee", "$95"), ("Bonus", "75,000 miles")],
     ["2x everywhere, no categories", "Easy redemptions"], ["$95 annual fee"],
     "cardratings-venture", "READY-TO-APPLY", "via CardRatings"),
    ("Blue Cash Everyday® (Amex)", "4.5", "Groceries and gas",
     [("Rewards", "3% groceries/gas"), ("Annual fee", "$0"), ("Offer", "Check current")],
     ["Great grocery rate, no fee", "Amex protections"], ["3% capped annually"],
     "amex-blue-cash", "PENDING", "Amex affiliate — verify in dashboard"),
    ("Discover it® Cash Back", "4.6", "Rotating 5% categories",
     [("Rewards", "5% rotating, 1% else"), ("Annual fee", "$0"), ("Match", "Cashback Match year 1")],
     ["5% categories", "First-year match doubles rewards", "$0 fee"], ["Must activate categories quarterly"],
     "discover-it", "READY-TO-APPLY", "via Commission Soup"),
    ("Citi Simplicity®", "4.4", "Balance transfers",
     [("Intro APR", "0% 21 mo BT"), ("Annual fee", "$0"), ("Late fees", "None")],
     ["Longest 0% BT period", "No late fees"], ["No rewards"],
     "cardratings-simplicity", "READY-TO-APPLY", "via CardRatings"),
]

def bp(b):
    n, r, bf, sp, pr, co, sl, st, nt = b
    return curated_pick(n, r, bf, sp, pr, co, sl, st, nt)

BRANDS = [bp(b) for b in CARD_BRANDS]

def card_progs(keywords, n=4):
    picks, seen = [], set()
    for kw in keywords:
        for p in PROGS:
            if p['name'] in seen: continue
            blob = (p['name'] + ' ' + p['notes']).lower()
            if kw.lower() in blob and any(x in blob for x in ['card', 'credit']):
                picks.append(pick_from_program(p, rating=rated(p['name'])))
                seen.add(p['name'])
                if len(picks) >= n: return picks
    return picks

def C(*a):
    return [("/", "Home"), ("/credit-cards", "Credit Cards")] + list(a)

def make(url_path, file_path, crumbs, title, h1, lead, meta, ct, cs, intro, picks, faqs):
    write_page(file_path, {
        "title": title, "url": url_path, "vertical": "credit-cards",
        "crumbs": crumbs, "h1": h1, "lead": lead, "meta": meta,
        "compare_title": ct, "compare_sub": cs, "intro": intro,
        "picks": picks, "methodology": std_methodology([]), "faqs": faqs,
    })

PAGES = [
 # 2.5 business
 ("/credit-cards/business", "credit-cards/business.html", C(("/credit-cards/business","Business")),
  f"Best Business Credit Cards of {MONTH}", f"Best Business Credit Cards of {MONTH}",
  "Separate business spending, earn bigger rewards, and build business credit. Top business cards compared.",
  f"Best business credit cards of {MONTH}. Rewards, 0% APR, and no-fee picks for businesses.",
  "the best business credit cards", "Rewards that scale with your business.",
  "Business cards offer higher limits and richer rewards. These are the best for every business size.",
  BRANDS[4:6] + BRANDS[:2] + card_progs(["business card", "airwallex"], 3),
  [("Do business cards affect personal credit?", "Most require a personal guarantee; some report to personal bureaus. Pay on time regardless."),
   ("Can freelancers get business cards?", "Yes — sole proprietors qualify with SSN and business revenue (even side income)."),
   ("Are business card rewards taxable?", "Generally rebates, not income — but consult a tax pro for large bonuses.")] ),
 # 2.6 student
 ("/credit-cards/student", "credit-cards/student.html", C(("/credit-cards/student","Student")),
  f"Best Student Credit Cards of {MONTH}", f"Best Student Credit Cards of {MONTH}",
  "Build credit from campus with cards designed for students — no credit history required.",
  f"Best student credit cards of {MONTH}. Build credit in college with $0-fee student cards.",
  "the best student credit cards", "Start building credit in college.",
  "The right student card builds your credit score while you study. No history needed.",
  BRANDS[6:7] + BRANDS[2:3] + card_progs(["student card", "petal"], 3),
  [("Do I need income for a student card?", "You need some income or an employed co-signer if under 21 (CARD Act rules)."),
   ("Will a student card build credit?", "Yes — on-time payments build history. Keep utilization under 30%."),
   ("What happens after graduation?", "Most issuers upgrade you to a regular card, keeping your history.")] ),
 # 2.7 secured
 ("/credit-cards/secured", "credit-cards/secured.html", C(("/credit-cards/secured","Secured")),
  f"Best Secured Credit Cards of {MONTH}", f"Best Secured Credit Cards of {MONTH}",
  "Rebuild or establish credit with a security deposit. The best secured cards with the lowest fees.",
  f"Best secured credit cards of {MONTH}. Build credit with refundable deposits, low fees.",
  "the best secured credit cards", "Rebuild credit the smart way.",
  "Secured cards are the fastest path to a good score when used right. Lowest fees, best upgrade paths.",
  BRANDS[6:7] + card_progs(["secured", "self financial", "kikoff", "merrick", "indigo"], 5),
  [("How does a secured card work?", "You put down a refundable deposit (usually $200+), which becomes your credit limit."),
   ("When do I get my deposit back?", "After 6-12 months of on-time payments, many issuers graduate you to unsecured and refund it."),
   ("Do secured cards build credit?", "Yes — they report to all three bureaus like regular cards.")] ),
 # 2.8 no-annual-fee
 ("/credit-cards/no-annual-fee", "credit-cards/no-annual-fee.html", C(("/credit-cards/no-annual-fee","No Annual Fee")),
  f"Best No-Annual-Fee Credit Cards of {MONTH}", f"Best No-Annual-Fee Credit Cards of {MONTH}",
  "Great rewards without the yearly cost. The best $0-annual-fee cards for every spending style.",
  f"Best no-annual-fee credit cards of {MONTH}. Top $0-fee cards with real rewards.",
  "the best no-annual-fee cards", "$0 fee, real rewards.",
  "You don't need to pay to play. These cards deliver strong rewards with no annual fee.",
  BRANDS[:3] + BRANDS[6:7] + card_progs(["no annual fee"], 2),
  [("Are no-fee cards worth it?", "Absolutely — many beat paid cards for moderate spenders once you subtract the fee."),
   ("Can I upgrade later?", "Yes — issuers let you product-change to premium cards, keeping your history."),
   ("Do no-fee cards have foreign transaction fees?", "Some do; check before traveling.")] ),
 # 2.9 rewards
 ("/credit-cards/rewards", "credit-cards/rewards.html", C(("/credit-cards/rewards","Rewards")),
  f"Best Rewards Credit Cards of {MONTH}", f"Best Rewards Credit Cards of {MONTH}",
  "Maximize every dollar with the highest-earning rewards cards — points, miles, and cash back.",
  f"Best rewards credit cards of {MONTH}. Top points, miles, and cash back cards compared.",
  "the best rewards credit cards", "Every dollar, maximized.",
  "The best rewards card matches your spending. These earn the most across categories.",
  BRANDS[:5] + card_progs(["rewards card"], 2),
  [("Points or cash back?", "Cash is simple and never devalues. Points win for frequent travelers using transfer partners."),
   ("How much are points worth?", "Roughly 1-2 cents each, more with smart transfers. Never hoard — they devalue."),
   ("Do rewards expire?", "Usually not while the account is open, but check your issuer.")] ),
 # 2.10 airline
 ("/credit-cards/airline", "credit-cards/airline.html", C(("/credit-cards/airline","Airline")),
  f"Best Airline Credit Cards of {MONTH}", f"Best Airline Credit Cards of {MONTH}",
  "Free checked bags, priority boarding, and miles toward free flights. Best airline cards compared.",
  f"Best airline credit cards of {MONTH}. Free bags, lounge access, and miles compared.",
  "the best airline credit cards", "Fly more, pay less.",
  "Loyal to an airline? Their card pays for itself in bags and perks alone.",
  BRANDS[3:5] + BRANDS[:1] + card_progs(["airline"], 3),
  [("Are airline cards worth the fee?", "If you fly the airline 2+ times a year, free bags alone usually cover it."),
   ("What are miles worth?", "~1.2-1.5 cents each on average; more for premium cabins."),
   ("Card or transferable points?", "Transferable points (Chase, Amex, Capital One) offer more flexibility than single-airline miles.")] ),
 # 2.11 hotel
 ("/credit-cards/hotel", "credit-cards/hotel.html", C(("/credit-cards/hotel","Hotel")),
  f"Best Hotel Credit Cards of {MONTH}", f"Best Hotel Credit Cards of {MONTH}",
  "Free anniversary nights, elite status, and bonus points. The best hotel cards for every chain.",
  f"Best hotel credit cards of {MONTH}. Free nights, elite status, and points compared.",
  "the best hotel credit cards", "Sleep free, upgrade often.",
  "One free anniversary night can cover the annual fee. These are the best hotel cards.",
  BRANDS[3:4] + BRANDS[:2] + card_progs(["hotel"], 3),
  [("Are hotel cards worth it?", "The anniversary free night alone often exceeds the annual fee."),
   ("Which chain?", "Pick the chain you actually stay with — status and points only matter there."),
   ("Do points expire?", "Most don't with account activity; check your program.")] ),
 # 2.12 0-apr
 ("/credit-cards/0-apr", "credit-cards/0-apr.html", C(("/credit-cards/0-apr","0% APR")),
  f"Best 0% APR Credit Cards of {MONTH}", f"Best 0% APR Credit Cards of {MONTH}",
  "Up to 21 months with no interest on purchases or balance transfers. The longest 0% APR offers.",
  f"Best 0% APR credit cards of {MONTH}. Longest intro periods for purchases and transfers.",
  "the best 0% APR cards", "Up to 21 months, zero interest.",
  "A long 0% period is free money if you have a payoff plan. These are the longest offers.",
  [BRANDS[7]] + BRANDS[:2] + card_progs(["0% apr", "balance transfer"], 3),
  [("How long is 0% APR?", "Up to 21 months on balance transfers, 12-15 on purchases at top cards."),
   ("Is there a transfer fee?", "Usually 3-5%. Factor it into your savings math."),
   ("What happens after?", "The regular APR (often 20%+) kicks in — have a payoff plan.")] ),
 # 2.13 bad-credit
 ("/credit-cards/bad-credit", "credit-cards/bad-credit.html", C(("/credit-cards/bad-credit","Bad Credit")),
  f"Best Credit Cards for Bad Credit of {MONTH}", f"Best Credit Cards for Bad Credit of {MONTH}",
  "Rebuild with cards designed for low scores — reasonable fees, real credit reporting, upgrade paths.",
  f"Best credit cards for bad credit of {MONTH}. Rebuild your score with honest, low-fee cards.",
  "the best cards for bad credit", "Rebuild without getting ripped off.",
  "Bad credit doesn't mean bad cards have to rip you off. These report properly and graduate.",
  BRANDS[6:7] + card_progs(["bad credit", "credit one", "indigo", "milestone", "premier"], 5),
  [("Can I get a card with bad credit?", "Yes — secured cards and subprime unsecured cards accept scores in the 500s."),
   ("How fast will my score improve?", "With on-time payments and low utilization, meaningful gains in 6-12 months."),
   ("Avoid?", "Cards with monthly fees, no grace period, or that don't report to all three bureaus.")] ),
 # 2.14 credit-builder
 ("/credit-cards/credit-builder", "credit-cards/credit-builder.html", C(("/credit-cards/credit-builder","Credit Builder")),
  f"Best Credit-Builder Cards & Tools of {MONTH}", f"Best Credit-Builder Cards & Tools of {MONTH}",
  "Cards and apps built to grow your score from scratch — no hard inquiry options included.",
  f"Best credit-builder cards of {MONTH}. Grow your score with no hard inquiry options.",
  "the best credit-builder tools", "From no score to good score.",
  "These tools build real credit history — some without even a hard inquiry.",
  card_progs(["self financial", "kikoff", "extra card", "credit builder"], 5) + BRANDS[6:7],
  [("Do credit-builder loans work?", "Yes — payments are reported to bureaus, building history. You get the money at the end."),
   ("Hard inquiry?", "Many builder products use soft pulls only — no score impact to start."),
   ("How long to see results?", "Typically 3-6 months of on-time payments.")] ),
 # 2.15 dining
 ("/credit-cards/dining", "credit-cards/dining.html", C(("/credit-cards/dining","Dining")),
  f"Best Dining & Restaurant Credit Cards of {MONTH}", f"Best Dining & Restaurant Credit Cards of {MONTH}",
  "Earn 3-4%+ on restaurants, takeout, and delivery. The best cards for food lovers.",
  f"Best dining credit cards of {MONTH}. Top rewards on restaurants, takeout, and delivery.",
  "the best dining cards", "Get paid to eat out.",
  "If restaurants are a big budget line, the right card pays you 3-4% back on every meal.",
  BRANDS[2:3] + BRANDS[5:6] + BRANDS[:1] + card_progs(["dining"], 2),
  [("What counts as dining?", "Restaurants, cafes, takeout, and usually delivery apps. Groceries are separate."),
   ("Best rate?", "Up to 4%+ on top cards; 3% is excellent for a no-fee card."),
   ("Delivery apps included?", "Usually yes — DoorDash, Uber Eats typically code as dining.")] ),
 # 2.16 gas
 ("/credit-cards/gas", "credit-cards/gas.html", C(("/credit-cards/gas","Gas")),
  f"Best Gas Credit Cards of {MONTH}", f"Best Gas Credit Cards of {MONTH}",
  "Save at the pump with 3-5% back on gas. The best cards for drivers.",
  f"Best gas credit cards of {MONTH}. Top rewards at the pump compared.",
  "the best gas cards", "Save every fill-up.",
  "Commuters and road-trippers: the right card cuts your fuel bill 3-5%.",
  BRANDS[5:6] + BRANDS[:2] + card_progs(["gas"], 2),
  [("Best gas rate?", "3-5% on top cards; warehouse clubs sometimes higher."),
   ("EV charging count?", "Some cards now include EV charging in bonus categories — check terms."),
   ("Station restrictions?", "Some exclude warehouse clubs or require pay-at-pump.")] ),
]

for p in PAGES:
    make(*p)
print("DONE credit cards batch")
