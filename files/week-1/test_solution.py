"""Checks for the Week 1 unit converter.

The script is run like a user would run it: the tests type the answers in
(standard input) and read what it printed (standard output).

By default the model answer (solution.py) is tested. To test your own work:
    CONVERTER_SCRIPT=starter.py python -m pytest weeks/week-1/practice
"""

import os
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).parent
SCRIPT = HERE / os.environ.get("CONVERTER_SCRIPT", "solution.py")


def run_converter(kilometres, celsius):
    result = subprocess.run(
        [sys.executable, "-I", str(SCRIPT)],
        input=f"{kilometres}\n{celsius}\n",
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


@pytest.mark.parametrize(
    "km, c, miles_line, f_line",
    [
        ("10", "25", "10.0 km is 6.21 miles", "25.0 C is 77.0 F"),
        ("0", "0", "0.0 km is 0.0 miles", "0.0 C is 32.0 F"),
        ("42.195", "100", "42.195 km is 26.22 miles", "100.0 C is 212.0 F"),
        ("5", "-40", "5.0 km is 3.11 miles", "-40.0 C is -40.0 F"),
        ("1", "37", "1.0 km is 0.62 miles", "37.0 C is 98.6 F"),
    ],
)
def test_conversions(km, c, miles_line, f_line):
    out = run_converter(km, c)
    assert miles_line in out
    assert f_line in out


def test_asks_for_both_values():
    out = run_converter("1", "1")
    assert "kilometres" in out
    assert "Celsius" in out
