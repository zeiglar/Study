import unittest
from PalindromeNumber import Solution

class TestPalindromeNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(121))

    def test_negative_number(self):
        self.assertFalse(self.solution.isPalindrome(-121))

    def test_not_palindrome(self):
        self.assertFalse(self.solution.isPalindrome(123))

    def test_single_digit(self):
        self.assertTrue(self.solution.isPalindrome(7))

    def test_zero(self):
        self.assertTrue(self.solution.isPalindrome(0))

    def test_large_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(123454321))

    def test_large_non_palindrome(self):
        self.assertFalse(self.solution.isPalindrome(123456789))

if __name__ == "__main__":
    unittest.main()
