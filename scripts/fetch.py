import requests, json, os
from sentiment import analyze_sentiment
from impact import detect_impact
from summarizer import summarize

API_KEY = os.getenv("NEWS_API_KEY")

KEYWORDS = "interest rate OR inflation OR CPI OR NFP OR FOMC OR GDP"

url = "https://newsapi.org/v2/everything"

params = {
    "q": KEYWORDS,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 20,
    "apiKey": API_KEY
}

res = requests.get(url, params=params)
data = res.json()

results = []

for art in data.get("articles", []):
    title = art.get("title","")
    desc = art.get("description","")

    text = title + " " + desc

    sentiment = analyze_sentiment(text)
    usd, gold = detect_impact(text)
    summary = summarize(desc)

    results.append({
        "title": title,
        "time": art.get("publishedAt"),
        "sentiment": sentiment,
        "usd": usd,
        "gold": gold,
        "summary": summary
    })

with open("data/news.json", "w") as f:
    json.dump(results, f, indent=2)
