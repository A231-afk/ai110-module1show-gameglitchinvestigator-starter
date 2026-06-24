from logic_utils import check_guess

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
