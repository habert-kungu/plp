def cuculate_discount(price, discount_percent):
    # price = int(input("Enter Original price item: "))
    # discount_percent = int(input("Please Enter the Discount percent: "))

    final_price = discount_percent / 100 * price
    final_price = round(final_price, 2)

    print(f"$ {final_price}")


cuculate_discount(50, 20)
