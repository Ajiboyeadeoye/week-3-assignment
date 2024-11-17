def calculate_discount(price, discount_percent):
    # If the discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No dicount applied
        return price
    

# Calculate the final price using the function
final_price = calculate_discount(40, 60)


