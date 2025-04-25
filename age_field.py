AGE_WORD_DICT: dict[str, int] = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
     "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100
}

def error_message() -> None:
    raise ValueError("The age is misspelled or seems too high. Please check.")

def validate_age(age: int) -> bool:
    if not isinstance(age, int):
        raise ValueError("Please enter a whole number for age.")
    if age < 0:
        raise ValueError("Age cannot be negative. Please enter a valid age.")
    if age > 122:
        raise ValueError("That age seems too high. Please enter a realistic age (0-122).")
    return True

def get_age_from_words(age: str) -> int:
    age_words: list[str] = age.lower().split()
    if len(age_words) != 1:
        one_to_nine: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        number_list: list[int] = []
        if len(age_words) == 3:
            for word in age_words:
                if word not in AGE_WORD_DICT.keys():
                    error_message()
                number_list.append(AGE_WORD_DICT[word])

            if (number_list[0] == 100) and (number_list[1] % 10 == 0 and number_list[1] != 10) and (number_list[2] in one_to_nine):
                age = sum(number_list)
                validate_age(age)
                return age
            error_message()

        if len(age_words) == 2:
            for word in age_words:
                if word not in AGE_WORD_DICT.keys():
                    error_message()
                number_list.append(AGE_WORD_DICT[word])

            if (number_list[0] % 10 == 0 and number_list[0] != 10) and (number_list[1] in one_to_nine or number_list[1] in range(10, 90)):
                age = sum(number_list)
                validate_age(age)
                return age
            error_message()

        error_message()

    if age not in AGE_WORD_DICT.keys():
        error_message()
    age = AGE_WORD_DICT[age]
    return age

def get_age(question: str = "Age:") -> int:
    prompt: str = question.strip() + " "
    while True:
        try:
            age: str = str(input(prompt)).strip().lower()                
            if all(c.isalnum() or c.isspace() for c in age):
                if age.isdigit():
                    age = int(age)
                    validate_age(age)
                    return age
                if age and all(c.isalpha() or c.isspace() for c in age):
                    if get_age_from_words(age):
                        age = get_age_from_words(age)
                        return age
            validate_age(age)
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    print(get_age(" Your age: "))
