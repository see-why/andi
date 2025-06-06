from functions.get_file_content import get_file_content
import unittest
from functions.write_file import write_file
from functions.delete_file import delete_file

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

class TestWriteFile(unittest.TestCase):
    def test_write_to_root(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Successfully wrote"))
        
        # Clean up
        delete_result = delete_file("calculator", "lorem.txt")
        print(f"Cleanup: {delete_result}")

    def test_write_to_subdirectory(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Successfully wrote"))
        
        # Clean up
        delete_result = delete_file("calculator", "pkg/morelorem.txt")
        print(f"Cleanup: {delete_result}")

    def test_write_outside_working_dir(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

if __name__ == "__main__":
    unittest.main()