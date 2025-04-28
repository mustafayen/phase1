import unittest
import os
import importlib.util
import sys

# Directory containing the Gemini test files
test_folder = "tests"
# Directory containing the GPT-3.5 code files
code_folder = "outputsGPT/gpt3.5"

# Counters
total_tasks = 30
skipped_tasks = 0
total_tests_run = 0
passed_tests = 0
failed_tests = 0

# Start iterating over all tasks
for task_id in range(total_tasks):
    test_file = os.path.join(test_folder, f"task_{task_id}_test.py")
    code_file = os.path.join(code_folder, f"task_{task_id}_code.py")

    if os.path.exists(test_file) and os.path.exists(code_file):
        print(f"\n[+] Running tests for Task {task_id}...")

        try:
            # Load the code module dynamically
            spec_code = importlib.util.spec_from_file_location(f"task_{task_id}_code", code_file)
            module_code = importlib.util.module_from_spec(spec_code)
            sys.modules["your_module"] = module_code  # name used inside test files
            spec_code.loader.exec_module(module_code)

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

            total_tests_run += result.testsRun
            failed_tests += len(result.failures) + len(result.errors)
            passed_tests += result.testsRun - len(result.failures) - len(result.errors)

        except Exception as e:
            print(f"⚠️  Skipping Task {task_id} due to error: {e}")
            skipped_tasks += 1

# Calculate success rates
if total_tests_run > 0:
    test_success_rate = (passed_tests / total_tests_run) * 100
else:
    test_success_rate = 0.0

executed_tasks = total_tasks - skipped_tasks
if total_tasks > 0:
    overall_task_success_rate = (executed_tasks / total_tasks) * 100
else:
    overall_task_success_rate = 0.0

# Print final report
print("\n\n========= FINAL REPORT =========")
print(f"Total Tasks            : {total_tasks}")
print(f"Executed Tasks         : {executed_tasks}")
print(f"Skipped Tasks          : {skipped_tasks}")
print(f"Overall Task Success   : {overall_task_success_rate:.2f}%")
print("---------------------------------")
print(f"Total Tests Run        : {total_tests_run}")
print(f"Successful Tests       : {passed_tests}")
print(f"Failed Tests           : {failed_tests}")
print(f"Test Success Rate      : {test_success_rate:.2f}%")
print("=================================")
