# Advanced Bank Management System

## Description

The **Advanced Bank Management System** is a console-based banking application developed using **Python and Object-Oriented Programming (OOP)** concepts.

This project simulates basic banking operations such as depositing money, withdrawing money, transferring funds, calculating interest, viewing transaction history, and generating an account statement.

The project also demonstrates important OOP concepts including **abstraction, encapsulation, inheritance, and polymorphism**, along with **custom exception handling**.

---

## Objectives

* To develop a simple banking management system using Python.
* To implement Object-Oriented Programming concepts in a real-world application.
* To manage customer and account information.
* To perform basic banking transactions.
* To maintain transaction history.
* To handle invalid operations using custom exceptions.

---

## Features

Customer Management

* Stores customer ID
* Stores customer name
* Stores phone number
* Stores email address
* Displays customer details

Account Management

The system supports:

* **Savings Account**
* **Current Account**

Deposit

Users can deposit money into their account.

The system does not allow zero or negative deposit amounts.

Withdrawal

Users can withdraw money from their account.

The system checks whether sufficient funds are available.

Fund Transfer

The system allows money to be transferred from one account to another.

In the current implementation:

* `user` → Sender account
* `user2` → Receiver account

Interest Calculation

The Savings Account calculates interest using:

```text
Interest = Balance × Rate / 100
```

For example:

```text
Balance = ₹5,000
Rate = 5%

Interest = 5000 × 5 / 100
         = ₹250
```

The Current Account does not provide interest.

 Transaction History

The system records:

* Deposits
* Withdrawals
* Fund transfers
* Interest calculations

Account Statement

The account statement displays:

* Customer details
* Account number
* Account type
* Current balance
* Transaction history

 Overdraft Facility

The Current Account supports an overdraft limit.

For example:

```text
Balance = ₹50,000
Overdraft Limit = ₹10,000

Maximum withdrawal = ₹60,000
```

---

OOP Concepts Used
 1. Class and Object

Classes are used as blueprints for creating customers and accounts.

Main classes:

```text
Customer
Account
Savings_account
Current_account
```

Objects created in the project include:

```python
customer1
user
user2
user1
```

---

2. Encapsulation

Encapsulation is used to protect important data.

For example:

```python
self.__balance
```

The customer information is also private:

```python
self.__customer_name
self.__phone_number
self.__email
```

The account balance is accessed through:

```python
get_balance()
update_balance()
```

---

3. Abstraction

The `Account` class is an abstract class:

```python
class Account(ABC):
```

It contains the abstract method:

```python
@abstractmethod
def calculate_interest(self):
    pass
```

The child classes provide their own implementation.

---

4. Inheritance

The `Savings_account` and `Current_account` classes inherit from the `Account` class.

```python
class Savings_account(Account):
```

```python
class Current_account(Account):
```

This allows the child classes to reuse the functionality of the parent class.

---

5. Polymorphism

Polymorphism is implemented through method overriding.

The `calculate_interest()` method behaves differently in different account classes.

Savings Account:

```text
Calculates interest
```

Current Account:

```text
Does not provide interest
```

The `withdrawal_amount()` method is also overridden in the Current Account to support overdraft.

---

Exception Handling

The project uses custom exceptions to handle banking errors.

### Custom Exceptions

```python
class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class TransferError(Exception):
    pass
```

Errors Handled

| Exception                  | Purpose                          |
| -------------------------- | -------------------------------- |
| `InvalidAmountError`       | Handles zero or negative amounts |
| `InsufficientBalanceError` | Handles insufficient balance     |
| `TransferError`            | Handles transfer-related errors  |
| `ValueError`               | Handles invalid numeric input    |

The project uses:

```python
try
except
raise
```

for error handling.

---

Application Menu

The application provides the following menu:

```text
========== BANK MANAGEMENT SYSTEM ==========

1. Display Account
2. Deposit
3. Withdraw
4. Fund Transfer
5. Calculate Interest
6. Transaction History
7. Account Statement
8. Exit
```

---

How to Run

### Step 1: Install Python

Make sure Python is installed.

Check the version:

```bash
python --version
```
 Step 2: Clone the Repository

```bash
git clone <your-repository-url>
```

Step 3: Open the Project Folder

```bash
cd Advanced-Bank-Management-System
```

Step 4: Run the Program

If your Python file is named `bank_management.py`:

```bash
python bank_management.py
```

---

Project Structure

```text
Advanced-Bank-Management-System/
│
├── bank_management.py
│
└── README.md
```

---

Sample Output

```text
========== BANK MANAGEMENT SYSTEM ==========

1. Display Account
2. Deposit
3. Withdraw
4. Fund Transfer
5. Calculate Interest
6. Transaction History
7. Account Statement
8. Exit

Enter your choice:
```

Example deposit:

```text
Enter your choice: 2
Enter deposit amount: 2000

2000 deposited successfully
Updated balance is ₹7000
```

Example invalid amount:

```text
Enter your choice: 2
Enter deposit amount: -500

Error: Deposit amount must be greater than 0
```

---

Learning Outcomes

This project helped in understanding:

* Python OOP concepts
* Classes and objects
* Encapsulation
* Abstraction
* Inheritance
* Polymorphism
* Method overriding
* Custom exceptions
* `try-except` error handling
* Menu-driven applications
* Transaction management

---



