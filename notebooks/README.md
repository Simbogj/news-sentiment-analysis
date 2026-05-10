# Financial News Sentiment Analysis - Task 1: Exploratory Data Analysis

## Overview

This project analyzes the relationship between financial news sentiment and stock market movements. Task 1 focuses on exploratory data analysis (EDA) of financial news headlines to understand patterns, trends, and characteristics of the dataset.

## Objective

Conduct comprehensive EDA on financial news data to:
- Analyze headline characteristics and distributions
- Identify key publishers and their activity patterns
- Examine publication timing and volume trends
- Extract common keywords and topics from headlines
- Establish baseline insights for subsequent sentiment and correlation analysis

## Dataset

The dataset contains financial news headlines with the following structure:

| Field     | Description                          |
|-----------|--------------------------------------|
| headline  | News article headline text          |
| url       | Direct link to the full article     |
| publisher | News source or author               |
| date      | Publication date and time (UTC-4)   |
| stock     | Associated stock ticker symbol      |

## Project Structure

```
news-sentiment-analysis/
├── .github/workflows/unittests.yml    # CI/CD pipeline
├── data/raw/                          # Raw dataset files
├── notebooks/task_1_eda.ipynb         # EDA analysis notebook
├── src/                               # Source code modules
├── tests/                             # Unit tests
├── scripts/                           # Utility scripts
├── requirements.txt                   # Python dependencies
└── README.md                       
```

## Technologies

- **Language**: Python 3.11
- **Core Libraries**: pandas, numpy, matplotlib, seaborn
- **NLP Tools**: scikit-learn, NLTK
- **Development**: Jupyter Notebook, Git, GitHub Actions

## Setup Instructions

1. **Clone Repository**
   ```bash
   git clone https://github.com/Simbogj/news-sentiment-analysis.git
   cd news-sentiment-analysis
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Analysis Performed

### 1. Data Quality Assessment
- Verified dataset structure and data types
- Checked for missing values and duplicates
- Validated date parsing and timezone handling

### 2. Headline Analysis
- Computed character and word count distributions
- Identified average headline lengths
- Analyzed text complexity patterns

### 3. Publisher Analysis
- Ranked publishers by article volume
- Examined contribution patterns
- Identified domain-based groupings

### 4. Temporal Analysis
- Analyzed daily publication volume trends
- Identified peak publishing hours
- Detected news volume spikes

### 5. Content Analysis
- Extracted top keywords using TF-IDF
- Generated n-gram frequency analysis
- Identified recurring financial themes

## Key Findings

- Headline lengths follow a normal distribution (mean: ~80 characters)
- Top publishers account for majority of news volume
- News volume peaks during market hours (9 AM - 4 PM EST)
- Common themes: earnings, guidance, analyst ratings, mergers

## Visualizations

- Headline length histograms
- Publisher activity bar charts
- Daily volume time series
- Hourly publication patterns
- Keyword frequency plots

## Development Workflow

- **Branch**: `task-1` for development
- **CI/CD**: Automated testing on push/PR via GitHub Actions
- **Testing**: Unit tests in `tests/` directory
- **Commits**: Conventional commit messages


## Author

Simbo Getachew