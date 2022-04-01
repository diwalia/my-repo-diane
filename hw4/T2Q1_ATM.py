"""
Simple ATM program
Using exception handling code blocks such as try/ except / else / finally,
write a program that simulates an ATM machine to withdraw money.
(NB: the more code blocks the better, but try to use at least two key words e.g. try/except)

Tasks:
1. Prompt user for a pin code
2. If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again.
You can give a user a maximum of 3 attempts and then exit a program.
3. Set account balance to 100.
4. Now we need to simulate cash withdrawal
5. Accept the withdrawal amount
6. Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be negative!)
7. However, when a user asks to ‘withdraw’ more money than they have on their account,
then you need to raise an error an exit the program.

"""

import sys

print("Welcome to the simple ATM program")
input("Press ENTER to continue")

def pin_code():
    attempt = 0
    while attempt < 3:
        pin = int(input("Please Enter your 4 digit pin code: "))
        if pin == (1234):
            print("Pin code entered successfully!")
            break
        else:
            print("Incorrect pin code, please try again")
            attempt += 1
    if attempt == 3:
        sys.exit("Incorrect pin code, you have no more remaining attempts to enter your pin. Goodbye!")
    else:
        print("Proceed to Menu Options:")
pin_code()


def menu_options():
    active = True
    option = 0
    balance = 100.00
    while active:
        # print("1: Deposit")
        print("1: Balance")
        print("2: Withdraw")
        print("3: Quit")
        option = int(input("Please select a number for your transaction: "))

        # check for balance
        if option == 1:
            print(f"balance: £ {balance}")

        # cash withdraw
        elif option == 2:
            print(f"Your total amount available to withdraw is: £ {balance}")
            withdraw = float(input("Withdraw: £ "))
            try:
                if withdraw > balance:
                    raise ValueError
            except ValueError:
                sys.exit(f"The entered amount £ {withdraw} that you wish to withdraw is higher than your remaining balance which is £ {balance} only. Goodbye!")
            else:
                balance = balance - withdraw
            # finally:
            #     break

            # while True:
            #     withdraw = int(input("Withdraw: £"))
            #     if withdraw > balance:
            #         print("Cannot withdraw more than available balance")
            #         continue
            #     balance = balance - withdraw
            #     break
            # quit
        elif option == 3:
            sys.exit("Thank you and have a great day, Goodbye!")
menu_options()