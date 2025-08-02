def generate_passwords(base_words, numbers):
    for word in base_words:
        for num in numbers:
            print(f"{word}{num}")
            print(f"{word}@{num}")
            print(f"{word.capitalize()}{num}")

if __name__ == "__main__":
    base_words = ["admin", "user", "test", "password"]
    numbers = ["123", "2024", "007"]
    generate_passwords(base_words, numbers)
