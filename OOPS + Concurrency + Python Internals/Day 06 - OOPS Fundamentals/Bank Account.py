import json
import os

class BankAccount:
    def __init__(self, account_number, acc_holder_name, account_type, pin):
        self.account_number = account_number
        self.acc_holder_name = acc_holder_name
        self.account_type = account_type
        self.pin = pin
        self.balance = 0.0
        self.is_active = True
        self.is_frozen = False
        self.transactions = []


    def to_dict(self):
        return {
            "Account Holder Name": self.acc_holder_name,
            "Account Type": self.account_type,
            "Account Pin": self.pin,
            "Balance": self.balance,
            "Active": self.is_active,
            "Frozen": self.is_frozen,
            "Transactions": self.transactions}

    @classmethod
    def from_dict(cls, account_number, data):
        account = cls(
            account_number,
            data["Account Holder Name"],
            data["Account Type"],
            data["Account Pin"])
        account.balance = data["Balance"]
        account.is_active = data["Active"]
        account.is_frozen = data["Frozen"]
        account.transactions = data.get("Transactions", [])
        return account


    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")


    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"Withdrawn: {amount}")


class AccountStorage:
    FILE = "accounts.json"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump({}, f)

    def load(self):
        with open(self.FILE, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.FILE, "w") as f:
            json.dump(data, f)

    def add_account(self, account):
        data = self.load()
        if account.account_number in data:
            raise Exception("Account already exists")
        data[account.account_number] = account.to_dict()
        self.save(data)

    def get_acc_by_number(self, account_number):
        data = self.load()
        if account_number not in data:
            raise Exception("Account not found")
        return BankAccount.from_dict(account_number, data[account_number])

    def save_account(self, account):
        data = self.load()
        data[account.account_number] = account.to_dict()
        self.save(data)


class UserAuthentication:

    def __init__(self, storage):
        self.storage = storage

    def login(self, account_number, pin):
        account = self.storage.get_acc_by_number(account_number)
        if account.pin != pin:
            raise Exception("Invalid PIN")

        if not account.is_active:
            raise Exception("Account is closed")
        return account


class User:

    def __init__(self, account, storage):
        self.account = account
        self.storage = storage

    def deposit(self, amount):
        if self.account.is_frozen:
            raise Exception("Account is frozen")
        if amount <= 0:
            raise Exception("Amount must be positive")

        self.account.deposit(amount)
        self.storage.save_account(self.account)

    def withdraw(self, amount):
        if self.account.is_frozen:
            raise Exception("Account is frozen")
        if amount <= 0:
            raise Exception("Amount must be positive")
        if amount > self.account.balance:
            raise Exception("Insufficient balance")

        self.account.withdraw(amount)
        self.storage.save_account(self.account)

    def check_balance(self):
        return self.account.balance



class Bank:
    def __init__(self, storage):
        self.storage = storage

    def open_account(self, account):
        account.is_active = True
        self.storage.save_account(account)

    def close_account(self, account):
        if account.balance != 0:
            raise Exception("Balance must be zero to close account")
        account.is_active = False
        self.storage.save_account(account)

    def freeze_account(self, account):
        account.is_frozen = True
        self.storage.save_account(account)

    def unfreeze_account(self, account):
        account.is_frozen = False
        self.storage.save_account(account)


class BankSystemControls:
    def __init__(self):
        self.storage = AccountStorage()
        self.auth = UserAuthentication(self.storage)
        self.bank = Bank(self.storage)

    def create_account(self):
        acc_no = input("Account number: ")
        name = input("Account holder name: ")
        acc_type = input("Account type: ")
        pin = int(input("Set PIN: "))

        account = BankAccount(acc_no, name, acc_type, pin)
        self.storage.add_account(account)
        print("Account created successfully")

    def user_mode(self):
        try:
            acc_no = input("Account number: ")
            pin = int(input("PIN: "))

            account = self.auth.login(acc_no, pin)
            user = User(account, self.storage)

            while True:
                print("\nUSER MODE")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transactions")
                print("5. Exit")

                choice = input("Choose: ")

                if choice == "1":
                    amt = float(input("Amount: "))
                    user.deposit(amt)

                elif choice == "2":
                    amt = float(input("Amount: "))
                    user.withdraw(amt)

                elif choice == "3":
                    print("Balance:", user.check_balance())

                elif choice == "4":
                    print(*account.transactions, sep="\n")

                elif choice == "5":
                    break

        except Exception as e:
            print("Error:", e)

    def bank_mode(self):
        try:
            acc_no = input("Enter account number: ")
            account = self.storage.get_acc_by_number(acc_no)

            while True:
                print("\nBANK MODE")
                print("1. Open Account")
                print("2. Close Account")
                print("3. Freeze Account")
                print("4. Unfreeze Account")
                print("5. Exit")

                choice = input("Choose: ")

                if choice == "1":
                    self.bank.open_account(account)
                elif choice == "2":
                    self.bank.close_account(account)
                elif choice == "3":
                    self.bank.freeze_account(account)
                elif choice == "4":
                    self.bank.unfreeze_account(account)
                elif choice == "5":
                    break

        except Exception as e:
            print("Error:", e)

    def main(self):
        while True:
            print("\nBANK SYSTEM")
            print("1. Create Account")
            print("2. User Mode")
            print("3. Bank Mode")
            print("4. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.user_mode()
            elif choice == "3":
                self.bank_mode()
            elif choice == "4":
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    system = BankSystemControls()
    system.main()