// interpreter/parser.js

const { Parser } = require('esprima');

const parser = new Parser({
  // Options for the parser
  tolerant: true, // Allow the parser to recover from errors
  loc: true, // Include location information in the AST
});

/**
 * Parse a string of code into an Abstract Syntax Tree (AST)
 * @param {string} code - The code to parse
 * @returns {Object} The parsed AST
 */
function parse(code) {
  try {
    const ast = parser.parseScript(code);
    return ast;
  } catch (error) {
    // Handle parsing errors
    console.error(`Error parsing code: ${error.message}`);
    throw error;
  }
}

module.exports = { parse };