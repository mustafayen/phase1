import unittest


# --- ListAnalyzer class (as provided previously, assumed to be correct) ---
class ListAnalyzer:
    """
    A class to analyze lists, providing methods to remove duplicates,
    find the most frequent element, and find pairs with a specific sum.
    """

    def __init__(self, data):
        """
        Initializes the ListAnalyzer with a list of data.
        A copy of the data is made to avoid external modifications affecting the analyzer.
        """
        self.data = list(data)

    def remove_duplicates(self):
        """
        Removes duplicate elements from the list while preserving their original order
        of first appearance.

        Returns:
            A new list with unique elements. The internal 'data' of the ListAnalyzer
            instance remains unchanged by this method.
        """
        seen = set()
        result = []
        for item in self.data:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def most_frequent_element(self):
        """
        Returns the element with the highest frequency in the analyzer's list.
        If there is a tie in frequency, it returns the one that appears first in the list.

        Returns:
            The most frequent element (any type). Returns None if the list is empty.
        """
        if not self.data:
            return None

        frequency_map = {}
        for element in self.data:
            frequency_map[element] = frequency_map.get(element, 0) + 1

        max_frequency = -1
        most_frequent = None

        # Iterate through the original list to find the element with the highest frequency
        # and handle ties by selecting the first encountered element.
        for element in self.data:
            if frequency_map[element] > max_frequency:
                max_frequency = frequency_map[element]
                most_frequent = element

        return most_frequent

    def find_pairs_with_sum(self, target):
        """
        Finds all unique pairs of numbers in the analyzer's list that add up to a target sum.
        A pair (a, b) is considered the same as (b, a).

        Args:
            target: The target sum (integer).

        Returns:
            A list of tuples, where each tuple represents a unique pair of numbers
            (sorted internally, e.g., (1, 5) not (5, 1)) that add up to the target sum.
            Returns an empty list if no such pairs exist. The list of pairs is sorted
            to ensure consistent output for testing.
        """
        pairs = set()  # Use a set of tuples to automatically handle uniqueness
        seen = set()  # To track numbers encountered so far

        for num in self.data:
            complement = target - num
            if complement in seen:
                pair = tuple(sorted((num, complement)))
                pairs.add(pair)
            seen.add(num)  # Add num to seen *after* checking its complement

        return sorted(list(pairs))  # Sort the list of pairs for consistent testing


# --- End of ListAnalyzer class ---


class TestListAnalyzerIntegration(unittest.TestCase):

    def test_chaining_remove_duplicates_then_most_frequent(self):
        """
        Integration test: Verify most_frequent_element behavior after removing duplicates.
        Original list has a tie-breaker.
        """
        initial_list = [1, 2, 2, 1, 3, 3, 3, 4]
        analyzer = ListAnalyzer(initial_list)

        self.assertEqual(analyzer.most_frequent_element(), 3,
                         "Should return 3 as the most frequent element in the original list.")

        deduplicated_list = analyzer.remove_duplicates()
        expected_deduplicated = [1, 2, 3, 4]
        self.assertEqual(deduplicated_list, expected_deduplicated,
                         "remove_duplicates should return [1, 2, 3, 4].")

        analyzer_deduplicated = ListAnalyzer(deduplicated_list)

        self.assertEqual(analyzer_deduplicated.most_frequent_element(), 1,
                         "After deduplication, 1 should be the most frequent (first encountered tie-breaker).")

    def test_chaining_remove_duplicates_then_find_pairs_with_sum(self):
        """
        Integration test: Verify find_pairs_with_sum behavior after removing duplicates.
        Demonstrates how removing duplicates can affect pair finding.
        """
        initial_list = [1, 2, 2, 4, 6, 8]
        analyzer = ListAnalyzer(initial_list)
        target_sum = 8

        # --- FIX IS HERE ---
        # With the current find_pairs_with_sum logic, (4,4) is NOT found
        # if there's only one '4' in the list during the iteration *before* it's added to 'seen'.
        # The first 4 (num=4, complement=4) will not find 4 in seen, then 4 is added to seen.
        # So, for [1, 2, 2, 4, 6, 8], only (2,6) should be found.
        expected_original_pairs = [(2, 6)]
        # --- END FIX ---

        self.assertEqual(analyzer.find_pairs_with_sum(target_sum), expected_original_pairs,
                         f"Original list should find {expected_original_pairs} for sum {target_sum}.")

        deduplicated_list = analyzer.remove_duplicates()
        expected_deduplicated = [1, 2, 4, 6, 8]
        self.assertEqual(deduplicated_list, expected_deduplicated,
                         "remove_duplicates should return [1, 2, 4, 6, 8].")

        analyzer_deduplicated = ListAnalyzer(deduplicated_list)

        # After deduplication, only one '4' exists, so (4,4) pair still cannot be formed. (2,6) should still be found.
        # The expected result remains the same as the original list in this specific case.
        expected_deduplicated_pairs = [(2, 6)]
        self.assertEqual(analyzer_deduplicated.find_pairs_with_sum(target_sum), expected_deduplicated_pairs,
                         f"After deduplication, only {expected_deduplicated_pairs} should be found for sum {target_sum}.")

        self.assertEqual(analyzer.data, initial_list,
                         "Original analyzer's data should remain unchanged after remove_duplicates.")

    def test_edge_cases_and_consistency(self):
        """
        Integration test: Covers edge cases like empty list, all duplicates,
        and verifies consistency when chaining with different scenarios.
        """
        # Scenario A: Empty list
        empty_list = []
        analyzer_empty = ListAnalyzer(empty_list)
        self.assertIsNone(analyzer_empty.most_frequent_element(),
                          "most_frequent_element on empty list should return None.")
        self.assertEqual(analyzer_empty.remove_duplicates(), [],
                         "remove_duplicates on empty list should return an empty list.")
        self.assertEqual(analyzer_empty.find_pairs_with_sum(10), [],
                         "find_pairs_with_sum on empty list should return an empty list.")

        # Scenario B: List with all duplicates
        all_duplicates_list = [5, 5, 5, 5, 5]
        analyzer_dup = ListAnalyzer(all_duplicates_list)

        self.assertEqual(analyzer_dup.most_frequent_element(), 5,
                         "Most frequent element in all-duplicate list should be the element itself.")

        deduplicated_dup_list = analyzer_dup.remove_duplicates()
        expected_deduplicated_dup = [5]
        self.assertEqual(deduplicated_dup_list, expected_deduplicated_dup,
                         "remove_duplicates on all-duplicate list should return a list with one element.")

        analyzer_deduplicated_dup = ListAnalyzer(deduplicated_dup_list)

        self.assertEqual(analyzer_deduplicated_dup.most_frequent_element(), 5,
                         "Most frequent element on deduplicated all-duplicate list should still be the element.")

        # Check find_pairs_with_sum on deduplicated list (target = 10, using 5+5)
        # It should NOT find (5,5) because there's only one '5' after deduplication
        self.assertEqual(analyzer_deduplicated_dup.find_pairs_with_sum(10), [],
                         "find_pairs_with_sum should return empty for (5,5) on [5] list.")

        # Check find_pairs_with_sum on original list (target = 10, using 5+5)
        # It SHOULD find (5,5) because there are multiple 5s, allowing a pair to form.
        self.assertEqual(analyzer_dup.find_pairs_with_sum(10), [(5, 5)],
                         "find_pairs_with_sum should find (5,5) on original all-duplicate list.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)