from abc import ABC, abstractmethod


class AbstractAnalyzer(ABC):
    @abstractmethod
    def mean(self, values: list[int]) -> float:
        """
        Calculate the mean of a list of integers.
        :param values: The list of integers.
        :return: A float representing the mean.
        """
        ...

    @abstractmethod
    def median(self, values: list[int]) -> float:
        """
        Calculate the median of a list of integers.
        :param values: The list of integers.
        :return: A float representing the median.
        """
        ...

    @abstractmethod
    def mode(self, values: list[int]) -> list[int]:
        """
        Calculate the mode of a list of integers.
        :param values: The list of integers.
        :return: A list of integers representing the mode.
        """
        ...