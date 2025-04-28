# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def find_longest_word(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

class TestFindLongestWord(unittest.TestCase):

    def test_find_longest_word_single_word(self):
        self.assertEqual(find_longest_word(["hello"]), "hello")

    def test_find_longest_word_multiple_words(self):
        self.assertEqual(find_longest_word(["apple", "banana", "cherry"]), "banana")

    def test_find_longest_word_empty_list(self):
        self.assertEqual(find_longest_word([]), "")

    def test_find_longest_word_equal_length_words(self):
        self.assertEqual(find_longest_word(["cat", "dog", "bat"]), "cat")

if __name__ == '__main__':
    unittest.main()