shopping_cart = {}

print(""" Welcome to Primus Scooby-Doo Emporium! Here are your options: 
1: Add item to your shopping cart.
2: Remove item from your shopping cart.
3: View your shopping cart.
0: Exit Primus' Best Produce and print your shopping cart
""")

exit_string = 'Thank you for shopping at Primus Scooby-Doo Emporium! Here is your final shopping cart.'

option = int(input("Please enter one of the available options. "))

while option != 0:
    if option == 1:
        item = input("What item would you like to add? ")
        amount = int(input("How many would you like? "))
        shopping_cart[item] = amount
        if item in shopping_cart:
            print("You already have this item in your cart.")
            # would you like to add more of this item?
        else:
            amount = int(input("How many would you like? "))
            shopping_cart[item] = amount
    elif option == 2:
        item = input("What item would you like to remove? ")
        #amount = int(input("How many would you like to remove? ")):
        del shopping_cart[item]
    elif option == 3:
        print(shopping_cart.format(item, amount))
    elif option != 0:
        print("Please enter 1 to add to you cart, 2 to remove an item from your cart, 3 to see your cart, or 0 to exit.")
else:
    print(exit_string, shopping_cart)

option = int(input("Please enter one of the available options: "))
