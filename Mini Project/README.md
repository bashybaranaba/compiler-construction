# Swahili Programming Language Compiler

## Overview
This project presents a compiler for a custom programming language that uses Swahili-based syntax. It is designed as a mini project for educational purposes. The compiler includes a lexer, parser, and interpreter for executing programs written in this language.

## Features

- **Lexical Analysis:** Tokenization of source code written in Swahili-like syntax.
- **Parsing:** Transformation of tokens into an Abstract Syntax Tree (AST).
- **Interpretation:** Execution of the AST to produce program output.

## Getting Started

### Prerequisites
Ensure you have Python installed on your system to run the compiler.

### Installation
Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```
Navigate to the project directory:

 ```bash
cd <project-directory-name>
 ```

## Usage

Write your source code in a text file with a `.sw` extension. Then, run the compiler with the following command:

 ```bash
python compiler.py path_to_your_file.sw
 ```

The compiler will tokenize, parse, and interpret the Swahili-syntax code.

## Language Syntax Guide

### Variables
Declare variables with identifiers:

 ```sw
moja = 1;
mbili = 2;
neno = "neno";
 ```

### Functions
Create functions using the `kazi` keyword:

 ```sw
kazi myFunction(x, y) {
    andika "hello";
}
 ```

### Print Statements
Output text to the console with `andika`:

 ```sw
andika "Jambo Dunia!";
 ```

### Arithmetic Operations
Perform basic arithmetic operations:

 ```sw
jumla = moja + mbili;
 ```

### Comments
Currently, comments are not supported in this language version.

## Example Program

Here's a sample program that adds two numbers and prints the result:

 ```sw
kazi jumuisha(x, y) {
  jibu = x + y;
  andika jibu;
}

jumuisha(1, 2);
 ```

## Contributing

Contributions to this project are welcome. Please fork the repository, add your contribution, and submit a pull request.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE.md) file for details.
