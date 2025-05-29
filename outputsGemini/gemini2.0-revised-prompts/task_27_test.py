import unittest
# Assuming generate_parentheses is in a file named task_27_code.py or similar
# If it's in the same file as the tests, you don't need the import statement.
# from task_27_code import generate_parentheses

# --- The generate_parentheses function (as provided by you) ---
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
# --- End of generate_parentheses function ---


class TestGenerateParentheses(unittest.TestCase):

    def test_n_equals_0(self):
        """Test with n = 0."""
        self.assertEqual(generate_parentheses(0), [""])

    def test_n_equals_1(self):
        """Test with n = 1."""
        self.assertEqual(generate_parentheses(1), ["()"])

    def test_n_equals_2(self):
        """Test with n = 2."""
        self.assertEqual(sorted(generate_parentheses(2)), sorted(["(())", "()()"]))

    def test_n_equals_3(self):
        """Test with n = 3."""
        self.assertEqual(sorted(generate_parentheses(3)), sorted(["((()))", "(()())", "()(())", "()()()", "(())()"]))

    def test_n_equals_4(self):
        """Test with n = 4."""
        # Corrected expected list (14 unique combinations for n=4)
        expected = [
            "(((())))", "((()()))", "((())())", "((()))()",
            "(()(()))", "(()()())", "(()())()", "(())(())",
            "()((()))", "()(()())", "()(())()", "()()(())",
            "()()()()", "(())()()" # This one was missing, and some were duplicated.
        ]
        self.assertEqual(len(generate_parentheses(4)), 14) # Verify the count first
        self.assertEqual(sorted(generate_parentheses(4)), sorted(expected))

    def test_n_equals_negative(self):
        """Test with a negative n."""
        self.assertEqual(generate_parentheses(-1), [])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)