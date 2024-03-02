grade = float(input())
grades = lambda x: (
    "Fail" if 2 <= x <= 2.99 else
    "Poor" if 3 <= x <= 3.49 else
    "Good" if 3.50 <= x <= 4.49 else
    "Very Good" if 4.50 <= x <= 5.49 else
    "Excellent" if 5.50 <= x <= 6 else
    "Invalid"
)

print(grades(grade))