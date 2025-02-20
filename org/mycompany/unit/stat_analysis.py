import unittest
import warnings
from types import ModuleType

from org.mycompany.abstract.analyzer import AbstractAnalyzer
from org.mycompany.exception.calculation_exception import CalculationException

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
        list_even = list(range(10, 19)) # 14.0 median, 14.0 mean
        list_odd = list_even + [31] # 14.5 median, 15.7 mean
        list_repeats_once = [10, 11, 12, 12, 13, 14] # 12 median, 12 mean
        list_repeats_twice = [10, 11, 12, 12, 13, 13] # 12 median, 11.833333333... mean

        # Mode tests
        implemented = True
        try:
            analyzer.mode(list_even)
        except NotImplementedError:
            implemented = False
        except:
            pass

        if implemented:
            self.assertListEqual(analyzer.mode(list_empty), list_empty)
            self.assertListEqual(analyzer.mode(list_zeroes_single), list_zeroes_single)
            self.assertListEqual(analyzer.mode(list_zeroes_odd), list_zeroes_single)
            self.assertListEqual(analyzer.mode(list_even), list_even)
            self.assertListEqual(analyzer.mode(list_repeats_once), [12])
            self.assertListEqual(analyzer.mode(list_repeats_twice), [12, 13])
        else:
            warnings.warn("Skipping tests on analyzer.mode as method raised NotImplemented.")

        # Median tests
        implemented = True
        try:
            analyzer.median(list_even)
        except NotImplementedError:
            implemented = False
        except:
            pass

        if implemented:
            self.assertEqualFloat(analyzer.median(list_empty), 0.0)
            self.assertEqualFloat(analyzer.median(list_zeroes_single), 0.0)
            self.assertEqualFloat(analyzer.median(list_zeroes_odd), 0.0)
            self.assertEqualFloat(analyzer.median(list_zeroes_even), 0.0)
            self.assertEqualFloat(analyzer.median(list_single), 10.0)
            self.assertEqualFloat(analyzer.median(list_odd), 14.5)
            self.assertEqualFloat(analyzer.median(list_even), 14.0)
            self.assertEqualFloat(analyzer.median(list_repeats_once), 12.0)
            self.assertEqualFloat(analyzer.median(list_repeats_twice), 12.0)
        else:
            warnings.warn("Skipping tests on analyzer.median as method raised NotImplemented.")

        # Mean tests
        implemented = True
        try:
            analyzer.mean(list_even)
        except NotImplementedError:
            implemented = False
        except:
            pass

        if implemented:
            self.assertRaises(CalculationException, analyzer.mean, list_empty)
            self.assertEqualFloat(analyzer.mean(list_zeroes_single), 0.0)
            self.assertEqualFloat(analyzer.mean(list_zeroes_odd), 0.0)
            self.assertEqualFloat(analyzer.mean(list_zeroes_even), 0.0)
            self.assertEqualFloat(analyzer.mean(list_single), 10.0)
            self.assertEqualFloat(analyzer.mean(list_odd), 15.7)
            self.assertEqualFloat(analyzer.mean(list_even), 14.0)
            self.assertEqualFloat(analyzer.mean(list_repeats_once), 12.0)
            self.assertEqualFloat(analyzer.mean(list_repeats_twice), 11.833333333333334)
        else:
            warnings.warn("Skipping tests on analyzer.mean as method raised NotImplemented.")


