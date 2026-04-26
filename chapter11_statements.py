# IT 533 - Chapter 11 Assignment
# Author: Umer Khatab
# Description: This file demonstrates different statement forms from
# Chapter 11 of Learning Python (5th Edition) by Mark Lutz. The examples
# cover different assignment statement forms (Table 11-1), an expression
# statement, and a print statement (Table 11-4), each adapted to a
# real-world scenario.


# ----------------------------------------------------------
# Example 1: Basic Assignment Statement (Table 11-1)
# Scenario: I work at a small coffee shop and I need to store
# the price of a regular coffee in a variable so I can use it
# later when I calculate customer totals at the register.
# ----------------------------------------------------------
coffee_price = 3.50


# ----------------------------------------------------------
# Example 2: Tuple Assignment / Sequence Assignment (Table 11-1)
# Scenario: I am processing a new customer record and I have
# their first name and last name together. Instead of writing
# two separate assignments, I can unpack both values at once
# using a tuple assignment.
# ----------------------------------------------------------
first_name, last_name = "Umer", "Khatab"


# ----------------------------------------------------------
# Example 3: Multiple-Target Assignment (Table 11-1)
# Scenario: My company is hiring three new employees and they
# are all starting at the same base salary. Instead of writing
# the same value three times, I can assign it to all three
# variables in a single line.
# ----------------------------------------------------------
emp1_salary = emp2_salary = emp3_salary = 35000


# ----------------------------------------------------------
# Example 4: Augmented Assignment Statement (Table 11-1)
# Scenario: I am keeping track of how many customers come into
# the coffee shop each day. Every time a new customer walks
# in, I want to add 1 to the customer counter without rewriting
# the whole expression.
# ----------------------------------------------------------
customer_count = 10
customer_count += 1   # A new customer just walked in


# ----------------------------------------------------------
# Example 5: Expression Statement (method call)
# Scenario: I keep a shopping list for the coffee shop, and I
# just realized we are running low on milk. I want to add
# "milk" to my existing list. Calling the append() method is
# an expression statement because the value it returns is not
# saved into a variable.
# ----------------------------------------------------------
shopping_list = ["bread", "eggs", "butter"]
shopping_list.append("milk")


# ----------------------------------------------------------
# Example 6: Print Statement (Table 11-4: sep and end keywords)
# Scenario: At the end of the day, I want to print a clean
# summary report for the manager. I use the sep keyword to
# control how values are separated, and the end keyword to
# control what is printed at the end of each line.
# ----------------------------------------------------------
print("===== Daily Coffee Shop Summary =====")
print("Employee:", first_name, last_name, sep=" ")
print("Coffee Price: $", coffee_price, sep="", end="\n")
print("Customers Today:", customer_count)
print("Shopping List:", shopping_list)
