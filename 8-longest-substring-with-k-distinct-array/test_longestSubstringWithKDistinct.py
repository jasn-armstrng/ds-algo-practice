import unittest
import longestSubstringWithKDistinct

class TestLongestSubstringWithKDistinct(unittest.TestCase):
    def test_longestSubstring(self):
        result=longestSubstringWithKDistinct.longestSubstring("araaci", 2)
        self.assertEqual(result, 4)

        result=longestSubstringWithKDistinct.longestSubstring("araaci", 1)
        self.assertEqual(result, 2)

        result=longestSubstringWithKDistinct.longestSubstring("cbbebi", 3)
        self.assertEqual(result, 5)

if __name__=="__main__":
    unittest.main()
