#!/usr/bin/env python3
"""Batch: Investing sub-pages (12 pages)."""
import sys
sys.path.insert(0, '.')
from generate import write_page
from page_helpers import PROGS, pick_from_program, curated_pick, rated, std_methodology

MONTH = "October 2026"
ROBINHOOD_LIVE = "https://join.robinhood.com/borisk90"

INV_BRANDS = [
    ("Robinhood", "4.5", "Commission-free trading",
     [("Commissions", "$0"), ("Fractional", "Yes"), ("IRA", "1% match")],
     ["$0 commissions", "1% IRA match", "Easy app"],
     ["Limited research tools", "Past outages"],
     "robinhood", "live", "", ROBINHOOD_LIVE),
    ("Fidelity", "4.8", "Best overall brokerage",
     [("Commissions", "$0"), ("Research", "Excellent"), ("Funds", "Zero-fee index")],
     ["Top research", "Zero-fee funds", "Great service"],
     ["App less slick than fintechs"],
     "fidelity", "READY-TO-APPLY", "verify in CJ dashboard"),
    ("Vanguard", "4.8", "Low-cost index pioneer",
     [("Commissions", "$0"), ("Funds", "Lowest fees"), ("Best for", "Long-term")],
     ["Lowest fund fees", "Investor-owned structure"],
     ["Dated app experience"],
     "vanguard", "READY-TO-APPLY", "affiliate program"),
    ("Charles Schwab", "4.7", "Full-service, $0 trades",
     [("Commissions", "$0"), ("Branches", "Yes"), ("Research", "Strong")],
     ["Branches + app", "Great research", "Banking built in"],
     ["Cash sweep yields lower"],
     "schwab", "PENDING", "via CJ — application in flight"),
    ("Acorns", "4.4", "Invest spare change",
     [("Fee", "From $3/mo"), ("Best for", "Beginners"), ("IRA", "Yes")],
     ["Automatic round-ups", "Simple portfolios"],
     ["Monthly fee", "Limited control"],
     "acorns-invest", "READY-TO-APPLY", "via Impact/FlexOffers"),
    ("Betterment", "4.6", "Best robo-advisor",
     [("Fee", "0.25%"), ("Best for", "Hands-off"), ("Tax-loss", "Yes")],
     ["Tax-loss harvesting", "Goal-based portfolios"],
     ["0.25% fee", "Limited customization"],
     "betterment", "READY-TO-APPLY", "affiliate program"),
    ("Wealthfront", "4.5", "Automated investing",
     [("Fee", "0.25%"), ("Best for", "Hands-off"), ("APY", "High cash")],
     ["Tax-loss harvesting", "High-yield cash account"],
     ["0.25% fee"],
     "wealthfront", "READY-TO-APPLY", "affiliate program"),
    ("Public.com", "4.3", "Social investing",
     [("Commissions", "$0"), ("Fractional", "Yes"), ("Best for", "Community")],
     ["Social features", "Fractional shares"],
     ["Smaller than big brokers"],
     "public-com", "PENDING", "via Everflow"),
]

def bp(b):
    n, r, bf, sp, pr, co, sl, st, nt = b[:9]
    href = b[9] if len(b) > 9 else None
    p = curated_pick(n, r, bf, sp, pr, co, sl, st, nt)
    if href:
        p["affiliate"]["href"] = href
        p["affiliate"]["status"] = "live"
    return p

BRANDS = [bp(b) for b in INV_BRANDS]

def inv_progs(keywords, n=4):
    picks, seen = [], set()
    for kw in keywords:
        for p in PROGS:
            if p['name'] in seen: continue
            blob = (p['name'] + ' ' + p['notes']).lower()
            if kw.lower() in blob and any(x in blob for x in ['invest', 'broker', 'trading', 'crypto', 'gold', 'ira']):
                picks.append(pick_from_program(p, rating=rated(p['name'])))
                seen.add(p['name'])
                if len(picks) >= n: return picks
    return picks

def C(*a):
    return [("/", "Home"), ("/investing", "Investing")] + list(a)

def make(url_path, file_path, crumbs, title, h1, lead, meta, ct, cs, intro, picks, faqs):
    write_page(file_path, {
        "title": title, "url": url_path, "vertical": "investing",
        "crumbs": crumbs, "h1": h1, "lead": lead, "meta": meta,
        "compare_title": ct, "compare_sub": cs, "intro": intro,
        "picks": picks, "methodology": std_methodology([]), "faqs": faqs,
    })

