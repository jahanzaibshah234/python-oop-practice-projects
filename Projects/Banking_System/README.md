# Banking System (Inheritance & Polymorphism)

## Concepts Covered
- Inheritance
- Method Overriding (Polymorphism)
- Reuse of Parent Class Methods

## Project Description

This project implements a simple Banking System to help learners understand the concepts of inheritance and polymorphism in Object-Oriented Programming (OOP) using Python. The system features a base account class and two specialized account types with unique behaviors.

### Features

- **Base Class: Account**
  - **Attributes:**
    - `account_number` (Account number)
    - `holder_name` (Account holder's name)
    - `balance` (Current balance)
  - **Methods:**
    - `deposit(amount)` — Add funds to the account
    - `withdraw(amount)` — Withdraw funds from the account
    - `display_info()` — Display account details

- **Child Class: SavingsAccount**
  - Inherits from `Account`
  - **Extra Attribute:**
    - `interest_rate` (Interest rate for the savings account)
  - **Method:**
    - `apply_interest()` — Add interest to the account balance

- **Child Class: CurrentAccount**
  - Inherits from `Account`
  - **Extra Attribute:**
    - `overdraft_limit` (Allowed overdraft limit)
  - **Overridden Method:**
    - `withdraw(amount)` — Withdraw funds, allowing overdraft within the limit

### What You'll Learn

- How to use inheritance to extend base functionality
- How to override methods to implement polymorphic behavior
- How to reuse parent class methods in child classes

---

Use this project to practice OOP principles such as inheritance and polymorphism, and to understand how different account types can share and customize behavior!
