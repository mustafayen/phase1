# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022



import unittest

def group_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())

class TestGroupAnagrams(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(group_anagrams([]), [])

    def test_single_word(self):
        self.assertEqual(group_anagrams(['hello']), [['hello']])

    def test_multiple_anagrams(self):
        self.assertEqual(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])

    def test_no_anagrams(self):
        self.assertEqual(group_anagrams(['car', 'dog', 'bird']), [['car'], ['dog'], ['bird']])

if __name__ == '__main__':
    unittest.main()