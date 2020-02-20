import unittest
from s3_simple_browser.bucket_mgr import *


class BucketTest(unittest.TestCase):

    def setUp(self):
         from dotenv import load_dotenv
         load_dotenv()

    def test_bucket_list(self):
        list = bucket_list()

        self.assertIsNotNone(list)
        self.assertTrue(len(list) > 0)

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

    def test_download(self):
        filename = download_object("data-bucket", "a/file.txt", "/tmp")

        self.assertIsNotNone(filename)
        self.assertEqual("/tmp/file.txt", filename)

    def test_upload(self):
        filename = upload_object("data-bucket", "a/newfile.txt", "/tmp/file.txt")

        self.assertIsNotNone(filename)
        self.assertEqual("a/newfile.txt", filename)


if __name__ == '__main__':
    unittest.main()
