"""
Safe User Registration System
Episode 12 Challenge Solution
"""

from datetime import datetime


# ==========================
# Custom Exception
# ==========================
class AgeError(Exception):
    """Raised when age is outside the valid range."""
    pass


# ==========================
# Error Logging
# ==========================
def log_error(error_message):
    """Save errors with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("errors.log", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {error_message}\n")


# ==========================
# Validators
# ==========================
def validate_name(name):
    """
    Validate user name.

    Raises:
        ValueError: If name is empty.
    """
    if not name.strip():
        raise ValueError("Name cannot be empty.")

    return name.strip()


def validate_age(age):
    """
    Validate user age.

    Raises:
        AgeError: If age is not between 0 and 120.
    """
    if age < 0 or age > 120:
        raise AgeError("Age must be between 0 and 120.")

    return age


# ==========================
# Registration Function
# ==========================
def register_user(name, age):
    """
    Register a user safely.
    """

    try:
        valid_name = validate_name(name)
        valid_age = validate_age(age)

    except ValueError as e:
        log_error(f"ValueError: {e}")
        return f"Registration Failed: {e}"

    except AgeError as e:
        log_error(f"AgeError: {e}")
        return f"Registration Failed: {e}"

    except Exception as e:
        log_error(f"Unexpected Error: {e}")
        return f"Registration Failed: {e}"

    else:
        return (
            f"Registration Successful!\n"
            f"Name: {valid_name}\n"
            f"Age: {valid_age}"
        )

    finally:
        print("Registration attempt completed.")


# ==========================
# Test Cases (Challenge Inputs)
# ==========================
test_cases = [
    ("", 25),          # Empty name
    ("Ali", -5),       # Negative age
    ("Ali", 999),      # Age too high
    ("Ali", 25),       # Valid user
]


print("\n===== TESTING SAFE USER REGISTRATION =====\n")

for name, age in test_cases:
    print(f"Input -> Name: '{name}', Age: {age}")
    print(register_user(name, age))
    print("-" * 50)
