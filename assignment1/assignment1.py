# Task 1: Hello
def hello():
    return "Hello!"
print(hello())

# Task 2: Greet with a Formatted String 
def greet(name):
    return f"Hello, {name}!"
print(greet("Name"))  # Output: Hello, Name!

# Task 3: Calculator
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return f"Unknown operation: {operation}"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

# Task 4: Data Type Conversion
def data_type_conversion(value, type):
    try:
        if type == "float":
            return float(value)
        elif type == "str":
            return str(value)
        elif type == "int":
            return int(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type}."
# Task 5: Grading System Using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."
#    Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result
#    Task 7: Student Scores Using **kwargs
def student_scores(operation, **kwargs):
    if operation == "best":
        return max(kwargs, key=kwargs.get)
    elif operation == "mean":
        return sum(kwargs.values()) / len(kwargs)
#    Task 8: Titleize, with String and List Operations
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()

    return " ".join(words)
#    Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result
#    Task 10: Pig Latin
def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            index = 0

            while index < len(word) and word[index] not in vowels:
                if word[index:index + 2] == "qu":
                    index += 2
                    break
                index += 1

            result.append(word[index:] + word[:index] + "ay")

    return " ".join(result)
print(pig_latin("apple"))
# appleay

print(pig_latin("hello"))
# ellohay

print(pig_latin("string"))
# ingstray

print(pig_latin("queen"))
# eenquay

print(pig_latin("quick"))
# ickquay

print(pig_latin("hello apple"))
# ellohay appleay

