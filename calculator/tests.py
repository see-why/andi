from functions.get_file_content import get_file_content

import unittest

class TestGetFileContent(unittest.TestCase):

    def test_read_main_py(self):
        result = get_file_content("calculator", "main.py")
        print(result)
        self.assertIsInstance(result, str)  # Assuming the function returns a string
        self.assertTrue(len(result) > 0)   # Ensure the content is not empty

    def test_read_pkg_calculator_py(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_read_invalid_file(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

if __name__ == "__main__":
    unittest.main()