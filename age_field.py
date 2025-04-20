def validate_age(age: int) -> bool:
    if not isinstance(age, int):
        raise ValueError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 122:
        raise ValueError("Age seems unrealistic.")
    return True

def get_age(question: str = "Age:") -> int:
    prompt: str = question.strip() + " "
    while True:
        try:
            age = int(input(prompt))
            validate_age(age)
            return age
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a number between 0 and 122.")
