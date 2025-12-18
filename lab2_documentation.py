def calculate_discount(price: float, discount: float) -> float:
    """
    Calculates the final price after applying a discount.
    
    Args:
        price (float): The original price of the item.
        discount (float): The discount percentage (0 to 100).

    Returns:
        float: The final price.
    
    Raises:
        ValueError: If discount is not between 0 and 100.
    """
    if not (0 <= discount <= 100):
        raise ValueError("Invalid discount")
    return price * (1 - discount / 100)
