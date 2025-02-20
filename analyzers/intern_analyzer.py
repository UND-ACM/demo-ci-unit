from org.mycompany.abstract import AbstractAnalyzer
from org.mycompany.exception import CalculationException


class StatAnalyzer(AbstractAnalyzer):
    def mean(self, values: list[int]) -> float:
        if len(values) == 0:
            raise CalculationException

        return float(sum(values) / len(values))

    def median(self, values: list[int]) -> float:
        # Avoid zero-length lists
        if len(values) == 0:
            return 0.0

        # Sort values and find the middle
        sorted_values = sorted(values)
        middle = len(sorted_values) // 2

        # Return middle value if odd, otherwise, return average of middle values.
        return float(sorted_values[middle]) \
            if len(sorted_values) % 2 == 1 \
            else float((sorted_values[middle] + sorted_values[middle - 1]) / 2)

    def mode(self, values: list[int]) -> list[int]:
        # Avoid zero-length lists
        if len(values) == 0:
            return []

        # Rank each value by number of occurrences
        ranking = dict()
        for value in values:
            ranking[value] = ranking.get(value, 0) + 1

        # Pick out the max number of occurrences of a value we see. Return any
        # values that match that count.
        max_occurrences = max(ranking.values()) or 0
        return [x for x in ranking.keys() if ranking[x] == max_occurrences]
