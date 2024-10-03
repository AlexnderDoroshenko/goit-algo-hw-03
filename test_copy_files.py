import os
import shutil
import unittest
import tempfile
from copy_files import copy_files


class TestFileCopying(unittest.TestCase):

    def setUp(self):
        """
        Create a temporary directory structure for testing.
        """
        self.src_dir = tempfile.mkdtemp()
        self.dest_dir = tempfile.mkdtemp()

        # Create test directories and files
        os.makedirs(os.path.join(self.src_dir, 'subdir1'))
        os.makedirs(os.path.join(self.src_dir, 'subdir2'))

        with open(os.path.join(self.src_dir, 'file1.txt'), 'w') as f:
            f.write('This is a text file.')

        with open(os.path.join(self.src_dir, 'file2.csv'), 'w') as f:
            f.write('Column1,Column2\nValue1,Value2')

        with open(os.path.join(self.src_dir, 'subdir1', 'file3.txt'), 'w') as f:
            f.write('This is another text file.')

        with open(os.path.join(self.src_dir, 'subdir2', 'file4.csv'), 'w') as f:
            f.write('Data1,Data2\nValue3,Value4')

        # Add image files
        with open(os.path.join(self.src_dir, 'image1.png'), 'wb') as f:
            # Create a 1KB PNG file (not a valid image)
            f.write(os.urandom(1024))

        with open(os.path.join(self.src_dir, 'image2.jpg'), 'wb') as f:
            # Create a 1KB JPG file (not a valid image)
            f.write(os.urandom(1024))

    def tearDown(self):
        """
        Clean up the temporary directories after the test.
        """
        shutil.rmtree(self.src_dir)
        shutil.rmtree(self.dest_dir)

    def test_copy_files(self):
        """
        Test the copy_files function to ensure files are copied correctly.
        """
        copy_files(self.src_dir, self.dest_dir)

        # Check if text files exist in the destination directory
        self.assertTrue(os.path.exists(
            os.path.join(self.dest_dir, 'txt', 'file1.txt')))
        self.assertTrue(os.path.exists(
            os.path.join(self.dest_dir, 'txt', 'file3.txt')))
        self.assertTrue(os.path.exists(
            os.path.join(self.dest_dir, 'csv', 'file2.csv')))
        self.assertTrue(os.path.exists(
            os.path.join(self.dest_dir, 'csv', 'file4.csv')))

        # Check if image files exist in the destination directory
        self.assertTrue(os.path.exists(
            os.path.join(self.dest_dir, 'png', 'image1.png')))
        self.assertTrue(os.path.exists(
            os.path.join(self.dest_dir, 'jpg', 'image2.jpg')))

        # Check file contents for text files
        with open(os.path.join(self.dest_dir, 'txt', 'file1.txt')) as f:
            self.assertEqual(f.read(), 'This is a text file.')

        with open(os.path.join(self.dest_dir, 'csv', 'file2.csv')) as f:
            self.assertEqual(f.read(), 'Column1,Column2\nValue1,Value2')


if __name__ == "__main__":
    unittest.main()
