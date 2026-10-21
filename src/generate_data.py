# Run this once in a python shell or script to generate data/reviews_sample.csv
import pandas as pd
import random

themes = [
    "I was charged a hidden fee during my auto-debit SIP transaction. Very confusing!",
    "Why is there an extra brokerage fee shown on my order statement?",
    "Love the clean app UI, but please make fee breakdowns more transparent.",
    "Hidden charges deducted on withdrawal. Need better explanation in the app.",
    "Great app for mutual fund investment, simple navigation.",
    "Customer support took 3 days to respond to my transaction failure query.",
    "The dark mode layout is amazing, very smooth scrolling.",
    "SIP setup is seamless, but transaction charges are unclear upfront."
]

data = []
for i in range(1, 125):
    data.append({
        "review_id": i,
        "user_id": 1000 + i,
        "date": f"2026-10-{random.randint(1, 28):02d}",
        "rating": random.choice([1, 2, 3, 4, 5]),
        "review_text": random.choice(themes)
    })

# Add a couple of "dirty" rows to test the sanity check
data.append({"review_id": 125, "user_id": 1125, "date": "2026-10-29", "rating": None, "review_text": None}) # Missing data
data.append({"review_id": 126, "user_id": 1126, "date": "2026-10-30", "rating": 6, "review_text": "Invalid rating test"}) # Out of bounds rating

df = pd.DataFrame(data)
df.to_csv("data/reviews_sample.csv", index=False)
print("✅ Generated 126 sample reviews in data/reviews_sample.csv")