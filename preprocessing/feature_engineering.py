def select_features(data):

    features = [
        "sleep_hours",
        "study_hours",
        "screen_time",
        "stress_level",
        "workload",
        "exercise_hours",
        "caffeine_intake",
        "break_frequency",
        "assignment_pressure"
    ]

    X = data[features]
    y = data["fatigue_level"]

    return X, y