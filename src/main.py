import logging
from typing import List

logging.basicConfig(level=logging.INFO)


class Calculator:
    """A simple calculator class for demonstration."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            logging.error("Division by zero attempted")
            raise ValueError("Cannot divide by zero")
        return a / b


def process_numbers(numbers: List[int]) -> int:
    """
    Process a list of numbers and return the sum of even numbers.
    """
    if not numbers:
        logging.warning("Empty list provided to process_numbers")
        return 0

    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num

    return total


# -----------------------------
# EXCLUDED FROM COVERAGE
# -----------------------------
def main():  # pragma: no cover
    logging.info("Application started")

    calc = Calculator()

    result1 = calc.add(10, 20)
    logging.info(f"Addition result: {result1}")

    try:
        result2 = calc.divide(50, 5)
        logging.info(f"Division result: {result2}")
    except ValueError as e:
        logging.error(f"Error: {e}")

    numbers = [1, 2, 3, 4, 5, 6]
    even_sum = process_numbers(numbers)
    logging.info(f"Sum of even numbers: {even_sum}")

    logging.info("Application finished")


if __name__ == "__main__":  # pragma: no cover
    main()

