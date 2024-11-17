def calculate_discount(price, discount_percent):
    # If the discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No dicount applied
        return price

try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percent: "))

    # Calculate the final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Display result
    if final_price > price:
        print(f"Final price after applying the discount: ${final_price}")
    else:
        print(f"price without discount percent : ${price}")
except ValueError:
    print("Enter valid number")