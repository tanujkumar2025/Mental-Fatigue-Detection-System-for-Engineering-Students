def clean_data(data):

    print("\nCleaning Dataset...\n")

    # Remove missing values
    data = data.dropna()

    # Convert fatigue labels
    fatigue_map = {
        "low":0,
        "medium":1,
        "high":2
    }

    data["fatigue_level"] = data["fatigue_level"].map(fatigue_map)

    print("Data Cleaned Successfully")

    return data