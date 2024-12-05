# Payment Processing System

This project demonstrates the use of **polymorphism** in Python by simulating a payment processing system. The program supports multiple payment methods, each implemented as a class with a common interface for processing payments.

---

## Features

- **Base Class**: `Payment`
  - Provides a generic method for processing payments.

- **Derived Classes**:
  - `CreditCardPayment`: Handles credit card payments.
  - `PayPalPayment`: Handles PayPal payments.
  - `BankTransferPayment`: Handles bank transfer payments.

- **Polymorphism**:
  - The `process_payment()` method is overridden in each derived class to provide specific behavior for different payment methods.

- **Utility Function**:
  - `execute_payments()`: Iterates through a list of payment objects and calls their `process_payment()` method, demonstrating polymorphism.

---

## Installation

No external dependencies are required. Ensure you have Python 3.x installed.

---

## Usage

1. Clone or download the repository.
2. Open the Python file in your IDE or text editor.
3. Run the script to execute payment processing.

### Example Output

The script creates instances of different payment types and processes them. Here is an example output:

```plaintext
Processing credit card payment of 1000.
Processing PayPal payment of 500.
Processing bank transfer payment of 200.
