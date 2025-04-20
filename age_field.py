def validate_age(age: int) -> bool:
    if not isinstance(age, int):
        raise ValueError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 122:
        raise ValueError("Age seems unrealistic.")
    return True
