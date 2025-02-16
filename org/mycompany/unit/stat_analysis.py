import unittest
from types import ModuleType

from org.mycompany.abstract.analyzer import AbstractAnalyzer
from org.mycompany.exception.zero_division_exception import ZeroDivisionException

class StatAnalyzerTestCase(unittest.TestCase):
    def __init__(self, methodName: str = "runTest", targetModule: ModuleType = AbstractAnalyzer, targetClass: str = "") -> None:
        super().__init__(methodName)
        self.targetModule = targetModule
        self.targetClass = targetClass

    def assertEqualFloat(self, first: float, second: float) -> None:
        self.assertIsInstance(first, float)
        self.assertIsInstance(second, float)
        self.assertEqual(first, second)

    def test_analyzer(self):
        # Get target module
        target_module: ModuleType = self.targetModule
        self.assertIsNotNone(target_module)

        # Instantiate an instance of the type
        self.assertTrue(hasattr(target_module, self.targetClass), "Specified module does not hold specified class!")
        analyzer: AbstractAnalyzer = getattr(target_module, self.targetClass)()
        self.assertIsInstance(analyzer, AbstractAnalyzer, "Class does not implement AbstractAnalyzer!")

        # Create test data
        list_empty = []
        list_zeroes_single = [0]
        list_zeroes_odd = [0] * 7
        list_zeroes_even = [0] * 8
        list_single = [10]
        list_even = list(range(10, 19)) # 14.5 median, 14.5 mean
        list_odd = list_even + [31] # 15.5 median, 16 mean
        list_repeats_once = [10, 11, 12, 12, 13, 14] # 12 median, 12 mean
        list_repeats_twice = [10, 11, 12, 12, 13, 13] # 12 median, 11.833333333... mean

        # Mode tests
        self.assertListEqual(analyzer.mode(list_empty), list_empty)
        self.assertListEqual(analyzer.mode(list_zeroes_single), list_zeroes_single)
        self.assertListEqual(analyzer.mode(list_zeroes_odd), list_zeroes_single)
        self.assertListEqual(analyzer.mode(list_even), list_even)
        self.assertListEqual(analyzer.mode(list_repeats_once), [12])
        self.assertListEqual(analyzer.mode(list_repeats_twice), [12, 13])

        # Median tests
        self.assertEqualFloat(analyzer.median(list_empty), 0.0)
        self.assertEqualFloat(analyzer.median(list_zeroes_single), 0.0)
        self.assertEqualFloat(analyzer.median(list_zeroes_odd), 0.0)
        self.assertEqualFloat(analyzer.median(list_zeroes_even), 0.0)
        self.assertEqualFloat(analyzer.median(list_single), 10.0)
        self.assertEqualFloat(analyzer.median(list_odd), 14.5)
        self.assertEqualFloat(analyzer.median(list_even), 14.0)
        self.assertEqualFloat(analyzer.median(list_repeats_once), 12.0)
        self.assertEqualFloat(analyzer.median(list_repeats_twice), 12.0)

        # Mean tests
        self.assertRaises(ZeroDivisionException, analyzer.mean, list_empty)


