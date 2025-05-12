
def calculate_discount(price, discount):
    """Calculate discounted price"""
    return price - (price * discount)

def format_currency(value):
    return f"${value:.2f}"

# Example usage
if __name__ == "__main__":
    price = 100
    discount = 0.15
    final_price = calculate_discount(price, discount)
    print("Final price:", format_currency(final_price))
