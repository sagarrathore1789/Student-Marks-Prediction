import pandas as pd
import numpy as np

np.random.seed(42)
n = 200

study_hours = np.round(np.random.uniform(1, 10, n), 1)
attendance = np.clip(np.random.normal(75, 12, n), 40, 100).round(0)
previous_marks = np.clip(np.random.normal(60, 15, n), 20, 100).round(0)
assignment_scores = np.clip(np.random.normal(65, 15, n), 25, 100).round(0)

final_marks = (
    0.35 * previous_marks +
    0.25 * assignment_scores +
    0.20 * attendance +
    0.20 * (study_hours * 10) +
    np.random.normal(0, 4, n)
)
final_marks = np.clip(final_marks, 0, 100).round(0)

df = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "previous_marks": previous_marks,
    "assignment_scores": assignment_scores,
    "final_marks": final_marks
})

df.to_csv("dataset/student_data.csv", index=False)
print(f"Created {len(df)} rows → dataset/student_data.csv")
print(df.head())