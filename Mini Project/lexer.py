import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

def lex(source_code):
    # Tokens are defined as pairs of (regex, type)
    token_specification = [
        ('STRING', r'\".*?\"'),        # String
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r'='),            # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z_]\w*'), # Identifiers
        ('OPAREN',   r'\('),           # Open parenthesis
        ('CPAREN',   r'\)'),           # Close parenthesis
        ('OBRACE',   r'\{'),           # Open brace
        ('CBRACE',   r'\}'),           # Close brace
        ('COMMA',    r','),            # Comma
        ('PLUS',     r'\+'),           # Plus operator
        ('MINUS',    r'-'),            # Minus operator
        ('MULTIPLY', r'\*'),           # Multiply operator
        ('DIVIDE',   r'/'),            # Divide operator
        ('EQUAL',    r'@'),            # Equal operator
        ('NOTEQUAL', r'!'),            # Not equal operator
        ('LESS',     r'<'),             # Less than operator
        ('GREATER',  r'>'),             # Greater than operator
        ('AND',      r'&'),            # Logical AND
        ('OR',       r'\|\|'),          # Logical OR
        ('NOT',      r'!'),             # Logical NOT
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]

    # Keywords and their corresponding types
    keywords = {
        'andika': 'PRINT',
        'kama': 'IF',
        'lasivyo': 'ELSE',
        'vunja': 'BREAK',
        'endelee': 'CONTINUE',
        'kwa': 'FOR',
        'wakati': 'WHILE',
        'kazi': 'FUNCTION',
        'rudisha': 'RETURN',
    }

    # Regex patterns
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    line_num = 1
    line_start = 0
    tokens = []

    for mo in re.finditer(token_regex, source_code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start

        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = keywords[value]
        elif kind == 'STRING':
            value = value.strip('"')
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')

        token = Token(kind, value)
        tokens.append(token)

    return tokens