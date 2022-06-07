import os
from pprint import pprint
from tinydb import TinyDB, Query
from pprint import pprint

# catalogue
db = TinyDB("db.json")
# cart
db2 = TinyDB("db2.json")
# orders
db3 = TinyDB("db3.json")


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


def main_menu():
    print("\n[1] Place‌‌ an ‌‌Order, or add to your cart.")
    print("[2] Cancel  ‌the‌‌ Order‌.")
    print("[3] view Cart.")
    print("[4] View Orders.")
    print("[q] Quit.")

    return input(
        """Hi again,
    Usage:
        hello, what would you like to do?
    """
    )


def order():
    print("[1] Yes.")
    print("[2] No.")

    req = input(
        """,
    Hi:
        hello, would you like to order?
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
        if db.search(It.item.exists()):
            pprint(f"The item {item} does exist")
            newquantity = input(
                """,
            **:
                Kindly indicate the quantity you want to buy?
            """
            )
            oldquantity = db.get(It.item == "oil")
            uid = oldquantity.doc_id
            oldquantity = int(oldquantity["quantity"])

            newquantity = int(newquantity)
            if oldquantity == 0:
                print("Kindly enter a number greater than 0")
            elif oldquantity >= newquantity:
                balance = oldquantity - newquantity
                db.update({"quantity": balance}, It.item == item)
                db2.insert({"item": item, "quantity": newquantity})
            else:
                "The quantity youve entered in not available"
            
            res = input(
                """,
            Hi:
                hello, would you like to view cart?
            """
            )

            print("[1] Yes.")
            print("[2] No.")

            if res == "1":
                view_cart() 
            elif res == "2":
                main_menu()
            else:
                print("\nInvaid choice.\n")

        else:
            return ("The item does not exist")

    elif req == "2":
        main_menu()
    else:
        print("\nI didn't understand that choice.\n")

    


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
        elif choice == "2":
            main_menu()
        else:
            print("\nI didn't understand that choice.\n")
    else:
        print("your cart is empty")


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
        db2.truncate()
        print("\nOrders have been cancelled.")
    elif choice == "2":
        main_menu()
    else:
        print("\nI didn't understand that choice.\n")


def view_order():
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
            print("\nThanks for using us. Bye.")
        elif choice == "2":
            main_menu()
        else:
            print("\nI didn't understand that choice.\n")

    else:
        print('Cart is empty')

entrypoint()


choice = ""
if choice != "q":
    choice = main_menu()

    # entrypoint()
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
