import unittest
import avgSubarrayOfSizeK

class TestAvgSubarrayOfSizeK(unittest.TestCase):
    def test_findAveragesOfOfSubarrays(self):
        result=avgSubarrayOfSizeK.findAveragesOfOfSubarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
        self.assertEqual(result, [2.2, 2.8, 2.4, 3.6, 2.8])

if __name__=="__main__":
    unittest.main()
