import importlib
import unittest
from os import listdir

from org.mycompany.unit import StatAnalyzerTestCase

def bootstrap():
    # Iterate over available analyzers
    for filename in [x[:-3] for x in listdir("./analyzers") if x[-3:] == ".py"]:
        # Try import target. Assert it's of the proper class.
        try:
            importlib.invalidate_caches()
            target_module = importlib.import_module("analyzers." + filename)
        except ModuleNotFoundError:
            print("Couldn't find requested module!")
            exit(1)

        # Build test suite
        suite = unittest.TestSuite()
        suite.addTest(StatAnalyzerTestCase("test_analyzer", target_module, "StatAnalyzer"))

        # Run unit tests on class
        runner = unittest.TextTestRunner()
        runner.run(suite)


if __name__ == '__main__':
    bootstrap()