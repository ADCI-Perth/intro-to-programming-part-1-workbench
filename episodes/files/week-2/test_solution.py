"""Tests for the Week 2 phone-book task.

These tests run the script like a user would: they type answers into it
and check what it prints. By default they test solution.py. To test your
own work, set the PHONEBOOK_FILE variable, for example in PowerShell:

    $env:PHONEBOOK_FILE = "starter.py"
    python -m pytest weeks/week-2/practice
"""
import ast
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
SCRIPT = HERE / os.environ.get("PHONEBOOK_FILE", "solution.py")


def run(*answers):
    """Run the script, typing each answer on its own line. Return stdout lines."""
    result = subprocess.run(
        [sys.executable, "-I", str(SCRIPT)],
        input="\n".join(answers) + "\n",
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, result.stderr
    # Prompts have no newline, so a printed line may start after a prompt.
    # That is fine: the tests only look for text inside the output.
    return result.stdout.splitlines()


def test_lookup_existing_contact():
    out = "\n".join(run("Cara", "0411 000 111", "08 9111 2222", "Ben", "Amy"))
    assert "Ben: 0400 333 444, 08 9000 1111" in out


def test_lookup_new_contact_is_tidied_and_has_both_numbers():
    out = "\n".join(run("  cara jones ", "0411 000 111", "08 9111 2222", "CARA JONES", "Amy"))
    assert "Cara Jones: 0411 000 111, 08 9111 2222" in out


def test_lookup_missing_contact():
    out = "\n".join(run("Cara", "0411 000 111", "08 9111 2222", "Zoe", "Amy"))
    assert "Zoe: not found" in out


def test_remove_and_sorted_list():
    out = "\n".join(run("Cara", "0411 000 111", "08 9111 2222", "Ben", "Amy"))
    assert "Contacts (2): Ben, Cara" in out


def test_removing_missing_name_changes_nothing():
    out = "\n".join(run("Cara", "0411 000 111", "08 9111 2222", "Ben", "Nobody"))
    assert "Contacts (4): Amy, Ben, Cara" not in out
    assert "Contacts (3): Amy, Ben, Cara" in out


def test_names_are_sorted():
    out = "\n".join(run("Aaron", "1", "2", "Ben", "Zzz"))
    assert "Contacts (4): Aaron, Amy, Ben, Zzz" not in out
    assert "Contacts (3): Aaron, Amy, Ben" in out


def test_stretch_set_counts_distinct_numbers():
    # Cara gives Ben's mobile as her own, so only 3 different numbers exist.
    out = "\n".join(run("Cara", "0400 333 444", "08 9111 2222", "Ben", "Amy"))
    assert "Different numbers for Cara and Ben: 3" in out


def test_uses_only_week_2_ideas():
    """The solution must not use if, loops or functions (Week 3 topics)."""
    tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
    banned = (ast.If, ast.For, ast.While, ast.FunctionDef, ast.Lambda, ast.Try)
    found = [type(n).__name__ for n in ast.walk(tree) if isinstance(n, banned)]
    assert not found, f"Week 3 ideas found: {found}"
