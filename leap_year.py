"""
Script to determine if a given year is a leap year.
Demonstrates the use of conditional statements (if, elif, else) and logical operators (and, or).
Rules for a leap year:
1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
4. The year is a leap year (it has 366 days).
5. The year is not a leap year (it has 365 days).
"""

def is_leap_year(year: int) -> bool:
    """
    Checks if a year is a leap year using chained conditional logic.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_leap_year_concise(year: int) -> bool:
    """
    Checks if a year is a leap year using a single concise conditional expression.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
