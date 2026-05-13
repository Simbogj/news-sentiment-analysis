# Financial News Sentiment Analysis

A rigorous, end-to-end analytical pipeline that quantifies the sentiment expressed in financial news headlines, computes technical indicators on historical stock price data, and measures the statistical relationship between the two — to support investment strategy recommendations for **Nova Financial Solutions**.

---

## Project Structure

```
news-sentiment-analysis/
├── .github/workflows/unittests.yml   # CI/CD – runs on push to all task branches
├── .vscode/settings.json
├── .gitignore
├── requirements.txt
├── README.md
├── data/
│   └── raw/
│       ├── raw_analyst_ratings.csv   # FNSPID news dataset
│       ├── AAPL.csv                  # Historical prices from yFinance
│       ├── AMZN.csv
│       ├── GOOG.csv
│       ├── META.csv
│       └── NVDA.csv
├── notebooks/
│   ├── task_1_eda.ipynb              # EDA: headline stats, publishers, keywords
│   ├── task2_technical_analysis.ipynb# Technical indicators: SMA, EMA, RSI, MACD
│   └── task_3_sentiment_correlation.ipynb  # Sentiment → return correlation
├── src/
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_sentiment_utils.py       # Unit tests for sentiment helpers
└── scripts/
    └── __init__.py
```

---

## Dataset

### Financial News (FNSPID) — `raw_analyst_ratings.csv`
| Field | Description |
|-------|-------------|
| headline | Article title (key financial actions, price targets, ratings) |
| url | Link to the full news article |
| publisher | Author or news source |
| date | Publication timestamp with UTC-4 offset |
| stock | Stock ticker (e.g., `AAPL`) |

### Historical Stock Prices — `{SYMBOL}.csv`
Sourced via the **yFinance** Python library for AAPL, AMZN, GOOG, META, NVDA.

| Field | Description |
|-------|-------------|
| Date | Trading day (non-trading days excluded) |
| Open / High / Low / Close | OHLC prices |
| Adj Close | Adjusted closing price (for return calculations) |
| Volume | Total shares traded |

---

## Setup

```bash
# 1. Clone the repository
git clone https://github.com/Simbogj/news-sentiment-analysis.git
cd news-sentiment-analysis

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Tasks

### Task 1 – Exploratory Data Analysis (`task_1_eda.ipynb`)
Branch: `task-1`

- Headline length distribution
- Publisher activity ranking & domain analysis
- Daily news volume time-series with spike identification
- Publishing-hour pattern analysis
- TF-IDF keyword extraction and visualisation

### Task 2 – Technical Indicators (`task2_technical_analysis.ipynb`)
Branch: `task-2`

- Load and validate OHLCV data for all 5 stocks
- Compute via **TA-Lib**: SMA-20, SMA-50, EMA-20, RSI-14, MACD (12/26/9)
- Daily return distribution and time-series per stock
- Multi-stock closing price comparison

### Task 3 – Sentiment × Return Correlation (`task_3_sentiment_correlation.ipynb`)
Branch: `task-3`

- Filter news to the 5 target stocks (AAPL, AMZN, GOOG, META, NVDA)
- Align publication dates to next valid trading day
- Apply **VADER** sentiment analysis → compound score per headline
- Compute daily percentage returns from closing prices
- Average daily sentiment per stock, merge with returns
- Pearson correlation coefficient + scatter plot
- Average return by sentiment category (Positive / Neutral / Negative) bar chart
- Written interpretation including limitations

---

## Running Tests

```bash
pytest tests/ -v
```

---

## Technologies

| Purpose | Library |
|---------|---------|
| Data manipulation | pandas, numpy |
| Visualisation | matplotlib, seaborn |
| Technical indicators | TA-Lib, PyNance |
| NLP / Sentiment | VADER (vaderSentiment), NLTK, scikit-learn (TF-IDF) |
| Statistics | scipy |
| Testing | pytest |
| CI/CD | GitHub Actions |

---

## Author

**Simbo Getachew**