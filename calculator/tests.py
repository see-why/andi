from functions.get_file_content import get_file_content

def run_tests():
    print("Test 1: Reading main.py")
    print(get_file_content("calculator", "main.py"))
    print("\nTest 2: Reading pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\nTest 3: Attempting to read /bin/cat (should fail)")
    print(get_file_content("calculator", "/bin/cat"))

if __name__ == "__main__":
    run_tests()