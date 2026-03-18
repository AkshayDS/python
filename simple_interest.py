"""
Script to calculate Simple Interest.
Demonstrates basic arithmetic and formula usage.
Formula: SI = (P * R * T) / 100
Where:
P = Principal amount
R = Rate of interest per year
T = Time in years
"""

def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculates simple interest given principal, rate, and time.
    """
    return (principal * rate * time) / 100

def calculate_total_amount(principal: float, rate: float, time: float) -> float:
    """
    Calculates the total amount (Principal + Interest).
    """
    interest = calculate_simple_interest(principal, rate, time)
    return principal + interest
