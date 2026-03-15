DIFFICULTY_CONFIG = {
    "Easy":   {"min_num": 1, "max_num": 20,  "max_attempts": 6},
    "Normal": {"min_num": 1, "max_num": 100, "max_attempts": 8},
    "Hard":   {"min_num": 1, "max_num": 50,  "max_attempts": 5},
}


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int = None, high: int = None):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    if "." in raw:
        return False, None, "Enter a whole number, not a decimal."

    try:
        value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if low is not None and high is not None:
        if value < low or value > high:
            return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return outcome: "Win", "Too High", or "Too Low".
    """
    if guess == secret:
        return "Win"

    try:
        if guess > secret:
            return "Too High"
        else:
            return "Too Low"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win"
        if g > secret:
            return "Too High"
        return "Too Low"


def get_hint_message(outcome: str) -> str:
    """Return the emoji hint message for a given outcome."""
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    return "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
