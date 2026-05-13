"""
Unit tests for the sentiment & date-alignment utilities used in Task 3.
"""

import datetime
import pytest


# ---------------------------------------------------------------------------
# Helpers (mirrors the notebook logic so tests can run without notebook deps)
# ---------------------------------------------------------------------------

def classify_sentiment(score):
    """Classify a VADER compound score into Positive / Neutral / Negative."""
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    return "Neutral"


def next_trading_day(d, trading_days_set):
    """Advance date d until it lands on a known trading day."""
    while d not in trading_days_set:
        d += datetime.timedelta(days=1)
    return d


# ---------------------------------------------------------------------------
# Tests: classify_sentiment
# ---------------------------------------------------------------------------

class TestClassifySentiment:
    def test_positive(self):
        assert classify_sentiment(0.5) == "Positive"

    def test_positive_boundary(self):
        assert classify_sentiment(0.051) == "Positive"

    def test_neutral_upper(self):
        assert classify_sentiment(0.05) == "Neutral"

    def test_neutral_lower(self):
        assert classify_sentiment(-0.05) == "Neutral"

    def test_neutral_zero(self):
        assert classify_sentiment(0.0) == "Neutral"

    def test_negative(self):
        assert classify_sentiment(-0.5) == "Negative"

    def test_negative_boundary(self):
        assert classify_sentiment(-0.051) == "Negative"


# ---------------------------------------------------------------------------
# Tests: next_trading_day
# ---------------------------------------------------------------------------

MOCK_TRADING_DAYS = {
    datetime.date(2020, 6, 1),  # Monday
    datetime.date(2020, 6, 2),  # Tuesday
    datetime.date(2020, 6, 3),  # Wednesday
    datetime.date(2020, 6, 4),  # Thursday
    datetime.date(2020, 6, 5),  # Friday
    # Weekend (6, 7) intentionally missing
    datetime.date(2020, 6, 8),  # Monday following
}


class TestNextTradingDay:
    def test_already_trading_day(self):
        d = datetime.date(2020, 6, 1)
        assert next_trading_day(d, MOCK_TRADING_DAYS) == d

    def test_saturday_maps_to_monday(self):
        saturday = datetime.date(2020, 6, 6)
        expected = datetime.date(2020, 6, 8)
        assert next_trading_day(saturday, MOCK_TRADING_DAYS) == expected

    def test_sunday_maps_to_monday(self):
        sunday = datetime.date(2020, 6, 7)
        expected = datetime.date(2020, 6, 8)
        assert next_trading_day(sunday, MOCK_TRADING_DAYS) == expected

    def test_friday_stays_friday(self):
        friday = datetime.date(2020, 6, 5)
        assert next_trading_day(friday, MOCK_TRADING_DAYS) == friday
