"""Модульные тесты для чистой логики калькулятора (pytest)."""
import pytest

from calculator import calculate_income, parse_positive_number


class TestCalculateIncome:
    def test_full_year(self):
        # 100000 * 10% * 365 / 365 = 10000
        assert calculate_income(100000, 10, 365) == pytest.approx(10000)

    def test_partial_year(self):
        assert calculate_income(100000, 10, 180) == pytest.approx(100000 * 10 / 100 * 180 / 365)

    def test_small_numbers(self):
        assert calculate_income(1000, 5, 30) == pytest.approx(1000 * 5 / 100 * 30 / 365)

    @pytest.mark.parametrize("s,p,d", [
        (0, 10, 365),
        (100000, 0, 365),
        (100000, 10, 0),
        (-5, 10, 365),
    ])
    def test_non_positive_raises(self, s, p, d):
        with pytest.raises(ValueError):
            calculate_income(s, p, d)


class TestParsePositiveNumber:
    def test_integer_string(self):
        assert parse_positive_number("100") == 100.0

    def test_float_string(self):
        assert parse_positive_number("12.5") == 12.5

    def test_zero_raises(self):
        with pytest.raises(ValueError):
            parse_positive_number("0")

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            parse_positive_number("-3")

    def test_non_numeric_raises(self):
        with pytest.raises(ValueError):
            parse_positive_number("abc")

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            parse_positive_number("")