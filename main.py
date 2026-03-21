from utils.data_loader import load_dataset
from preprocessing.data_cleaning import clean_data
from preprocessing.feature_engineering import select_features
from ml_models.train_model import train_model
from ml_models.predict_model import load_model, predict_fatigue
from nlp_module.sentiment_analysis import analyze_sentiment
from fuzzy_engine.fuzzy_model import calculate_fatigue_score


def main():

    # Load dataset
    data = load_dataset()

    # Clean dataset
    clean_dataset = clean_data(data)

    # Feature selection
    X, y = select_features(clean_dataset)

    # Train ML model
    train_model(X, y)

    # Load saved model
    model = load_model()

    # Sample student input
    sample_student = [
        5,  # sleep_hours
        8,  # study_hours
        7,  # screen_time
        8,  # stress_level
        9,  # workload
        0,  # exercise_hours
        3,  # caffeine_intake
        1,  # break_frequency
        9   # assignment_pressure
    ]

    # ML prediction
    prediction = predict_fatigue(model, sample_student)

    print("\nML Predicted Fatigue Level:", prediction)

    # Fuzzy logic inputs
    sleep_hours = sample_student[0]
    study_hours = sample_student[1]
    stress_level = sample_student[3]

    # Fuzzy fatigue calculation
    score, level = calculate_fatigue_score(
        sleep_hours,
        stress_level,
        study_hours
    )

    print("Fuzzy Fatigue Score:", score)
    print("Fuzzy Fatigue Level:", level)

    # NLP feedback analysis
    feedback = "I feel very stressed due to exams"

    sentiment = analyze_sentiment(feedback)

    print("Feedback Sentiment:", sentiment)


if __name__ == "__main__":
    main()
    can 9 