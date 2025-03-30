# Excellenteam Coding Practices
This document is the de facto practice guideline standard; any deviation from the practices presented below is a valid reason for grade reduction.

## Python Best Practices
Following section presents general Python practices.

### Incorrect or Missing Use of `try/except`

✅ **Positive Example**:
```python
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
```

❌ **Not using try/except when needed**:
```python
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()  # Will raise an error if file does not exist
```

❌ **Using try/except in a wrong way**:
```python
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y  # This can raise ZeroDivisionError
    print("Result:", result)
except:
    print("Something went wrong!")  # Catches all exceptions, hiding the real issue
```

🔴 **What's wrong?**
- Broad `except` clause – hides actual exceptions.
- No specific handling for `ValueError`, `ZeroDivisionError`, etc.
- No helpful error message to the user.

### Input Verification

✅ **Only Validate at Input Handling**:
```python
def get_user_age():
    age = input("Enter your age: ")
    if not age.isdigit():
        raise ValueError("Age must be a valid positive integer.")
    return int(age)
```

💡 **Why is this better?**
- Validation is done early at input.
- Prevents invalid values from spreading in the program.
- Avoids repeated checks like `isinstance()` in all functions.

❌ **Over-validating everywhere**:
```python
def calculate_discount(price):
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number!")  # Overly strict!
    return price * 0.9
```

💡 **Why is this bad?**
- Prevents valid cases like `Decimal`.
- Adds unnecessary overhead.
- Prefer validating at input boundaries.

### Redundant Condition Checks

✅ **Positive Example**:
```python
if x > 10:
    print("Big number")
print("Small number")
```

❌ **Negative Example**:
```python
if x > 10:
    print("Big number")
elif x <= 10:  # Redundant check
    print("Small number")
```

### Edge Case Errors in Functions

✅ **Positive Example**:
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

❌ **Negative Example**:
```python
def divide(a, b):
    return a / b  # Doesn't handle division by zero
```

### Code Duplication

✅ **Positive Example**:
```python
def greet(time_of_day):
    print(f"Good {time_of_day}!")

greet("morning")
greet("evening")
```

❌ **Negative Example**:
```python
def greet_morning():
    print("Good morning!")

def greet_evening():
    print("Good evening!")
```

### Using Magic Numbers/Strings

✅ **Positive Example**:
```python
ADMIN = "admin"
ACCESS_LEVELS = {"admin": 3}

if user_type == ADMIN:
    access_level = ACCESS_LEVELS[ADMIN]
```

❌ **Negative Example**:
```python
if user_type == "admin":
    access_level = 3  # Magic string and number
```

### Non-Descriptive Variable Names

✅ **Positive Example**:
```python
max_users = 10
timeout_seconds = 20
```

❌ **Negative Example**:
```python
x = 10  # What is x?
y = 20  # What is y?
```

### Using Explicit Paths in Code

✅ **Positive Example** (using a relative path):
```python
import os

relative_path = "./myfile.txt"
full_path = os.path.abspath(relative_path)
print("Full path to the file:", full_path)
```

❌ **Negative Example**:
```python
file_path = "/home/user/data.txt"
```

### Functions Not Called in `main`

✅ **Positive Example**:
```python
def process_data():
    print("Processing data...")

if __name__ == "__main__":
    print("Program started")
    process_data()
```

❌ **Negative Example**:
```python
def process_data():
    print("Processing data...")

if __name__ == "__main__":
    print("Program started")  # Forgot to call process_data
```

### Missing `if __name__ == "__main__"`

✅ **Positive Example**:
```python
def main():
    print("Running program")

if __name__ == "__main__":
    main()
```

❌ **Negative Example**:
```python
def main():
    print("Running program")

main()  # Runs even when imported
```

### Using `for` Loop Unnecessarily Instead of `in`

✅ **Positive Example**:
```python
found = target in my_list
```

❌ **Negative Example**:
```python
found = False
for item in my_list:
    if item == target:
        found = True
```

### Not Using List Comprehension

✅ **Positive Example**:
```python
squared = [x * x for x in numbers]
```

❌ **Negative Example**:
```python
squared = []
for x in numbers:
    squared.append(x * x)
```

### Using `while True`

