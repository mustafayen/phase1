import os
import sys
import coverage
import unittest

cov = coverage.Coverage()
cov.start()

folder = "outputsGPT/gpt3.5"

sys.path.insert(0, folder)

loader = unittest.TestLoader()
suite = unittest.TestSuite()

for i in range(30):
    test_path = os.path.join(folder, f"task_{i}_test.py")
    if os.path.exists(test_path):
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(f"task_{i}_test", test_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            suite.addTests(loader.loadTestsFromModule(module))
        except Exception as e:
            print(f"[!] Failed to import test for task {i}: {e}")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

cov.stop()
cov.save()

print("\n========= COVERAGE REPORT =========")
cov.report()
print("===================================")
