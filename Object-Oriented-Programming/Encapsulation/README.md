# Banking System with OOP

This project demonstrates a simple banking system implemented using Object-Oriented Programming (OOP) principles in Python. It showcases concepts such as classes, inheritance, encapsulation, and polymorphism.

## Project Structure

The project consists of a single Python file:

- `main.py`: Contains the implementation of the banking system classes.

## Classes

### Account

Represents a basic account with the following features:
- Initializes with a balance and account holder's name
- Private balance attribute
- Methods to set and get balance
- Method to display account holder's name

### Loan

Represents a loan with the following features:
- Initializes with a loan balance
- Private loan balance attribute
- Methods to set and get loan balance

### PremiumAccount

A premium account that inherits from both Account and Loan:
- Initializes with balance, loan balance, and account holder's name
- Method to calculate and display total balance (account balance + loan balance)

## Usage

To use this banking system:

1. Ensure you have Python installed on your system.
2. Save the code in a file named `main.py`.
3. Run the script using a Python interpreter:

```bash
python main.py

Name  M:Huzaifa
Get loan balance 30000.0
Get balance : 100000.0
Get total balance :  130000.0
