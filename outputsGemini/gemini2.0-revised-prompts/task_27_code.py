def generate_parentheses(n):
  """
  Generates all valid combinations of n pairs of parentheses using backtracking.

  Args:
    n: The number of pairs of parentheses (non-negative integer).

  Returns:
    A list of strings, each representing a well-formed combination of parentheses.
  """
  if n < 0:
    return []  # Handle negative input for n
  if n == 0:
    return [""] # Base case: n=0 returns a list with an empty string

  result = []

  def backtrack(current_combination, open_count, close_count):
    # Base case: if the current combination has reached the desired length
    if len(current_combination) == 2 * n:
      result.append("".join(current_combination))
      return

    # Add an opening parenthesis if we haven't exceeded the allowed open count
    if open_count < n:
      current_combination.append("(")
      backtrack(current_combination, open_count + 1, close_count)
      current_combination.pop()  # Backtrack: remove the last added parenthesis

    # Add a closing parenthesis if it forms a valid pair (i.e., open_count > close_count)
    if close_count < open_count:
      current_combination.append(")")
      backtrack(current_combination, open_count, close_count + 1)
      current_combination.pop()  # Backtrack: remove the last added parenthesis

  backtrack([], 0, 0)
  return result