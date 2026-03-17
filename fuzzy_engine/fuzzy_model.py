def calculate_fatigue_score(sleep_hours, stress_level, study_hours):

    score = 0

    # Rule 1
    if sleep_hours < 5 and stress_level > 7:
        score += 0.8

    # Rule 2
    if study_hours > 8 and sleep_hours < 6:
        score += 0.7

    # Rule 3
    if stress_level > 6:
        score += 0.6

    # Rule 4
    if sleep_hours >= 7 and stress_level <= 4:
        score += 0.2

    # Limit score
    score = min(score, 1)

    # Convert score to fatigue level
    if score >= 0.7:
        level = "High Fatigue"

    elif score >= 0.4:
        level = "Medium Fatigue"

    else:
        level = "Low Fatigue"

    return score, level