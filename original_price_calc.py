"""
Module: original_price_calc
Provides utility functions for calculating discounted prices with optional tax.
"""

import logging

logging.basicConfig(level=logging.INFO)

def calculate_discount(price: float, discount: float, tax_rate: float = 0.0) -> float:
    """Calculate the final price after discount and tax."""
    if not (0 <= discount <= 1):
        raise ValueError("Discount must be between 0 and 1.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    discounted = price - (price * discount)
    taxed = discounted * (1 + tax_rate)
    logging.info(f"Calculated final price: {taxed}")
    return taxed

def format_currency(value: float) -> str:
    """Return a string representation of a float in currency format."""
    return f"${value:.2f}"

# Example usage
if __name__ == "__main__":
    price: float = 100
    discount: float = 0.15
    tax_rate: float = 0.07
    final_price = calculate_discount(price, discount, tax_rate)
    print("Final price:", format_currency(final_price))
