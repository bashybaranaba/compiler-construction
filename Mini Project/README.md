# Swahili Programming Language Compiler

## Overview
This project presents a compiler for a custom programming language that uses Swahili-based syntax. It is designed as a mini project for educational purposes. The compiler includes a lexer, parser, and interpreter for executing programs written in this language, now with enhanced functionality for control structures and additional operators.

## Features

- **Lexical Analysis:** Tokenization of source code written in Swahili-like syntax.
- **Parsing:** Transformation of tokens into an Abstract Syntax Tree (AST).
- **Interpretation:** Execution of the AST to produce program output.
- **Control Structures:** Implementation of `kama` (if) and `lasivyo` (else) for conditional logic.
- **Extended Operators:** Introduction of operators for equality (`@`), inequality (`!`), and logical operations.

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

### Control Structures
Use `kama` and `lasivyo` for conditional logic:

 ```sw
kama(moja > mbili){
  andika "story za jaba";
}lasivyo{
  andika "all good";
}
 ```

### Arithmetic and Logical Operations
Perform arithmetic and logical operations:

 ```sw
# Arithmetic
jumla = moja + mbili;

# Equality Check
kama(moja @ mbili){
  andika "moja na mbili ni sawa";
}

# Logical AND
kama(moja < mbili & neno @ "neno"){
  andika "both conditions are true";
}
 ```

### Comments
Currently, comments are not supported in this language version.

## Example Program

This example program demonstrates variables, functions, print statements, and conditional logic:

 ```sw
kazi jumuisha(x, y) {
  jibu = x + y;
  andika jibu;
}

moja = 3;
mbili = 2;

neno = "Hello world";
andika neno;

jumuisha(moja, mbili);

kama(moja > mbili){
  andika "story za jaba";
}lasivyo{
  andika "all good";
}
 ```
