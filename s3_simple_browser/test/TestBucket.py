import unittest
from s3_simple_browser.bucket_mgr import *


class TestBucket(unittest.TestCase):

    def test_bucket_list(self):
        list = bucket_list()

        self.assertIsNotNone(list)
        self.assertEqual(1, len(list))

    def test_item_list(self):
        list = item_list("data-bucket")

        self.assertIsNotNone(list)
        self.assertTrue(len(list) > 0)

    def test_item_list_with_prefix(self):
        list = item_list("data-bucket", "a")

        self.assertIsNotNone(list)
        self.assertTrue(len(list) > 0)

    def test_item_key_list(self):
        list = item_key_list("data-bucket")

        self.assertIsNotNone(list)
        self.assertTrue(len(list) > 0)

    def test_get_paths(self):
        paths = get_paths(["a/b/file.txt", "b/file.pdf", "file.json"])

        self.assertIsNotNone(paths)
        self.assertEqual(3, len(paths))
        self.assertEqual(".", paths[0].key)
        self.assertEqual(".", paths[0].normalized_key)
        self.assertEqual("a/b", paths[1].key)
        self.assertEqual("a-b", paths[1].normalized_key)
        self.assertEqual("b", paths[2].key)
        self.assertEqual("b", paths[2].normalized_key)

    def test_get_path(self):
        self.assertEquals("a/b/c", get_path("a/b/c/file.txt"))


if __name__ == '__main__':
    unittest.main()
