from store import Store
import products
import promotion

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotion.SecondHalfPrice("Second Half price!")
third_one_free = promotion.ThirdOneFree("Third One Free!")
thirty_percent = promotion.PercentDiscount("30% off!", 30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = Store(product_list)


def start(store_object):
    """Shows user the menu of options of actions, asks for their choice, and performs the chosen function"""
    while True:
        print(
            """Store Menu\n   __________\n1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit""")
        user_choice = input("Please enter your choice 1-4: ")
        if user_choice == '4':
            break  # Exit the loop and end the program
        elif user_choice in ('1', '2', '3'):
            if user_choice == '1':
                menu_of_products(product_list)
            elif user_choice == '2':
                show_total_amount_in_store(best_buy)
            elif user_choice == '3':
                make_an_order(product_list)
        else:
            print("Invalid input! Please enter a valid menu option (1-4).")


def menu_of_products(list_of_products):
    print("--------")
    item_number = 1
    for item in list_of_products:
        print(f"{item_number}. {item.show()}")
        item_number += 1
    print("--------")


def show_total_amount_in_store(store_object):
    total_amount = store_object.get_total_quantity()
    print(f"Total of {total_amount} items in store.")


def make_an_order(list_of_products):
    menu_of_products(list_of_products)
    shopping_list = []
    print(f"_________\nWhen you want to finish your order, please "
          f"enter empty text.")
    user_choice = "."
    shipping = False
    while user_choice != "":
        user_choice = input("Which product # do you want? ")
        if user_choice == "":
            total_price = best_buy.order(shopping_list)
            print(f"*********\nOrder made! Total payment: {total_price}")
            break
        try:
            user_choice = int(user_choice) - 1
        except ValueError:
            print("Invalid input! Please enter a valid product number.")
            continue
        product = list_of_products[user_choice]
        if product == list_of_products[4]:

            if not shipping:
                shopping_list.append((product, product.maximum))
                shipping = True
                print(f"{product.name} Product added to list!\n")
            else:
                print("Maximum for this product is 1. You already have this item on your list.")
        else:
            quantity = int(input("What quantity would you like? "))
            shopping_list.append((product, quantity))
            for item in shopping_list:
                print(f"{item[0].name}, quantity: {item[1]}")
            print("Product added to list!\n")


def main():
    start(best_buy)


if __name__ == "__main__":
    main()
