
import logging

logging.basicConfig(level=logging.INFO)

def calculate_discount(price, discount, tax_rate=0.0):
    """Calculate discounted price with optional tax."""
    if not (0 <= discount <= 1):
        raise ValueError("Discount must be between 0 and 1.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    discounted = price - (price * discount)
    taxed = discounted + (discounted * tax_rate)
    logging.info(f"Calculated final price: {taxed}")
    return taxed

def format_currency(value):
    return f"${value:.2f}"

# Example usage
if __name__ == "__main__":
    price = 100
    discount = 0.15
    tax_rate = 0.07
    final_price = calculate_discount(price, discount, tax_rate)
    print("Final price:", format_currency(final_price))
