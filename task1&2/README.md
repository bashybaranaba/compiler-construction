## Compiler Construction Task

### Task 1: Identify Lines as Comments or Not

#### i Logic Used

1. We define a function `is_comment` that checks if a given line starts with the `#` symbol, denoting it's a comment in Python.
2. We strip any leading or trailing white spaces from the line using the `strip()` method.
3. We use the `startswith()` method to check if the line starts with `#`.


#### ii Lexical and Syntax Analysis
In this simple implementation, we've used a form of lexical analysis to identify if the token (`#`) is present at the start of a given line. Lexical analysis is essential because it helps in identifying tokens in the given input string. Syntax analysis was not explicitly used in this specific logic, as we are only identifying comments based on the token, not analyzing the structure of the entire program.
