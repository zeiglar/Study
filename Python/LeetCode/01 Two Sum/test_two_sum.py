import unittest

from TwoSum import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.twoSum([2,7,11,15], 9), [0,1])

    def test_no_solution(self):
        self.assertEqual(self.solution.twoSum([1,2,3], 7), [])

    def test_multiple_solutions(self):
        # Only the first valid pair should be returned
        result = self.solution.twoSum([3,2,4], 6)
        self.assertIn(result, ([1,2], [2,1]))

    def test_negative_numbers(self):
        self.assertEqual(self.solution.twoSum([-3,4,3,90], 0), [0,2])

    def test_duplicates(self):
        self.assertEqual(self.solution.twoSum([3,3], 6), [0,1])

if __name__ == "__main__":
    unittest.main()
