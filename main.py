import os
from pprint import pprint
import re
from tinydb import TinyDB, Query
from pprint import pprint

# catalogue data table
db = TinyDB("db.json")
# cart data table
db2 = TinyDB("db2.json")
# orders data table
db3 = TinyDB("db3.json")

# The application entry point 
def entrypoint():
    os.system("clear")
    print("\t**********************************************")
    print("\t***  Kyosk - Hello wwelcome to the catalogue!  ***")
    print("\t**********************************************")

    print(
        """\tHello welcome to kyosk cart
    \t Usage:
            A simple Cart made using python and databse set up with tinyDB
        """
    )
    print("\t**********************************************")

#The applications main menu
def main_menu():
    print("\n[1] Place‌‌ an ‌‌Order, or add to your cart.")
    print("[2] Cancel  ‌the‌‌ Order‌.")
    print("[3] view Cart.")
    print("[4] View Orders.")
    print("[q] Quit.")

    choice = input(
        """Hi again,
    Usage:
        hello, what would you like to do?
    """
    )

    if choice == "1":
        order()
    elif choice == "2":
        cancel_order()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        view_order()
    elif choice == "q":
        print("\nThanks for using us. Bye.")
    else:
        print("\nI didn't understand that choice.\n")

#The order function
def order():
    print("[1] Yes.")
    print("[2] No.")

    req = input(
        """,
    Hi:
        would you like to order an item?
    """
    )

    if req == "1":
        Cat = db.all()
        pprint(Cat)

        item = input(
            """
        Hi:
            Kindly name the item you want to buy? (e.g oil)
        """
        )
        item = item.lower()
        It = Query()
        try:
            if query_item := db.search(It.item.matches(item, flags=re.IGNORECASE)):
                
                # pprint(f"The item {item} catalogue is as {query_item}")

                check = db.get(It.item == item)
                oldquantity = (check["quantity"])

                if oldquantity == 0:
                    print("Theres no item of that product currently available")
                    order()

                newquantity = input(
                    """
                **:
                    Kindly indicate the quantity you want to buy?
                **
                """
                )

                newquantity = int(newquantity)

                if newquantity == 0:
                    print("Kindly enter a number greater than 0")
                    order()
                elif oldquantity >= newquantity:
                    balance = oldquantity - newquantity
                    db.update({"quantity": balance}, It.item == item)
                    db2.insert({"item": item, "quantity": newquantity})
                else:
                    print(f"The quantity you've entered in not in stock, the current available stock is {oldquantity}, kindly input a lower quantity")
                    order()

                print("[1] Yes.")
                print("[2] No.")

                res = input(
                    """,
                Hi:
                    hello, would you like to view cart?
                """
                )

                if res == "1":
                    view_cart()
                elif res == "2":
                    main_menu()
                else:
                    print("\nInvaid choice.\n")

            else:
                print("The item does not exist,kindly input an item that exists")
                order()

        except TypeError:
            print('Item does not exist')
            order()

    elif req == "2":
        main_menu()
    else:
        print("\nI didn't understand that choice.\n")

#The view cart function 
def view_cart():
    cart = db2.all()
    pprint(cart)
    if cart:
        print("\n[1] Yes.")
        print("[2] No‌.")

        confirm = input(
            """Hi here is your cart,
        Message:
            Do you want to confirm order?
        """
        )

        if confirm == "1":
            new_dict = {}
            cart = db2.all()
            for i in cart:
                new_dict |= i
            db3.insert(new_dict)
            db2.truncate()
            print("\n Your order is ready, you will be paid on delivery")
        elif confirm == "2":
            main_menu()
        else:
            print("\nI didn't understand that choice.\n")
    else:
        print("your cart is empty")
        main_menu()

#the cancel order function
def cancel_order():

    print("\n[1] Yes.")
    print("[2] No‌.")

    confirm = input(
        """Hi again,
    Usage:
        Are you sure you want to cancel the orders?
    """
    )

    if confirm == "1":
        # delete the items in the cart and add the back to the original catalogue
        for i in db2:
            cart_quantity = i["quantity"]
            item = i["item"]
            It = Query()
            check = db.get(It.item == item)
            oldquantity = (check["quantity"])
            balance = oldquantity + cart_quantity
            db.update({"quantity": balance}, It.item == item)
        db2.truncate()
        print("\nOrders have been cancelled.")
    elif choice == "2":
        main_menu()
    else:
        print("\nI didn't understand that choice.\n")

#The view order fnction
def view_order():
    cart = db3.all()
    print(f"""Hi, here is your are your previous orders,
        Your Orders:
        """)
    pprint(cart)
    if cart:

        print("\n[1] Exit.")
        print("[2]  Main menu‌.")
        confirm = input(
            """Hi here is your are your previous orders,
        Message:
            Do you want to exit?
        """
        )

        if confirm == "1":
            print("\nThanks for using us. Bye.")
        elif confirm == "2":
            main_menu()
        else:
            print("\nI didn't understand that choice.\n")

    else:
        print("There are no recent orders")


choice = ""
if choice != "q":
    choice = main_menu()