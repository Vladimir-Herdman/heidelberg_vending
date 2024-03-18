"""
This module gets the money of the user, and then their choice of what to buy.
"""
def get_money():
    """
    Takes in user input to determine a cash amount that is greater than 0, then returns that amount

    Parameters:
    None: No function arguments

    Returns:
    float: The cash amount given
    """
    user_cash = -1.00  # Just initializing with fake before use
    decimal_user_cash = 3  # Just initializing with fake before use

    while user_cash <= 0 or len(decimal_user_cash) > 2:
        try:
            user_cash = float(input("Please enter the amount of money you have: $"))
            decimal_user_cash = str(user_cash).split('.')[1]

            assert user_cash > 0  # Check if cash greater than 0, raise error if not
            assert len(decimal_user_cash) <= 2  # Check if decimal of cash less than or equal to 2, raise error if not

        except AssertionError:
            if user_cash <= 0:  # Cash less than 0, not valid to buy with
                print("\nYou can't buy anything with no money (and I won't pay you if it's negative), earn some and try again!")
            elif len(decimal_user_cash) > 2:  # Not valid money input, can't have thousandth or less of money
                print("\nYou can't have more than two decimals of cash, enter proper amount!")

        except Exception:  # Not a valid input, such as letters or spaces
            print(f"\nThat is not a valid number, please enter cash amount!")

    print()
    return user_cash

def get_choice(inventory_list):
  """
  Determines choice of user, wether that be to exit, or numbers 1, 2, 3, or 4

  Parameters:
  List: list to be used (should be copy)

  Returns:
  str | int: the choice, 'exit' or 1 through 4
  """
  for index, item in enumerate(inventory_list, 1):  # use special f-string format to better see what is printed
      print(f"{index}. "
      f"{item['name']} "
      f"({item['price']:.2f}) - "
      f"{item['quantity']} left")
  choice = 0
  while choice not in range(1,5):
    choice = input("\nPlease enter the number of the item you wish to purchase: ")

    if choice.isnumeric() and int(choice) in range(1,5):
      return int(choice)
    elif choice.isalpha() and choice == 'exit':
      return 'exit'
    elif choice.isalpha():
      print("Choice must be a number 1 through 4, go again")
    else:
      print("Invalid selection, please enter number 1 through 4")
