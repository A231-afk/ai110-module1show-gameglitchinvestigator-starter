def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Claude helped refactor parse_guess out of app.py; pytest verified the repair.
    # Reject decimals ("5.9") and nonnumeric input ("hello") instead of silently
    # coercing via int(float(...)). Plain int() handles all three cases:
    #   "42" -> 42, "5.9" -> ValueError, "hello" -> ValueError.
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    return True, value, None


# FIX: Refactored with Claude and corrected the reversed hint directions; verified with pytest.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Both values are always numeric, so a plain numeric comparison is enough.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Claude helped refactor update_score out of app.py; pytest verified the repair.
    # A wrong guess must never increase the score, so both "Too High" and "Too Low"
    # subtract 5 (the old alternating "+5 on even attempts" path was the bug).
    # Win scoring formula preserved unchanged to keep this change focused.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
