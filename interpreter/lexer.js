// interpreter/lexer.js

const { Lexer } = require('moo');

const lexer = new Lexer({
  // Define the lexer rules
  keywords: [
    'if',
    'else',
    'while',
    'for',
    'function',
    'var',
    'let',
    'const',
  ],
  rules: [
    ['\\s+', 'WS'], // whitespace
    ['\\n', 'NL'], // newline
    ['[a-zA-Z_][a-zA-Z_0-9]*', 'IDENTIFIER'], // identifier
    ['[0-9]+', 'NUMBER'], // number
    ['[+*/-]', 'OPERATOR'], // operator
    ['\\(', '('], // left parenthesis
    ['\\)', ')'], // right parenthesis
    ['\\{', '{'], // left curly bracket
    ['\\}', '}'], // right curly bracket
    ['\\[', '['], // left square bracket
    ['\\]', ']'], // right square bracket
    ['\\.', '.'], // dot
    ['\\,', ','], // comma
    ['\\:', ':'], // colon
    ['\\;', ';'], // semicolon
  ],
});

/**
 * Tokenize a string of code into an array of tokens
 * @param {string} code - The code to tokenize
 * @returns {Array} The tokenized code
 */
function tokenize(code) {
  try {
    const tokens = lexer.tokenize(code);
    return tokens;
  } catch (error) {
    // Handle lexing errors
    console.error(`Error lexing code: ${error.message}`);
    throw error;
  }
}

module.exports = { tokenize };