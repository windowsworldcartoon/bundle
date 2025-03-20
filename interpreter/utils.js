// interpreter/utils.js

/**
 * Create a new environment
 * @returns {Object} The new environment
 */
function createEnvironment() {
  return {};
}

/**
 * Extend an environment with a new scope
 * @param {Object} env - The environment to extend
 * @param {Object} scope - The new scope to add
 * @returns {Object} The extended environment
 */
function extendEnvironment(env, scope) {
  return { ...env, ...scope };
}

/**
 * Lookup a variable in an environment
 * @param {Object} env - The environment to search
 * @param {string} name - The name of the variable to lookup
 * @returns {any} The value of the variable, or undefined if not found
 */
function lookupVariable(env, name) {
  return env[name];
}

/**
 * Set a variable in an environment
 * @param {Object} env - The environment to modify
 * @param {string} name - The name of the variable to set
 * @param {any} value - The value to set
 */
function setVariable(env, name, value) {
  env[name] = value;
}

/**
 * Create a new function scope
 * @param {Object} env - The environment to create the scope in
 * @param {string[]} params - The parameter names for the function
 * @param {Object} body - The function body
 * @returns {Object} The new function scope
 */
function createFunctionScope(env, params, body) {
  const scope = {};
  params.forEach((param) => {
    scope[param] = undefined;
  });
  return extendEnvironment(env, scope);
}

/**
 * Create a new block scope
 * @param {Object} env - The environment to create the scope in
 * @returns {Object} The new block scope
 */
function createBlockScope(env) {
  return extendEnvironment(env, {});
}

module.exports = {
  createEnvironment,
  extendEnvironment,
  lookupVariable,
  setVariable,
  createFunctionScope,
  createBlockScope,
};