"""
This module is for processing and running all the information across the created modules.
"""
import inventory as inv
import user_io as ui

import user_io2 as ui2

def main():
    print("Welcome to the Vending Machine!")
    cash = ui.get_money()
    ui.get_choice(inv.inventory_list, cash)

def main2():
    print("Welcome to the Vending Machine!")
    cash = ui2.get_money()

    choice = ''
    while choice != 'exit':
        choice = ui2.get_choice(inv.inventory_list.copy())

        if choice == 'exit':
            print("\nThanks for coming by!")
            break
    
        # What did they buy section
        choice_name = inv.inventory_list[choice - 1]['name']
        choice_price = inv.inventory_list[choice - 1]['price']
        choice_quant = inv.inventory_list[choice - 1]['quantity']


        print(f"\nYou have selected a {choice_name}. The price is ${choice_price:.2f}.")
        if cash < choice_price:
            print(f"\nYou do not have enough cash to buy that, get something else or 'exit'\n")
            continue
        elif choice_quant < 1:
            print(f"{choice_name} has no more left in stock, buy something else or 'exit'\n")
            continue
        else:
            print(f"\nYou have inserted ${cash:.2f}. Your change is ${(cash - choice_price):.2f}.")
            cash -= choice_price
            print(f"\nThank you for your purchase! Enjoy your {choice_name}\n\n{'':-<60}\n")
            inv.inventory_list[choice - 1]['quantity'] -= 1

if __name__ == '__main__':
    choice_here = int(input("Your's (1) or the team's main (2): "))
    print(f"\n{'':-<60}\n")
    if choice_here == 1:
        main()
    elif choice_here == 2:
        main2()
    else:
        print("You did not make the right choice, 1 or 2")
