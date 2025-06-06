from functions.get_files_info import get_files_info

def run_tests():
    print("Test 1: Listing current directory")
    print(get_files_info("calculator", "."))
    print("\nTest 2: Listing pkg directory")
    print(get_files_info("calculator", "pkg"))
    print("\nTest 3: Attempting to list /bin (should fail)")
    print(get_files_info("calculator", "/bin"))
    print("\nTest 4: Attempting to list parent directory (should fail)")
    print(get_files_info("calculator", "../"))

if __name__ == "__main__":
    run_tests() 