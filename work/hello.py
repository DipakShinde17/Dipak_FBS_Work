import getpass
import time

class User:
    def __init__(self, card_number, pin, balance=0):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
        self.history = []

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount."
        self.balance += amount
        self.history.append(f"Deposited: ${amount}")
        return f"Deposited ${amount} successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.history.append(f"Withdrew: ${amount}")
        return f"Withdrew ${amount} successfully."

    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def get_history(self):
        return "\n".join(self.history[-5:] or ["No recent transactions."])


class ATM:
    def __init__(self):
        self.users = {
            "12345678": User("12345678", "1234", 1000),
            "87654321": User("87654321", "4321", 500),
        }
        self.current_user = None

    def authenticate(self):
        print("==== Welcome to Python ATM ====")
        card = input("Enter your card number: ")
        pin = getpass.getpass("Enter your PIN: ")

        user = self.users.get(card)
        if user and user.check_pin(pin):
            self.current_user = user
            print("Login successful.\n")
            return True
        else:
            print("Invalid card number or PIN.\n")
            return False

    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Transaction History")
            print("5. Exit")

            ch
