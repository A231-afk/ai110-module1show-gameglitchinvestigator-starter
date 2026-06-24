from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome is "Too High" and hint says go LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome is "Too Low" and hint says go HIGHER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()

def test_guess_far_too_low():
    # check_guess(9, 80) should be "Too Low"
    outcome, message = check_guess(9, 80)
    assert outcome == "Too Low"

def test_guess_far_too_high():
    # check_guess(100, 99) should be "Too High"
    outcome, message = check_guess(100, 99)
    assert outcome == "Too High"

def test_exact_match_wins():
    # check_guess(42, 42) should be "Win"
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"


# FIX: Claude helped refactor parse_guess/update_score into logic_utils.py;
# these tests verify the input-parsing and incorrect-score repairs.

def test_parse_whole_number_string():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_blank_rejected():
    ok, value, err = parse_guess("")
    assert ok is False
    assert err == "Enter a guess."

def test_parse_whitespace_rejected():
    ok, value, err = parse_guess("   ")
    assert ok is False
    assert err == "Enter a guess."

def test_parse_nonnumeric_rejected():
    ok, value, err = parse_guess("hello")
    assert ok is False
    assert value is None

def test_parse_decimal_rejected():
    ok, value, err = parse_guess("5.9")
    assert ok is False
    assert value is None

def test_too_high_subtracts_five():
    # Must subtract regardless of attempt number (old bug added on even attempts).
    assert update_score(100, "Too High", 2) == 95
    assert update_score(100, "Too High", 3) == 95

def test_too_low_subtracts_five():
    assert update_score(100, "Too Low", 2) == 95
    assert update_score(100, "Too Low", 3) == 95


# FIX: Claude helped move get_range_for_difficulty into logic_utils.py; these tests
# verify the difficulty ranges.

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 50)
