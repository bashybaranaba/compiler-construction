class InterpreterError(Exception):
    pass

class Interpreter:
    def __init__(self):
        self.context = {}

    def interpret(self, node):
        method_name = 'interpret_' + node.type
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise InterpreterError(f"No interpret_{node.type} method")

    def interpret_program(self, node):
        result = None
        for child in node.children:
            result = self.interpret(child)
        return result

    def interpret_function_definition(self, node):
        self.context[node.value] = node
        # Assuming functions don't return a value upon definition
        return None

    def interpret_function_call(self, node):
        function_node = self.context.get(node.value)
        if not function_node:
            raise InterpreterError(f"Function {node.value} not defined")

        if len(function_node.children[0]) != len(node.children):
            raise InterpreterError(f"Function {node.value} takes {len(function_node.children[0])} arguments but {len(node.children)} were given")

        # Save the current context
        saved_context = self.context.copy()

        # Update the context with arguments
        for param, arg in zip(function_node.children[0], node.children):
            self.context[param.value] = self.interpret(arg)

        # Interpret the function body
        result = self.interpret(function_node.children[1])

        # Restore the original context
        self.context = saved_context

        return result

    def interpret_block(self, node):
        result = None
        for statement in node.children:
            result = self.interpret(statement)
        return result

    def interpret_print_statement(self, node):
        value = self.interpret(node.children[0])
        print(value)
        return value

    def interpret_assignment_statement(self, node):
        var_name = node.value
        value = self.interpret(node.children[0])
        self.context[var_name] = value
        return value

    def interpret_identifier(self, node):
        var_name = node.value
        if var_name not in self.context:
            raise InterpreterError(f"Undefined variable '{var_name}'")
        return self.context[var_name]

    def interpret_number(self, node):
        return node.value

    def interpret_parameter(self, node):
        # Parameters are handled during function calls, but if this method is called,
        # it suggests a parameter is being used as a standalone expression, which is an error.
        raise InterpreterError(f"Parameter {node.value} cannot be used as an expression")

    # Add methods for handling expressions, like addition, subtraction, etc.
    # Assuming you have node types 'add', 'subtract', 'multiply', 'divide'

    def interpret_string(self, node):
        return node.value.strip('"')

    def interpret_add(self, node):
        left_val = self.interpret(node.children[0])
        right_val = self.interpret(node.children[1])
        return left_val + right_val

    def interpret_subtract(self, node):
        left_val = self.interpret(node.children[0])
        right_val = self.interpret(node.children[1])
        return left_val - right_val

    def interpret_multiply(self, node):
        left_val = self.interpret(node.children[0])
        right_val = self.interpret(node.children[1])
        return left_val * right_val

    def interpret_divide(self, node):
        left_val = self.interpret(node.children[0])
        right_val = self.interpret(node.children[1])
        if right_val == 0:
            raise InterpreterError("Division by zero")
        return left_val / right_val


    def interpret_if_statement(self, node):
      condition = self.interpret(node.children[0])
      if condition:
          return self.interpret(node.children[1])  # true_block
      elif node.children[2] is not None:
          return self.interpret(node.children[2])  # false_block


    def interpret_less_than(self, node):
        left_val = self.interpret(node.children[0])
        right_val = self.interpret(node.children[1])
        return left_val < right_val

    def interpret_greater_than(self, node):
        left_val = self.interpret(node.children[0])
        right_val = self.interpret(node.children[1])
        return left_val > right_val

    def interpret_less_equal(self, node):
        left_val = self.interpret(node.children[0])
        right_val = self.interpret(node.children[1])
        return left_val <= right_val

    def interpret_greater_equal(self, node):
        left_val = self.interpret(node.children[0])
        right_val = self.interpret(node.children[1])
        return left_val >= right_val

    def interpret_equal(self, node):
        left_val = self.interpret(node.children[0])
        right_val = self.interpret(node.children[1])
        return left_val == right_val

    def interpret_not_equal(self, node):
        left_val = self.interpret(node.children[0])
        right_val = self.interpret(node.children[1])
        return left_val != right_val