✅ **Positive Example**:
```python
while (data := input("Enter data: ")) != "exit":
    pass
```

❌ **Negative Example**:
```python
while True:
    data = input("Enter data: ")
    if data == "exit":
        break
```

### Removing Items While Iterating

✅ **Positive Example**:
```python
my_list = [item for item in my_list if item >= 0]
```

❌ **Negative Example**:
```python
for item in my_list:
    if item < 0:
        my_list.remove(item)  # Causes issues
```

### Improper Function Input Handling

✅ **Positive Example**:
```python
def greet(name: str):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    print(f"Hello {name}")
```

❌ **Negative Example**:
```python
def greet(name):
    print("Hello " + name)  # Assumes name is a string
```

### Unnecessary List Usage

✅ **Positive Example**:
```python
items = set(my_list)
```

❌ **Negative Example**:
```python
items = list(set(my_list))  # Unnecessary conversion
```

## Documentation
Following section presents general documentation practices.

### Insufficient or Incorrect Documentation Format

✅ **Positive Example**:
```python
def add(a: int, b: int) -> int:
    """
    Adds two numbers and returns the sum.

    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b
```

❌ **Negative Example**:
```python
def add(a, b):
    """This function adds."""
    return a + b  # Not detailed enough
```

### No Documentation

✅ **Positive Example**:
```python
def calculate_area(r: float) -> float:
    """Calculates the area of a circle given its radius."""
    return 3.14 * r * r
```

❌ **Negative Example**:
```python
def calculate_area(r):
    return 3.14 * r * r  # No explanation
```

## Naming Conventions
Following section presents general naming conventions.

### Constants Names

✅ Use `UPPERCASE_WITH_UNDERSCORES`
```python
MAX_USERS = 1000
PI = 3.14159
```

❌ Avoid lowercase or mixed case:
```python
maxUsers = 1000
MaxUsers = 1000
```

### Class Names

✅ Use `PascalCase`
```python
class UserProfile:
    pass
```

❌ Avoid:
- `snake_case`: `class user_profile:`
- `lowercase`: `class userprofile:`

### Variable and Function Names

✅ Use `snake_case`:
```python
def calculate_discount(price, discount_rate):
    return price * discount_rate
```

❌ Avoid:
- `camelCase`
- `PascalCase`
- Single-letter names unless standard in context

### Method & Attribute Names (Inside Classes)

✅ Use `snake_case`:
```python
class User:
    def get_full_name(self):
        return self.first_name + " " + self.last_name
```

❌ Avoid:
- `PascalCase`: `GetFullName`
- `camelCase`: `getFullName`

### Private and Protected Attributes & Methods

✅ Use underscore prefix:
```python
class User:
    def __init__(self):
        self._session_token = "abcd1234"
```

✅ Use double underscores for private:
```python
class User:
    def __init__(self):
        self.__password = "secret"
```

### Function and Keyword Arguments

✅ Use descriptive names:
```python
def send_email(recipient_email, subject, message_body):
    pass
```

✅ Use `*args`, `**kwargs`:
```python
def print_names(*args, **kwargs):
    pass
```

❌ Avoid unclear names like `data`, `value`, unless context is obvious.

### Module and Package Names

✅ Use all lowercase with underscores:
```python
import user_auth
import db_utils
```

❌ Avoid:
- `UserAuth`
- `utils.py` (too generic)

### Exception Naming

✅ Use `PascalCase` ending in `Error`:
```python
class AuthenticationError(Exception):
    pass
```

❌ Avoid:
- `AuthException`
- `AuthIssue`

### File Naming

✅ Use `snake_case`:
```
user_controller.py
database_handler.py
```

❌ Avoid:
- `UserController.py`
- `user controller.py`
- `UserController.py`

### Naming Loop Variables

✅ Use descriptive names:
```python
for user in users:
    print(user.name)
```

✅ Use `i`, `j`, `k` for simple counters:
```python
for i in range(10):
    print(i)
```

❌ Avoid generic names like `x`, `y`, `data` without context.

### Avoid Magic Numbers and Strings

✅ Use named constants:
```python
DISCOUNT_RATE = 0.1
MAX_RETRIES = 3

if retries < MAX_RETRIES:
    ...
```

❌ Avoid:
```python
if retries < 3:  # Bad
```
