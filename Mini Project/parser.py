class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None

    def eat(self, token_type):
        if self.current_token is None or self.current_token.type != token_type:
            raise ParserError(f"Expected token {token_type}, got {self.current_token.type if self.current_token else 'None'}")
        self.next_token()

    def parse(self):
        return self.program()

    def program(self):
        nodes = []
        while self.current_token is not None:
            if self.current_token.type == 'FUNCTION':
                nodes.append(self.function_definition())
            else:
                nodes.append(self.statement())
        return ASTNode('program', children=nodes)

    def function_definition(self):
        self.eat('FUNCTION')
        func_name = self.current_token.value
        self.eat('ID')
        self.eat('OPAREN')
        params = self.parameters()
        self.eat('CPAREN')
        self.eat('OBRACE')
        body = self.block()
        self.eat('CBRACE')
        return ASTNode('function_definition', value=func_name, children=[params, body])

    def parameters(self):
        params = []
        while self.current_token and self.current_token.type == 'ID':
            params.append(ASTNode('parameter', value=self.current_token.value))
            self.eat('ID')
            if self.current_token.type == 'COMMA':
                self.eat('COMMA')
        return params

    def block(self):
        statements = []
        while self.current_token and self.current_token.type != 'CBRACE':
            statements.append(self.statement())
        return ASTNode('block', children=statements)

    def statement(self):
        if self.current_token.type == 'IF':
            return self.if_statement()
        elif self.current_token.type == 'FOR':
            return self.for_statement()
        if self.current_token.type == 'ID':
            if self.peek() == 'ASSIGN':
                return self.assignment_statement()
            elif self.peek() == 'OPAREN':
                return self.function_call()
            else:
                raise ParserError(f"Unrecognized statement starting with ID: {self.current_token.value}")
        elif self.current_token.type == 'PRINT':
            return self.print_statement()
        else:
            raise ParserError("Invalid statement")

    def assignment_statement(self):
        var_name = self.current_token.value
        self.eat('ID')
        self.eat('ASSIGN')
        value = self.expression()
        self.eat('END')
        return ASTNode('assignment_statement', value=var_name, children=[value])

    def function_call(self):
        func_name = self.current_token.value
        self.eat('ID')
        self.eat('OPAREN')
        args = self.arguments()
        self.eat('CPAREN')
        self.eat('END')
        return ASTNode('function_call', value=func_name, children=args)

    def arguments(self):
        args = []
        while self.current_token and self.current_token.type != 'CPAREN':
            args.append(self.expression())
            if self.current_token.type == 'COMMA':
                self.eat('COMMA')
        return args

    def print_statement(self):
        self.eat('PRINT')
        expressions = []
        expressions.append(self.expression())
        self.eat('END')
        return ASTNode('print_statement', children=expressions)


    def if_statement(self):
        self.eat('IF')
        self.eat('OPAREN')
        condition = self.comparison()
        self.eat('CPAREN')
        self.eat('OBRACE')
        true_block = self.block()
        self.eat('CBRACE')

        false_block = None
        if self.current_token and self.current_token.type == 'ELSE':
            self.eat('ELSE')
            self.eat('OBRACE')
            false_block = self.block()
            self.eat('CBRACE')

        return ASTNode('if_statement', children=[condition, true_block, false_block])

    def for_statement(self):
        self.eat('FOR')
        self.eat('OPAREN')
        # Optional initialization part
        init = self.assignment_statement() if self.current_token.type == 'ID' else None
        self.eat('END')
        # Condition part
        condition = self.expression()
        self.eat('END')
        # Optional increment part
        increment = self.assignment_statement() if self.current_token.type == 'ID' else None
        self.eat('CPAREN')
        self.eat('OBRACE')
        body = self.block()
        self.eat('CBRACE')

        return ASTNode('for_statement', children=[init, condition, increment, body])


    def expression(self):
      node = self.term()

      # Handle additional terms separated by PLUS
      while self.current_token and self.current_token.type == 'PLUS':
          self.eat('PLUS')
          right = self.term()
          node = ASTNode('add', children=[node, right])

      # Handle additional terms separated by MINUS
      while self.current_token and self.current_token.type == 'MINUS':
          self.eat('MINUS')
          right = self.term()
          node = ASTNode('subtract', children=[node, right])
      # Handle additional terms separated by MULTIPLY
      while self.current_token and self.current_token.type == 'MULTIPLY':
          self.eat('MULTIPLY')
          right = self.term()
          node = ASTNode('multiply', children=[node, right])

      # Handle additional terms separated by DIVIDE
      while self.current_token and self.current_token.type == 'DIVIDE':
          self.eat('DIVIDE')
          right = self.term()
          node = ASTNode('divide', children=[node, right])

      return node

    def comparison(self):
      node = self.term()

      # handle comparison operators like LESS, GREATER, LESSEQUAL, GREATEREQUAL, EQUAL, NOTEQUAL, etc.
      # Example for handling one comparison operator:
      while self.current_token and self.current_token.type == 'LESS':
          self.eat('LESS')
          right = self.term()
          node = ASTNode('less_than', children=[node, right])
      while self.current_token and self.current_token.type == 'GREATER':
          self.eat('GREATER')
          right = self.term()
          node = ASTNode('greater_than', children=[node, right])
      while self.current_token and self.current_token.type == 'EQUAL':
          self.eat('EQUAL')
          right = self.term()
          node = ASTNode('equal', children=[node, right])
      while self.current_token and self.current_token.type == 'NOTEQUAL':
          self.eat('NOTEQUAL')
          right = self.term()
          node = ASTNode('not_equal', children=[node, right])

      return node
    
    def term(self):
        # A term is either a number, a string, or an identifier
        token = self.current_token
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return ASTNode('number', value=token.value)
        elif token.type == 'STRING':
            self.eat('STRING')
            return ASTNode('string', value=token.value)
        elif token.type == 'ID':
            self.eat('ID')
            return ASTNode('identifier', value=token.value)
        else:
            raise ParserError(f"Invalid term: Unexpected token {token.type} with value '{token.value}'")
    def peek(self):
        return self.tokens[0].type if self.tokens else None