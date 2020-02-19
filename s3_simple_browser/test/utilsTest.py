import unittest
from s3_simple_browser.bucket_mgr import *


class UtilsTest(unittest.TestCase):

    def test_sanitize_key(self):
        self.assertEqual("a-b-c-file.txt", sanitize_key("a/b/c/file.txt"))

    def test_rebuild_key(self):
        self.assertEqual("a/b/c/file.txt", rebuild_key("a-b-c-file.txt"))

    def test_get_path(self):
        self.assertEqual("a/b/c", get_path("a/b/c/file.txt"))

    def test_get_filename(self):
        self.assertEqual("file.txt", get_filename("a/b/c/file.txt"))

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

if __name__ == '__main__':
    unittest.main()
