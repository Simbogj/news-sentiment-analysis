# Financial News Sentiment Analysis

## Project Overview

This project analyzes the relationship between financial news sentiment and stock market movements. The goal is to determine whether news headlines can help predict stock price changes by combining Natural Language Processing (NLP), Exploratory Data Analysis (EDA), technical analysis indicators, and statistical correlation methods.

# Task 1 — Exploratory Data Analysis (EDA)

## Objective

The objective of Task 1 is to:

- Set up a professional data science project environment
- Configure GitHub version control and CI/CD workflow
- Explore the financial news dataset
- Identify trends, patterns, and anomalies
- Analyze publishers, headline characteristics, and publication behavior
- Extract common keywords and topics from news headlines

---

# Project Structure

news-sentiment-analysis/
│
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── data/
│   └── raw/
│
├── notebooks/
│   └── task1_eda.ipynb
│
├── src/
│
├── tests/
│
├── scripts/
│
├── requirements.txt
├── README.md
└── .gitignore


---

# Dataset Description

The dataset contains financial news headlines and metadata.

| Column    | Description               |
| --------- | ------------------------- |
| headline  | News article headline     |
| url       | Link to article           |
| publisher | News source or author     |
| date      | Publication date and time |
| stock     | Stock ticker symbol       |

---

# Technologies Used

## Programming Language

* Python

## Libraries

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* nltk

## Tools

* Jupyter Notebook
* Git & GitHub
* GitHub Actions (CI/CD)
* VS Code

---

# Environment Setup

## Clone Repository

git clone https://github.com/Simbogj/news-sentiment-analysis.git
cd news-sentiment-analysis


## Create Virtual Environment for Windows

python -m venv venv
venv\Scripts\activate

## Install Dependencies


pip install -r requirements.txt
---

# Exploratory Data Analysis Performed

## 1. Data Inspection

* Checked dataset structure
* Verified data types

## 2. Headline Analysis

* Calculated headline lengths
* Analyzed headline length distribution

## 3. Publisher Analysis

* Identified most active publishers
* Compared article contribution frequency

## 4. Time Series Analysis

* Analyzed article publication frequency over time
* Identified spikes in news activity
* Examined publishing hours

## 5. Keyword & Topic Analysis

* Extracted important keywords using TF-IDF
* Generated keyword frequency visualizations
* Created a word cloud for headline text

---

# Visualizations Included

* Headline Length Distribution
* Top Publishers Bar Chart
* Daily News Volume Trend
* Publishing Hours Distribution
* Top Keywords Visualization


---


# CI/CD Configuration

GitHub Actions workflow was configured to:

* Automatically install dependencies
* Run tests on push and pull requests
* Ensure project reproducibility

Workflow file:

.github/workflows/unittests.yml


---

# Branching Strategy

| Branch | Purpose                |
| ------ | ---------------------- |
| main   | Stable project version |
| task-1 | Task 1 development     |

---

# Author

Simbo Getachew

---

