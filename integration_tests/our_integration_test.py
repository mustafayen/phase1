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

    def test_integration_remove_duplicates_and_most_frequent(self):
        lst = [1, 2, 2, 3, 3, 3, 4]
        analyzer = ListAnalyzer(lst)
        unique = analyzer.remove_duplicates()
        most_freq = analyzer.most_frequent_element()
        self.assertEqual(unique, [1, 2, 3, 4])
        self.assertEqual(most_freq, 3)

    def test_integration_find_pairs_after_duplicate_removal(self):
        lst = [1, 2, 3, 2, 4, 3]
        analyzer = ListAnalyzer(lst)
        unique = analyzer.remove_duplicates()
        analyzer = ListAnalyzer(unique)
        pairs = analyzer.find_pairs_with_sum(5)
        self.assertCountEqual(pairs, [(1, 4), (2, 3)])

    def test_all_methods_combined(self):
        lst = [2, 4, 2, 4, 6, 6, 1]
        analyzer = ListAnalyzer(lst)
        self.assertEqual(analyzer.most_frequent_element(), 2)
        self.assertCountEqual(analyzer.remove_duplicates(), [2, 4, 6, 1])
        self.assertCountEqual(analyzer.find_pairs_with_sum(6), [(2, 4)])

if __name__ == '__main__':
    unittest.main()
