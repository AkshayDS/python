# Problem: Calculate Compound Interest
# Description: Write a function `compound_interest(principal, rate, time)` that returns the total amount including compound interest.
# Formula: A = P * (1 + R/100)^T. The interest is A - P.

def compound_interest(principal, rate, time):
    amount = principal * ((1 + rate / 100) ** time)
    interest = amount - principal
    return amount, interest

# Basic Example
if __name__ == "__main__":
    p = 1000
    r = 5.0
    t = 2
    
    amount, interest = compound_interest(p, r, t)
    print(f"Principal: {p}, Rate: {r}%, Time: {t} years")
    print(f"Total Amount: {amount:.2f}")
    print(f"Compound Interest: {interest:.2f}")

    # Another example
    p2 = 1200
    r2 = 5.4
    t2 = 2
    amount2, interest2 = compound_interest(p2, r2, t2)
    print(f"\nPrincipal: {p2}, Rate: {r2}%, Time: {t2} years")
    print(f"Total Amount: {amount2:.2f}")
    print(f"Compound Interest: {interest2:.2f}")
