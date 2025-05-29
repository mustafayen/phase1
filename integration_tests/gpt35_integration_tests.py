"""
Integration tests generated using GPT-3.5 for the ListAnalyzer class.
"""

import unittest
from collections import Counter

# In case ListAnalyzer is in the same file for test convenience.
class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def remove_duplicates(self):
        return list(set(self.lst))

    def most_frequent_element(self):
        counter = Counter(self.lst)
        return counter.most_common(1)[0][0]

    def find_pairs_with_sum(self, target):
        seen = set()
        pairs = set()
        for number in self.lst:
            complement = target - number
            if complement in seen:
                pairs.add(tuple(sorted((number, complement))))
            seen.add(number)
        return list(pairs)


class TestListAnalyzerIntegration(unittest.TestCase):

    def test_remove_duplicates_then_pairs(self):
        """
        After calling remove_duplicates, the new list should still allow
        correct pair-sum detection for a given target.
        """
        original = [1, 2, 2, 3, 4, 4, 5]
        analyzer = ListAnalyzer(original)

        dedup = analyzer.remove_duplicates()
        dedup_analyzer = ListAnalyzer(dedup)

        self.assertCountEqual(
            dedup_analyzer.find_pairs_with_sum(6),
            [(1, 5), (2, 4)]
        )

    def test_most_frequent_still_present_after_dedup(self):
        """
        The element that was most frequent in the original list
        must still be present after duplicates are removed.
        """
        original = [7, 7, 7, 8, 8, 9]
        analyzer = ListAnalyzer(original)

        most_freq_before = analyzer.most_frequent_element()
        dedup = analyzer.remove_duplicates()

        self.assertIn(most_freq_before, dedup)

    def test_frequency_and_pairs_consistency(self):
        """
        Ensure consistency across all three methods:
        * most_frequent_element is correct,
        * find_pairs_with_sum catches expected pair,
        * the same pair exists after duplicate removal.
        """
        original = [10, 10, 5, 5, 5, 1, 4]
        analyzer = ListAnalyzer(original)

        # Check most-frequent element
        self.assertEqual(analyzer.most_frequent_element(), 5)

        # Check that (10, 5) is detected as a sum-15 pair
        self.assertIn(
            (5, 10),
            [tuple(sorted(p)) for p in analyzer.find_pairs_with_sum(15)]
        )

        # After deduplication, the pair should still be detectable
        dedup_analyzer = ListAnalyzer(analyzer.remove_duplicates())
        self.assertIn(
            (5, 10),
            [tuple(sorted(p)) for p in dedup_analyzer.find_pairs_with_sum(15)]
        )


if __name__ == "__main__":
    unittest.main()
