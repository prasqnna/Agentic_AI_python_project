from abc import ABC, abstractmethod
class InsufficientBalanceError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class TransferError(Exception):
    pass

class Customer:
    def __init__(self,customer_id,customer_name,phone_number,email):
        self.customer_id=customer_id
        self.__customer_name=customer_name
        self.__phone_number=phone_number
        self.__email=email
    def display_details(self):
       
        print(f'Customer id is {self.customer_id}')
        print(f'Customer name is {self.__customer_name}')
        print(f'Customer phone number is {self.__phone_number}')
        print(f'Customer email id is {self.__email}')
#customer1=Customer(1,"lakshmi","9441986354","prasannabont@gmail.com")
customer2=Customer(2345,"saketh",8210642977,"saketh@codegnan.com")
#customer1.display_details()
class Account(ABC):
    def __init__(self,account_number,balance,account_type,customer):
        self.account_number=account_number
        self.__balance=balance
        self.account_type=account_type
        self.customer=customer
        self.transaction_history = []
    def display(self):
        self.customer.display_details()
      
        print(f'customer account number is {self.account_number}')
        print(f'customer balanace is {self.__balance}')
        print(f'customer account type is {self.account_type}')
    def get_balance(self):
        return self.__balance
    def update_balance(self, new_balance):
        self.__balance = new_balance
    @abstractmethod
    def calculate_interest(self):
        pass
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

            self.transaction_history.append(f'Deposited ₹{amount}')

            print(f'{amount} deposited successfully')
            print(f'Updated balance is ₹{self.__balance}')
        else:
            raise InvalidAmountError("Deposit amount must be greater than 0")
    def withdrawal_amount(self, withdrawal):
        if withdrawal <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than 0")
        elif withdrawal <= self.__balance:
            self.__balance -= withdrawal

            self.transaction_history.append(f'Withdrawn ₹{withdrawal}')

            print(f'{withdrawal} withdrawn successfully')
            print(f'Balance after withdrawal is {self.__balance}')

        else:
            raise InsufficientBalanceError("Insufficient balance")
    def transfer(self, destination_account, amount):
        if amount <= 0:
            raise InvalidAmountError("Transfer amount must be greater than 0")
        if amount > self.__balance:
            raise TransferError("Insufficient balance for transfer")

        sender_balance = self.get_balance()
        receiver_balance = destination_account.get_balance()

        new_sender_balance = sender_balance - amount
        new_receiver_balance = receiver_balance + amount

        self.update_balance(new_sender_balance)
        destination_account.update_balance(new_receiver_balance)

        # Transaction History
        self.transaction_history.append(f'Transferred ₹{amount} to account {destination_account.account_number}')

        destination_account.transaction_history.append(f'Received ₹{amount} from account {self.account_number}')

        print(f'₹{amount} transferred successfully')
        print(f'Sender balance is ₹{self.get_balance()}')
        print(f'Receiver balance is ₹{destination_account.get_balance()}')
        
     # Transaction History
    def display_transaction_history(self):

        print("\n------ Transaction History ------")

        if len(self.transaction_history) == 0:
            print("No transactions found")

        else:
            for transaction in self.transaction_history:
                print(transaction)
    def account_statement(self):
        print("\n========== ACCOUNT STATEMENT ==========")

        self.customer.display_details()

        print("\n------ Account Details ------")
        print(f'Account Number: {self.account_number}')
        print(f'Account Type: {self.account_type}')
        print(f'Current Balance: ₹{self.get_balance()}')

        print("\n------ Transaction History ------")

        if len(self.transaction_history) == 0:
            print("No transactions found")
        else:
            for transaction in self.transaction_history:
                print(transaction)

        print("======================================")
            

class Savings_account(Account):
    def __init__(self,account_number,balance,account_type,customer,rate):
        self.rate=rate
        super().__init__(account_number,balance,account_type,customer)
    def display(self):
        super().display()
        print(f'The rate of interest is {self.rate} %')
    def calculate_interest(self):
        current_balance = self.get_balance()
        interest = current_balance * self.rate / 100

        self.transaction_history.append(
            f'Interest calculated: ₹{interest}'
        )

        print(f'Interest amount is ₹{interest}')
        return interest
class Current_account(Account):
    def __init__(self,account_number,balance,account_type,customer,overdraft_limit):
        super().__init__(account_number,balance,account_type,customer)
        self.overdraft_limit=overdraft_limit
    def display(self):
        super().display()
        print(f'The overdraft limit is {self.overdraft_limit}')
    def withdrawal_amount(self, withdrawal):
        if withdrawal <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than 0")
        current_balance = self.get_balance()

        maximum_available = current_balance + self.overdraft_limit

        if withdrawal <= maximum_available:

            new_balance = current_balance - withdrawal

            self.update_balance(new_balance)

            # Transaction History
            self.transaction_history.append(f'Withdrawn ₹{withdrawal}')
            print(f'{withdrawal} withdrawn successfully')
            print(f'Updated balance is {self.get_balance()}')
        else:
            raise InsufficientBalanceError("Withdrawal exceeds overdraft limit")
    def calculate_interest(self):
        print("Current account does not provide interest.")



user=Savings_account("987654321456",5000,"Savings",customer2,5)
user2=Savings_account("123456789012",20000,"Savings",customer2,5)
user1=Current_account("456789123456",50000,"Current",customer2,10000)
# ==============================
# MENU DRIVEN BANKING SYSTEM
# ==============================

while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Display Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Fund Transfer")
    print("5. Calculate Interest")
    print("6. Transaction History")
    print("7. Account Statement")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # 1. Display Account
    if choice == "1":
        user.display()

    # 2. Deposit
    elif choice == "2":

        try:
            amount = float(input("Enter deposit amount: "))
            user.deposit(amount)

        except InvalidAmountError as e:
            print("Error:", e)

        except ValueError:
            print("Please enter a valid number")

    # 3. Withdraw
    elif choice == "3":

        try:
            amount = float(input("Enter withdrawal amount: "))
            user.withdrawal_amount(amount)

        except InvalidAmountError as e:
            print("Error:", e)

        except InsufficientBalanceError as e:
            print("Error:", e)

        except ValueError:
            print("Please enter a valid number")

    # 4. Fund Transfer
    elif choice == "4":

        try:
            amount = float(input("Enter transfer amount: "))
            user.transfer(user2, amount)

        except InvalidAmountError as e:
            print("Error:", e)

        except TransferError as e:
            print("Error:", e)

        except ValueError:
            print("Please enter a valid number")

    # 5. Calculate Interest
    elif choice == "5":

        user.calculate_interest()

    # 6. Transaction History
    elif choice == "6":

        user.display_transaction_history()

    # 7. Account Statement
    elif choice == "7":

        user.account_statement()

    # 8. Exit
    elif choice == "8":

        print("\nThank you for using the Bank Management System!")
        break

    # Invalid choice
    else:

        print("Invalid choice. Please select 1 to 8.")
