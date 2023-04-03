import unittest
from hw8 import MySet

class TestMySet(unittest.TestCase):
    def test_init(self):
        s = MySet([1, 2, 3])
        self.assertEqual(len(s), 3)
        self.assertIn(1, s)
        self.assertIn(2, s)
        self.assertIn(3, s)

    def test_len(self):
        s = MySet([1, 2, 3])
        self.assertEqual(len(s), 3)

    def test_contains(self):
        s = MySet([1, 2, 3])
        self.assertIn(1, s)
        self.assertIn(2, s)
        self.assertIn(3, s)
        self.assertNotIn(4, s)

    def test_put(self):
        s = MySet([1, 2, 3])
        s.put(4)
        self.assertIn(4, s)
        self.assertEqual(len(s), 4)

    def test_put_bucket_size(self):
        s = MySet([1, 2, 3,4,5,6,7,8,9,10])
        s.put(4)
        self.assertEqual(len(s), 10)

    def test_remove(self):
        s = MySet([1, 2, 3])
        s.remove(2)
        self.assertNotIn(2, s)
        self.assertEqual(len(s), 2)

    def test_remove_missing(self):
        s = MySet([1, 2, 3])
        with self.assertRaises(KeyError):
            s.remove(4)

    def test_eq(self):
        s1 = MySet([1, 2, 3])
        s2 = MySet([2, 1, 3])
        s3 = MySet([1, 2, 4])
        self.assertEqual(s1, s2)
        self.assertNotEqual(s1, s3)

if __name__ == '__main__':
    unittest.main()