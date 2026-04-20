import unittest
from LongestSubstringWithoutRepeatingCharacters import Solution

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_cases(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)  # "abc"
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)    # "b"
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)   # "wke"

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_character(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)

    def test_all_unique(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdef"), 6)

    def test_all_same(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("aaaaaa"), 1)

    def test_mixed(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("dvdf"), 3)  # "vdf"
        self.assertEqual(self.solution.lengthOfLongestSubstring("anviaj"), 5)  # "nviaj"

if __name__ == "__main__":
    unittest.main()
