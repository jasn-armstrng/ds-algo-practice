import unittest
import longestSubstring

class TestlongestSubstring(unittest.TestCase):
    def test_lenLongestSubstring(self):
        result=longestSubstring.lenLongestSubstring("abcabcbb")
        self.assertEqual(result, 3)

        result=longestSubstring.lenLongestSubstring("bbbbb")
        self.assertEqual(result, 1)

        result=longestSubstring.lenLongestSubstring("pwwkew")
        self.assertEqual(result, 3)

        result=longestSubstring.lenLongestSubstring("")
        self.assertEqual(result, 0)

        result=longestSubstring.lenLongestSubstring("aab")
        self.assertEqual(result, 2)

        result=longestSubstring.lenLongestSubstring("dvdf")
        self.assertEqual(result, 3)

if __name__=="__main__":
    unittest.main()
