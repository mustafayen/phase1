import unittest
import os
import importlib.util
import sys

# Directory containing the code and test files
folder = "outputs/gpt3.5"

# Counters for overall test statistics
total_tests = 0
passed_tests = 0
failed_tests = 0

# Iterate through each task
for task_id in range(30):
    test_file = os.path.join(folder, f"task_{task_id}_test.py")

    if os.path.exists(test_file):
        print(f"\n[+] Running tests for Task {task_id}...")

        try:
            # Load the test module dynamically
            spec_test = importlib.util.spec_from_file_location(f"task_{task_id}_test", test_file)
            module_test = importlib.util.module_from_spec(spec_test)
            sys.modules[f"task_{task_id}_test"] = module_test
            spec_test.loader.exec_module(module_test)

            # Run the tests
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromModule(module_test)
            runner = unittest.TextTestRunner(verbosity=0, resultclass=unittest.result.TestResult)
            result = runner.run(suite)

            total_tests += result.testsRun
            failed_tests += len(result.failures) + len(result.errors)
            passed_tests += result.testsRun - len(result.failures) - len(result.errors)

        except Exception as e:
            print(f"Error in Task {task_id}: {e}")

# Print overall test results
print("\n\n========= TEST RESULTS =========")
print(f"Total Tests Run   : {total_tests}")
print(f"Successful Tests  : {passed_tests}")
print(f"Failed Tests      : {failed_tests}")
if total_tests > 0:
    print(f"Success Rate      : {(passed_tests / total_tests) * 100:.2f}%")
else:
    print("No tests were executed.")
print("=================================")
