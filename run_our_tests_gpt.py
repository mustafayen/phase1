import unittest
import os
import importlib.util
import sys
from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Directory containing the code and test files
folder = "outputsGPT/gpt3.5"
sys.path.insert(0, folder)

# Counters for overall test statistics
total_tests = 0
passed_tests = 0
failed_tests = 0

# Table to store per-task results
table = PrettyTable()
table.field_names = ["Task ID", "Total Tests", "Passed", "Failed", "Status"]

# Iterate through each task
for task_id in range(30):
    test_file = os.path.join(folder, f"task_{task_id}_our_test.py")

    if os.path.exists(test_file):
        print(f"\n[+] Running tests for Task {task_id}...")

        try:
            # Load the test module dynamically
            spec_test = importlib.util.spec_from_file_location(f"task_{task_id}_our_test", test_file)
            module_test = importlib.util.module_from_spec(spec_test)
            sys.modules[f"task_{task_id}_our_test"] = module_test
            spec_test.loader.exec_module(module_test)

            # Run the tests
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromModule(module_test)
            runner = unittest.TextTestRunner(verbosity=0)
            result = runner.run(suite)

            task_total = result.testsRun
            task_failed = len(result.failures) + len(result.errors)
            task_passed = task_total - task_failed

            total_tests += task_total
            passed_tests += task_passed
            failed_tests += task_failed

            status = "✓ Passed" if task_failed == 0 else "✗ Failed"
            table.add_row([f"Task {task_id}", task_total, task_passed, task_failed, status])

            # Optional: Show details if failed
            if task_failed > 0:
                for test, traceback in result.failures + result.errors:
                    print(f"  [-] Failed: {test}\n    Traceback:\n{traceback}")

        except Exception as e:
            print(f"[!] Error in Task {task_id}: {e}")
            table.add_row([f"Task {task_id}", "N/A", "N/A", "N/A", "⚠️ Error"])

# Print table
print("\n\n========= DETAILED TASK RESULTS =========")
print(table)

# Print overall test results
print("\n========= OVERALL TEST RESULTS =========")
print(f"Total Tests Run   : {total_tests}")
print(f"Successful Tests  : {passed_tests}")
print(f"Failed Tests      : {failed_tests}")
if total_tests > 0:
    print(f"Success Rate      : {(passed_tests / total_tests) * 100:.2f}%")
else:
    print("No tests were executed.")
print("=========================================")



labels = ['Passed', 'Failed']
counts = [passed_tests, failed_tests]
colors = ['green', 'red']

plt.figure(figsize=(6, 6))
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Test Success Rate for GPT-3.5 Tasks')
plt.axis('equal')
plt.tight_layout()
plt.show()