PAGES = [
 ("/investing", "investing/index.html", C(),
  f"Best Investing Platforms of {MONTH}", f"Best Investing Platforms of {MONTH}",
  "Brokerages, robo-advisors, and apps — the best places to invest this year.",
  f"Best investing platforms of {MONTH}. Brokerages and robo-advisors compared.",
  "the best investing platforms", "Every way to invest, ranked.",
  "The best platform fits your style — DIY, automated, or somewhere between.",
  BRANDS[:6] + inv_progs(["brokerage"], 2),
  [("How much to start?", "Many brokerages have $0 minimums. Start with what you can."),
   ("Brokerage vs robo-advisor?", "Brokerages = you pick. Robos = automated portfolios for 0.25%."),
   ("Are my investments safe?", "SIPC protects up to $500k in securities if a brokerage fails.")] ),
 ("/investing/robo-advisors", "investing/robo-advisors.html", C(("/investing/robo-advisors","Robo-Advisors")),
  f"Best Robo-Advisors of {MONTH}", f"Best Robo-Advisors of {MONTH}",
  "Automated portfolios, tax-loss harvesting, 0.25% fees. The best robo-advisors compared.",
  f"Best robo-advisors of {MONTH}. Automated investing with low fees compared.",
  "the best robo-advisors", "Investing on autopilot.",
  "Robo-advisors build and manage your portfolio for a fraction of advisor cost.",
  BRANDS[5:7] + BRANDS[4:5] + inv_progs(["robo"], 2),
  [("What do robos charge?", "Typically 0.25% annually, plus fund fees."),
   ("Tax-loss harvesting?", "Top robos harvest losses automatically — a real after-tax edge."),
   ("Can I customize?", "Somewhat — risk level, goals, some exclusions. Not stock-picking.")] ),
 ("/investing/iras", "investing/iras.html", C(("/investing/iras","IRAs")),
  f"Best IRA Accounts of {MONTH}", f"Best IRA Accounts of {MONTH}",
  "The best IRA providers — low fees, great funds, and easy rollovers.",
  f"Best IRA accounts of {MONTH}. Low-fee IRAs with top fund selection.",
  "the best IRA accounts", "Retire richer.",
  "The right IRA saves you thousands in fees over decades. These are the best.",
  BRANDS[:4] + inv_progs(["ira"], 2),
  [("Traditional or Roth?", "Traditional = deduction now; Roth = tax-free later. Roth wins for most young savers."),
   ("Contribution limit?", "For 2026: $7,000 ($8,000 if 50+)."),
   ("Can I have multiple IRAs?", "Yes — but the limit applies across all of them.")] ),
 ("/investing/roth-ira", "investing/roth-ira.html", C(("/investing/roth-ira","Roth IRA")),
  f"Best Roth IRA Accounts of {MONTH}", f"Best Roth IRA Accounts of {MONTH}",
  "Tax-free growth and withdrawals. The best Roth IRA providers compared.",
  f"Best Roth IRA accounts of {MONTH}. Tax-free growth with top providers.",
  "the best Roth IRA accounts", "Tax-free forever.",
  "Roth IRAs are the closest thing to a perfect retirement account. Best providers here.",
  BRANDS[:4] + inv_progs(["roth"], 1),
  [("Income limits?", "Phase-outs apply at higher incomes; backdoor Roths exist."),
   ("Withdrawals?", "Contributions anytime tax-free; earnings after 59½ and 5-year rule."),
   ("Roth vs 401(k)?", "Do both if you can — 401(k) match first, then Roth.")] ),
 ("/investing/401k", "investing/401k.html", C(("/investing/401k","401(k)")),
  f"401(k) Rollover Guide {MONTH}", "401(k) Rollover Guide",
  "Left a job? Roll your 401(k) into an IRA for lower fees and more choices.",
  f"401(k) rollover guide {MONTH}. How to roll over to an IRA with lower fees.",
  "401(k) rollover options", "Don't leave money behind.",
  "Rolling over gives you control and usually lower fees. Here's how.",
  BRANDS[:4],
  [("Should I roll over?", "Usually yes — IRAs have lower fees and more choices than most 401(k)s."),
   ("Direct vs indirect?", "Direct (trustee-to-trustee) avoids withholding and deadlines."),
   ("What about my match?", "Always contribute enough to get the full employer match first.")] ),
 ("/investing/crypto", "investing/crypto.html", C(("/investing/crypto","Crypto")),
  f"Best Crypto Platforms of {MONTH}", f"Best Crypto Platforms of {MONTH}",
  "Buy Bitcoin and crypto with low fees and strong security. Best platforms compared.",
  f"Best crypto platforms of {MONTH}. Low fees and strong security compared.",
  "the best crypto platforms", "Crypto, done safely.",
  "Stick to reputable platforms with real security. These are the best.",
  inv_progs(["crypto", "moonpay", "bitcoin"], 5) + BRANDS[:1],
  [("How much crypto?", "Most advisors suggest 1-5% of a portfolio — it's volatile."),
   ("Exchange vs wallet?", "Buy on an exchange; move large amounts to your own wallet."),
   ("Taxes?", "Crypto sales are taxable events. Track everything.")] ),
 ("/investing/apps", "investing/apps.html", C(("/investing/apps","Apps")),
  f"Best Investing Apps of {MONTH}", f"Best Investing Apps of {MONTH}",
  "Trade from your phone with $0 commissions. The best investing apps compared.",
  f"Best investing apps of {MONTH}. $0-commission mobile trading compared.",
  "the best investing apps", "Your portfolio in your pocket.",
  "The best apps make investing effortless — without pushing you to overtrade.",
  BRANDS[:2] + BRANDS[7:8] + BRANDS[4:5] + inv_progs(["investing app"], 1),
  [("Are app brokers safe?", "Yes if SIPC-insured. Watch for gamification pushing frequent trading."),
   ("Fractional shares?", "Top apps let you buy $1 of any stock."),
   ("Best for beginners?", "Simple apps with education built in.")] ),
 ("/investing/gold-ira", "investing/gold-ira.html", C(("/investing/gold-ira","Gold IRA")),
  f"Best Gold IRA Companies of {MONTH}", f"Best Gold IRA Companies of {MONTH}",
  "Hold physical gold in a retirement account. The most reputable gold IRA companies.",
  f"Best gold IRA companies of {MONTH}. Reputable precious metals IRAs compared.",
  "the best gold IRA companies", "Gold for retirement.",
  "Gold IRAs have high fees — only the reputable firms are worth considering.",
  inv_progs(["gold ira", "golden"], 4) + BRANDS[1:2],
  [("What is a gold IRA?", "A self-directed IRA holding physical precious metals."),
   ("Fees?", "Setup, storage, and custodian fees — often $200+/year. Compare carefully."),
   ("Worth it?", "Gold is a diversifier, not a growth engine. Keep allocations small.")] ),
 ("/investing/beginners", "investing/beginners.html", C(("/investing/beginners","Beginners")),
  f"Investing for Beginners — Start in {MONTH}", "Investing for Beginners — Start Here",
  "New to investing? Start here: the simplest path from $0 to your first portfolio.",
  f"Investing for beginners {MONTH}. The simplest path to your first portfolio.",
  "beginner investing options", "Start today, thank yourself later.",
  "You don't need much money or knowledge to start. Here's the simplest path.",
  BRANDS[:2] + BRANDS[4:6] + inv_progs(["beginner"], 1),
  [("How much to start?", "$0 at many brokerages. Even $50/month builds wealth."),
   ("What should I buy first?", "A total-market index fund. Simple, diversified, low-fee."),
   ("When?", "Now. Time in the market beats timing the market.")] ),
 ("/investing/retirement", "investing/retirement.html", C(("/investing/retirement","Retirement")),
  f"Best Retirement Accounts of {MONTH}", f"Best Retirement Accounts of {MONTH}",
  "IRAs, 401(k)s, and taxable accounts — the best places to save for retirement.",
  f"Best retirement accounts of {MONTH}. IRAs and 401(k)s compared.",
  "the best retirement accounts", "Retire on your terms.",
  "The right accounts save you thousands in taxes and fees. These are the best.",
  BRANDS[:5] + inv_progs(["retirement"], 1),
  [("How much to save?", "Aim for 15% of income including employer match."),
   ("Order of operations?", "401(k) to match → Roth IRA → back to 401(k) → taxable."),
   ("What investments?", "Low-cost target-date or total-market index funds.")] ),
 ("/investing/fractional-shares", "investing/fractional-shares.html", C(("/investing/fractional-shares","Fractional Shares")),
  f"Best Fractional-Share Brokerages of {MONTH}", f"Best Fractional-Share Brokerages of {MONTH}",
  "Buy $1 of Amazon or Tesla. The best brokerages for fractional shares.",
  f"Best fractional-share brokerages of {MONTH}. Buy slices of any stock.",
  "the best fractional-share brokerages", "Own a slice of anything.",
  "Fractional shares let small accounts diversify like big ones.",
  BRANDS[:2] + BRANDS[7:8] + inv_progs(["fractional"], 1),
  [("How do fractional shares work?", "The broker buys whole shares and splits them among investors."),
   ("Dividends?", "Yes — paid proportionally."),
   ("Can I transfer?", "Usually yes via ACATS, though some brokers liquidate fractions.")] ),
 ("/investing/esg", "investing/esg.html", C(("/investing/esg","ESG")),
  f"Best ESG Investing Options of {MONTH}", f"Best ESG Investing Options of {MONTH}",
  "Invest your values: the best ESG funds and platforms for socially responsible investing.",
  f"Best ESG investing of {MONTH}. Socially responsible funds and platforms.",
  "the best ESG investing options", "Profit with principles.",
  "ESG investing has grown up — competitive returns without compromising values.",
  BRANDS[1:3] + BRANDS[5:6] + inv_progs(["esg", "sustainable"], 1),
  [("Does ESG underperform?", "Studies show competitive long-term returns vs. conventional funds."),
   ("What does ESG screen?", "Environmental, social, governance factors — varies by fund."),
   ("Greenwashing?", "Check actual holdings; some 'ESG' funds barely differ.")] ),
]

for p in PAGES:
    make(*p)
print("DONE investing batch")
