// interpreter/ast.js

/**
 * Abstract Syntax Tree (AST) node types
 */
const NodeType = {
  PROGRAM: 'Program',
  FUNCTION_DECLARATION: 'FunctionDeclaration',
  VARIABLE_DECLARATION: 'VariableDeclaration',
  EXPRESSION_STATEMENT: 'ExpressionStatement',
  LITERAL: 'Literal',
  IDENTIFIER: 'Identifier',
  BINARY_EXPRESSION: 'BinaryExpression',
  // Add more node types as needed
};

/**
 * Abstract Syntax Tree (AST) node base class
 */
class Node {
  constructor(type, loc) {
    this.type = type;
    this.loc = loc;
  }
}

/**
 * Program node
 */
class Program extends Node {
  constructor(body, loc) {
    super(NodeType.PROGRAM, loc);
    this.body = body;
  }
}

/**
 * Function declaration node
 */
class FunctionDeclaration extends Node {
  constructor(id, params, body, loc) {
    super(NodeType.FUNCTION_DECLARATION, loc);
    this.id = id;
    this.params = params;
    this.body = body;
  }
}

/**
 * Variable declaration node
 */
class VariableDeclaration extends Node {
  constructor(id, init, loc) {
    super(NodeType.VARIABLE_DECLARATION, loc);
    this.id = id;
    this.init = init;
  }
}

/**
 * Expression statement node
 */
class ExpressionStatement extends Node {
  constructor(expression, loc) {
    super(NodeType.EXPRESSION_STATEMENT, loc);
    this.expression = expression;
  }
}

/**
 * Literal node
 */
class Literal extends Node {
  constructor(value, loc) {
    super(NodeType.LITERAL, loc);
    this.value = value;
  }
}

/**
 * Identifier node
 */
class Identifier extends Node {
  constructor(name, loc) {
    super(NodeType.IDENTIFIER, loc);
    this.name = name;
  }
}

/**
 * Binary expression node
 */
class BinaryExpression extends Node {
  constructor(operator, left, right, loc) {
    super(NodeType.BINARY_EXPRESSION, loc);
    this.operator = operator;
    this.left = left;
    this.right = right;
  }
}

module.exports = {
  NodeType,
  Node,
  Program,
  FunctionDeclaration,
  VariableDeclaration,
  ExpressionStatement,
  Literal,
  Identifier,
  BinaryExpression,
};