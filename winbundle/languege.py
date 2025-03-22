# winbundle/language.py

# Define the language syntax
class Language:
  def __init__(self):
    self.keywords = ["let", "const", "function", "if", "else", "for", "while", "switch", "case", "default"]
    self.operators = ["+", "-", "*", "/", "%", "==", "!=", ">", "<", ">=", "<="]
    self.separators = ["(", ")", "{", "}", "[", "]"]
    self.identifiers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  def tokenize(self, code):
    # Tokenize the code into keywords, operators, separators, and identifiers
    tokens = []
    for char in code:
      if char in self.keywords:
        tokens.append({"type": "keyword", "value": char})
      elif char in self.operators:
        tokens.append({"type": "operator", "value": char})
      elif char in self.separators:
        tokens.append({"type": "separator", "value": char})
      elif char in self.identifiers:
        tokens.append({"type": "identifier", "value": char})
      else:
        tokens.append({"type": "unknown", "value": char})
    return tokens

  def parse(self, tokens):
    # Parse the tokens into an abstract syntax tree (AST)
    ast = []
    for token in tokens:
      if token["type"] == "keyword":
        if token["value"] == "let":
          # Parse a let statement
          ast.append({"type": "let", "name": tokens[1]["value"], "value": tokens[2]["value"]})
        elif token["value"] == "const":
          # Parse a const statement
          ast.append({"type": "const", "name": tokens[1]["value"], "value": tokens[2]["value"]})
        elif token["value"] == "function":
          # Parse a function statement
          ast.append({"type": "function", "name": tokens[1]["value"], "params": tokens[2]["value"], "body": tokens[3]["value"]})
      elif token["type"] == "operator":
        # Parse an operator
        ast.append({"type": "operator", "value": token["value"]})
      elif token["type"] == "separator":
        # Parse a separator
        ast.append({"type": "separator", "value": token["value"]})
      elif token["type"] == "identifier":
        # Parse an identifier
        ast.append({"type": "identifier", "value": token["value"]})
    return ast

# Define the language interpreter
class Interpreter:
  def __init__(self, ast):
    self.ast = ast
    self.variables = {}

  def interpret(self):
    # Interpret the AST
    for node in self.ast:
      if node["type"] == "let":
        # Interpret a let statement
        self.variables[node["name"]] = node["value"]
      elif node["type"] == "const":
        # Interpret a const statement
        self.variables[node["name"]] = node["value"]
      elif node["type"] == "function":
        # Interpret a function statement
        self.variables[node["name"]] = {"params": node["params"], "body": node["body"]}
      elif node["type"] == "operator":
        # Interpret an operator
        if node["value"] == "+":
          # Interpret an addition operator
          self.variables[node["name"]] = self.variables[node["name"]] + node["value"]
        elif node["value"] == "-":
          # Interpret a subtraction operator
          self.variables[node["name"]] = self.variables[node["name"]] - node["value"]
        elif node["value"] == "*":
          # Interpret a multiplication operator
          self.variables[node["name"]] = self.variables[node["name"]] * node["value"]
        elif node["value"] == "/":
          # Interpret a division operator
          self.variables[node["name"]] = self.variables[node["name"]] / node["value"]
      elif node["type"] == "separator":
        # Interpret a separator
        pass
      elif node["type"] == "identifier":
        # Interpret an identifier
        pass

# Define the language compiler
class Compiler:
  def __init__(self, ast):
    self.ast = ast

  def compile(self):
    # Compile the AST into machine code
    machine_code = []
    for node in self.ast:
      if node["type"] == "let":
        # Compile a let statement
        machine_code.append("mov eax, " + node["value"])
        machine_code.append("mov [" + node["name"] + "], eax")
      elif node["type"] == "const":
        # Compile a const statement
        machine_code.append("mov eax, " + node["value"])
        machine_code.append("mov [" + node["name"] + "], eax")
      elif node["type"] == "function":
        # Compile a function statement
        machine_code.append("jmp " + node["name"])
        machine_code.append("label " + node["name"])
        for param in node["params"]:
          machine_code.append("mov eax, " + param["value"])
          machine_code.append("mov [" + param["name"] + "], eax")
        machine_code.append("call " + node["body"])
      elif node["type"] == "operator":
        # Compile an operator
        if node["value"] == "+":
          # Compile an addition operator
          machine_code.append("mov eax, " + node["left"])
          machine_code.append("add eax, " + node["right"])
          machine_code.append("mov [" + node["result"] + "], eax")
        elif node["value"] == "-":
          # Compile a subtraction operator
          machine_code.append("mov eax, " + node["left"])
          machine_code.append("sub eax, " + node["right"])
          machine_code.append("mov [" + node["result"] + "], eax")
        elif node["value"] == "*":
          # Compile a multiplication operator
          machine_code.append("mov eax, " + node["left"])
          machine_code.append("mul eax, " + node["right"])
          machine_code.append("mov [" + node["result"] + "], eax")
        elif node["value"] == "/":
          # Compile a division operator
          machine_code.append("mov eax, " + node["left"])
          machine_code.append("div eax, " + node["right"])
          machine_code.append("mov [" + node["result"] + "], eax")
      elif node["type"] == "separator":
        # Compile a separator
        pass
      elif node["type"] == "identifier":
        # Compile an identifier
        machine_code.append("mov eax, [" + node["value"] + "]")
    return machine_code
   