from importlib import import_module

import pytest


Solution = import_module("algorithms.121_best_time_to_buy_and_sell_stock").Solution


@pytest.mark.parametrize(
    ("prices", "expected"),
    [
        pytest.param([7, 1, 5, 3, 6, 4], 5, id="example-one"),
        pytest.param([7, 6, 4, 3, 1], 0, id="prices-only-decrease"),
        pytest.param([1, 2], 1, id="buy-before-sell"),
        pytest.param([2, 4, 1], 2, id="best-profit-before-final-drop"),
        pytest.param([3, 3, 3], 0, id="repeated-prices"),
        pytest.param([5], 0, id="single-day"),
        pytest.param([], 0, id="no-days"),
    ],
)
def test_max_profit(prices, expected):
    assert Solution().maxProfit(prices) == expected
