#!/usr/bin/env python3
"""Batch: Banking sub-pages (11 pages)."""
import sys
sys.path.insert(0, '.')
from generate import write_page
from page_helpers import PROGS, pick_from_program, curated_pick, rated, std_methodology

MONTH = "October 2026"

BANK_BRANDS = [
    ("Relay Financial", "4.6", "Business banking with no fees",
     [("Monthly fee", "$0"), ("APY", "Competitive"), ("Best for", "Small business")],
     ["No account fees or minimums", "Multiple checking accounts", "Strong integrations"],
     ["Business only — no personal accounts"],
     "relay-financial", "READY-TO-APPLY", "direct — $50-$300 per account"),
    ("Acorns", "4.4", "Invest spare change + banking",
     [("APY", "Competitive"), ("Fee", "From $3/mo"), ("Best for", "Beginners")],
     ["Round-ups invest automatically", "Banking + investing in one app"],
     ["Monthly fee", "Limited banking features"],
     "acorns", "READY-TO-APPLY", "via Impact/FlexOffers"),
    ("Greenlight", "4.5", "Banking for kids & teens",
     [("Fee", "From $4.99/mo"), ("Best for", "Families"), ("Controls", "Parental")],
     ["Chores & allowance tools", "Spending controls for parents", "Investing for kids"],
     ["Monthly fee", "Kids-focused only"],
     "greenlight", "READY-TO-APPLY", "via MaxBounty — $37.50/lead"),
    ("Ally Bank", "4.5", "Online bank, no fees",
     [("Monthly fee", "$0"), ("APY", "High-yield"), ("Best for", "Online banking")],
     ["No monthly fees", "High savings APY", "Great app"],
     ["No branches"],
     "ally-bank", "READY-TO-APPLY", "verify in CJ dashboard"),
    ("Chime", "4.3", "Fee-free mobile banking",
     [("Monthly fee", "$0"), ("Best for", "Mobile-first"), ("Overdraft", "SpotMe")],
     ["No fees", "Early direct deposit", "Easy signup"],
     ["No joint accounts", "Customer service varies"],
     "chime", "READY-TO-APPLY", "verify in CJ dashboard"),
    ("Discover Bank", "4.6", "Online bank, cashback debit",
     [("Monthly fee", "$0"), ("APY", "High-yield"), ("Debit rewards", "1% cashback")],
     ["Cashback on debit", "No fees", "60,000+ ATMs"],
     ["No branches"],
     "discover-bank", "READY-TO-APPLY", "verify in dashboard"),
]

def bp(b):
    n, r, bf, sp, pr, co, sl, st, nt = b
    return curated_pick(n, r, bf, sp, pr, co, sl, st, nt)

BRANDS = [bp(b) for b in BANK_BRANDS]

def bank_progs(keywords, n=4):
    picks, seen = [], set()
    for kw in keywords:
        for p in PROGS:
            if p['name'] in seen: continue
            blob = (p['name'] + ' ' + p['notes']).lower()
            if kw.lower() in blob and any(x in blob for x in ['bank', 'saving', 'checking', 'cd ', 'deposit', 'account']):
                picks.append(pick_from_program(p, rating=rated(p['name'])))
                seen.add(p['name'])
                if len(picks) >= n: return picks
    return picks

def C(*a):
    return [("/", "Home"), ("/banking", "Banking")] + list(a)

def make(url_path, file_path, crumbs, title, h1, lead, meta, ct, cs, intro, picks, faqs):
    write_page(file_path, {
        "title": title, "url": url_path, "vertical": "banking",
        "crumbs": crumbs, "h1": h1, "lead": lead, "meta": meta,
        "compare_title": ct, "compare_sub": cs, "intro": intro,
        "picks": picks, "methodology": std_methodology([]), "faqs": faqs,
    })

