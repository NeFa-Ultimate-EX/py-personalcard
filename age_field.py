AGE_WORD_DICT: dict[str, int] = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
     "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100
}

def raise_age_error(message: str = "The age is misspelled or seems too high. Please check.") -> None:
    raise ValueError(message)

def validate_age(age: int) -> bool:
    if not isinstance(age, int):
        raise ValueError("Please enter a whole number for age.")
    if age < 0:
        raise ValueError("Age cannot be negative. Please enter a valid age.")
    if age > 122:
        raise ValueError("That age seems too high. Please enter a realistic age (0-122).")
    return True

def get_age_from_words(age_input: str) -> int:
    age_words: list[str] = age_input.lower().split()

    if len(age_words) != 1:
        units_only: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        number_list: list[int] = []

        if len(age_words) == 3:
            for word in age_words:
                if word not in AGE_WORD_DICT.keys():
                    raise_age_error()
                number_list.append(AGE_WORD_DICT[word])

            if (number_list[0] == 100) and (number_list[1] % 10 == 0 and number_list[1] != 10) and (number_list[2] in units_only):
                parsed_age = sum(number_list)
                validate_age(parsed_age)
                return parsed_age
            raise_age_error()

        if len(age_words) == 2:
            for word in age_words:
                if word not in AGE_WORD_DICT.keys():
                    raise_age_error()
                number_list.append(AGE_WORD_DICT[word])

            if (number_list[0] % 10 == 0 and number_list[0] != 10) and (number_list[1] in units_only):
                parsed_age = sum(number_list)
                validate_age(parsed_age)
                return parsed_age

            if (number_list[0] % 100 == 0) and (number_list[1] in range(10, 90)):
                parsed_age = sum(number_list)
                validate_age(parsed_age)
                return parsed_age

            raise_age_error()

        raise_age_error()

    if age_input not in AGE_WORD_DICT.keys():
        raise_age_error()

    return AGE_WORD_DICT[age_input]

def get_age(question: str = "Age:") -> int:
    prompt: str = question.strip() + " "

    while True:
        try:
            age_input: str = str(input(prompt)).strip().lower()
            age_input = age_input.replace(" and ", " ", 1).replace("-", " ", 1)
            age_input_list = age_input.split()

            if all(c.isalnum() or c.isspace() or c == "-" for c in age_input):
                if age_input.isdigit():
                    final_age = int(age_input)
                    validate_age(final_age)
                    return final_age

                if age_input and all(c.isalpha() or c.isspace() or c == "-" for c in age_input):
                    if (len(age_input_list) >= 2) and (age_input_list[0] == "one" and age_input_list[1] == "hundred"):
                        age_input = age_input.replace("one", " ", 1).strip()
                    parsed_age: str = get_age_from_words(age_input)
                    return parsed_age

            validate_age(age_input)
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    print(get_age(" Your age: "))
