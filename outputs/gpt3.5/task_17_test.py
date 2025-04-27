# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


1. Test case to check if the function returns the correct output for a valid music string:
```python
import unittest

class TestParseMusic(unittest.TestCase):
    
    def test_valid_music_string(self):
        music_string = "CDEFGAB"
        expected_output = ["C", "D", "E", "F", "G", "A", "B"]
        self.assertEqual(parse_music(music_string), expected_output)

if __name__ == '__main__':
    unittest.main()
```

2. Test case to check if the function handles an empty music string correctly:
```python
import unittest

class TestParseMusic(unittest.TestCase):
    
    def test_empty_music_string(self):
        music_string = ""
        expected_output = []
        self.assertEqual(parse_music(music_string), expected_output)

if __name__ == '__main__':
    unittest.main()
```

3. Test case to check if the function raises an error for an invalid music string:
```python
import unittest

class TestParseMusic(unittest.TestCase):
    
    def test_invalid_music_string(self):
        music_string = "ABCDEFGH"
        with self.assertRaises(ValueError):
            parse_music(music_string)

if __name__ == '__main__':
    unittest.main()
```