PAGES = [
 ("/banking", "banking/index.html", C(),
  f"Best Bank Accounts of {MONTH}", f"Best Bank Accounts of {MONTH}",
  "The best checking, savings, and CD accounts — high yields, low fees, compared.",
  f"Compare the best bank accounts of {MONTH}. Checking, savings, CDs with top rates.",
  "the best bank accounts", "Every account type, ranked.",
  "The best bank account depends on how you use it. These are our top picks across every category.",
  BRANDS + bank_progs(["banking", "savings"], 2),
  [("Online vs traditional bank?", "Online banks pay higher rates with fewer fees; traditional banks offer branches and in-person service."),
   ("Are online banks safe?", "Yes — if FDIC insured, your deposits are protected up to $250,000, same as any bank."),
   ("How many bank accounts should I have?", "At least checking + high-yield savings. Add more for specific goals.")] ),
 ("/banking/checking", "banking/checking.html", C(("/banking/checking","Checking")),
  f"Best Checking Accounts of {MONTH}", f"Best Checking Accounts of {MONTH}",
  "Free checking with no monthly fees, no minimums, and ATM access. Top checking accounts compared.",
  f"Best checking accounts of {MONTH}. No-fee checking with ATM access compared.",
  "the best checking accounts", "Free checking, really free.",
  "The best checking account charges nothing and gives everywhere-access. These are our picks.",
  BRANDS[3:6] + BRANDS[:1] + bank_progs(["checking"], 2),
  [("What fees to avoid?", "Monthly maintenance, overdraft, and out-of-network ATM fees."),
   ("Minimum balance?", "Best accounts have none. Avoid accounts requiring $1,500+ to waive fees."),
   ("Overdraft protection?", "Link savings or opt into no-fee overdraft programs like SpotMe.")] ),
 ("/banking/money-market", "banking/money-market.html", C(("/banking/money-market","Money Market")),
  f"Best Money Market Accounts of {MONTH}", f"Best Money Market Accounts of {MONTH}",
  "Higher rates than savings with check-writing. Best money market accounts compared.",
  f"Best money market accounts of {MONTH}. High rates with check access compared.",
  "the best money market accounts", "Savings rates, checking flexibility.",
  "Money markets split the difference between savings and checking. Best rates here.",
  BRANDS[3:4] + BRANDS[5:6] + bank_progs(["money market"], 2),
  [("Money market vs savings?", "Money markets may offer checks/debit cards; savings usually pays slightly more."),
   ("Are they FDIC insured?", "Yes, at banks. Money market *funds* at brokerages are different (SIPC, not FDIC)."),
   ("Minimums?", "Some require $500-$2,500; best have none.")] ),
 ("/banking/business-checking", "banking/business-checking.html", C(("/banking/business-checking","Business Checking")),
  f"Best Business Checking Accounts of {MONTH}", f"Best Business Checking Accounts of {MONTH}",
  "No-fee business checking with the tools small businesses need. Compared for owners.",
  f"Best business checking of {MONTH}. No-fee accounts for small businesses compared.",
  "the best business checking accounts", "Built for business owners.",
  "Business banking shouldn't eat your margins. These accounts are free and full-featured.",
  BRANDS[:1] + BRANDS[3:4] + bank_progs(["business banking", "relay", "northone"], 3),
  [("Do I need a separate business account?", "Yes — for taxes, liability protection, and professionalism."),
   ("What documents?", "EIN or SSN (sole prop), business license, ID."),
   ("Fees to watch?", "Monthly fees, transaction limits, cash deposit fees.")] ),
 ("/banking/business-savings", "banking/business-savings.html", C(("/banking/business-savings","Business Savings")),
  f"Best Business Savings Accounts of {MONTH}", f"Best Business Savings Accounts of {MONTH}",
  "Earn on your business cash reserves. Best business savings rates compared.",
  f"Best business savings accounts of {MONTH}. High yields for business cash compared.",
  "the best business savings accounts", "Your business cash, earning.",
  "Idle business cash should earn. These accounts pay top rates on reserves.",
  BRANDS[:1] + BRANDS[3:4] + bank_progs(["business savings"], 2),
  [("Why separate business savings?", "Tax reserves, emergency fund, and large purchases — kept distinct."),
   ("APY?", "Top business savings pay competitive rates; compare often."),
   ("Limits?", "Six-withdrawal rule is gone federally, but banks may still limit.")] ),
 ("/banking/online-banks", "banking/online-banks.html", C(("/banking/online-banks","Online Banks")),
  f"Best Online Banks of {MONTH}", f"Best Online Banks of {MONTH}",
  "Higher rates, lower fees, no branches needed. The best online banks compared.",
  f"Best online banks of {MONTH}. High rates and low fees compared.",
  "the best online banks", "Bank from anywhere.",
  "Online banks pass branch savings to you as higher rates. These are the best.",
  BRANDS[3:6] + bank_progs(["online bank"], 2),
  [("Are online banks safe?", "Yes — FDIC insurance applies identically."),
   ("Cash deposits?", "Some partner with ATM networks; others don't take cash well."),
   ("Customer service?", "24/7 chat/phone at the best; check reviews.")] ),
 ("/banking/student-banking", "banking/student-banking.html", C(("/banking/student-banking","Student Banking")),
  f"Best Student Bank Accounts of {MONTH}", f"Best Student Bank Accounts of {MONTH}",
  "No-fee accounts for students with the apps and tools campus life needs.",
  f"Best student bank accounts of {MONTH}. No-fee student checking and savings.",
  "the best student bank accounts", "Banking for campus life.",
  "Student accounts waive fees and keep it simple. Best picks for students.",
  BRANDS[4:5] + BRANDS[3:4] + bank_progs(["student bank"], 2),
  [("Student vs regular?", "Student accounts waive fees with enrollment verification; convert after graduation."),
   ("Overdraft?", "Opt out — overdraft fees hit students hardest."),
   ("What do I need to open?", "ID, SSN, proof of enrollment.")] ),
 ("/banking/joint-accounts", "banking/joint-accounts.html", C(("/banking/joint-accounts","Joint Accounts")),
  f"Best Joint Bank Accounts of {MONTH}", f"Best Joint Bank Accounts of {MONTH}",
  "Share finances smoothly with the best joint checking and savings accounts.",
  f"Best joint bank accounts of {MONTH}. Joint checking and savings compared.",
  "the best joint accounts", "Money, together.",
  "The right joint account makes shared money simple. Best picks for couples and partners.",
  BRANDS[3:6] + bank_progs(["joint"], 1),
  [("Joint or separate?", "Many couples do both: joint for shared bills, separate for personal."),
   ("Both owners equal?", "Yes — either owner can withdraw. Choose a partner you trust fully."),
   ("What if we split?", "Either can drain it. Keep an individual emergency fund.")] ),
 ("/banking/kids-banking", "banking/kids-banking.html", C(("/banking/kids-banking","Kids Banking")),
  f"Best Banking for Kids & Teens of {MONTH}", f"Best Banking for Kids & Teens of {MONTH}",
  "Teach money skills with accounts built for kids — parental controls included.",
  f"Best kids bank accounts of {MONTH}. Parental controls and money lessons compared.",
  "the best kids bank accounts", "Money lessons, built in.",
  "The best kids accounts teach earning, saving, and spending — with guardrails.",
  BRANDS[2:3] + BRANDS[1:2] + bank_progs(["kids", "greenlight", "acorns"], 2),
  [("What age?", "Most allow 6+ with a parent as joint owner; teens get debit cards."),
   ("Fees?", "Many charge $5/mo — weigh against the lessons."),
   ("Do they build credit?", "No — but they build habits. Credit comes later.")] ),
 ("/banking/no-fee-checking", "banking/no-fee-checking.html", C(("/banking/no-fee-checking","No-Fee Checking")),
  f"Best No-Fee Checking Accounts of {MONTH}", f"Best No-Fee Checking Accounts of {MONTH}",
  "Truly free checking: no monthly fee, no minimum, no gotchas.",
  f"Best free checking accounts of {MONTH}. No monthly fees, no minimums.",
  "the best free checking accounts", "Free means free.",
  "No monthly fee, no minimum balance games. These checking accounts are actually free.",
  BRANDS[3:6] + bank_progs(["no fee", "free checking"], 1),
  [("Truly free?", "The picks here have no monthly fee and no minimum to avoid one."),
   ("Overdraft?", "Decline overdraft 'protection' — it's a $35 fee machine."),
   ("ATM access?", "Look for 50,000+ fee-free ATMs or rebates.")] ),
 ("/banking/savings-bonus", "banking/savings-bonus.html", C(("/banking/savings-bonus","Bank Bonuses")),
  f"Best Bank Bonuses & Promotions of {MONTH}", f"Best Bank Bonuses & Promotions of {MONTH}",
  "Earn $200-$3,000+ for opening an account. The best bank bonuses right now.",
  f"Best bank account bonuses of {MONTH}. Earn cash for opening checking and savings.",
  "the best bank bonuses", "Get paid to switch.",
  "Banks pay big to win your deposits. These bonuses are actually worth the effort.",
  BRANDS[3:6] + bank_progs(["bonus", "promotion"], 1),
  [("What's the catch?", "Direct deposit and/or minimum balance requirements, usually for 60-90 days."),
   ("Taxes?", "Bonuses are taxable interest income — you'll get a 1099-INT."),
   ("Can I get multiple?", "Yes — but don't open accounts you won't use; ChexSystems tracks openings.")] ),
]

for p in PAGES:
    make(*p)
print("DONE banking batch")
