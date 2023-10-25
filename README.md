# Employee Database Management System
This is a simple Python program for managing an employee database using the tkinter library for the GUI and SQLite for the database. The program allows you to add, view, update, and delete employee information.

## Table of Contents

- [Introduction](#employee-database-management-system)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Features](#features)
- [Code Explanation](#code-explanation)
- [License](#license)

## Prerequisites

Before using this program, make sure you have the following prerequisites installed:

- Python: You need to have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/).


## Usage

The following are features of the program:

- **Add New Employee:** Click the "Add New" button to enter the details of a new employee, including their name, age, salary, department, location, education level, and year of passing.

- **View Employee:** Click the "View" button to search for an employee by their ID. You can view their details, update their information, or delete their record.

- **Update Employee:** If you want to update an employee's information, select the "Update" button after viewing their details.

- **Delete Employee:** To delete an employee's record, click the "Delete" button after viewing their details.

- **Close:** Use the "Close" button to exit the program.

## Features

- Add new employees to the database.
- View employee details, including their name, age, salary, department, location, education level, and year of passing.
- Update employee information.
- Delete employee records.
- Error handling for non-existing employee IDs and duplicate employee IDs.
- GUI for easy interaction.

## Code Explanation

#### Import necessary libraries:
```python
import tkinter as tk
import sqlite3
```
- Imports the Tkinter library for creating the graphical user interface.
- Imports the SQLite library for working with a SQLite database.

#### Initialize a global SQLite database connection and cursor:
```python
def creation():
    global conn, cursor
    conn = sqlite3.connect("employee.sqlite")
    cursor = conn.cursor()
```
- The `creation()` function creates a connection to the SQLite database file named "employee.sqlite" and initializes a cursor to execute SQL queries.

#### Check if database tables exist:
```python
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
if ('Departments',) not in tables:
    cursor.execute("CREATE TABLE Departments ...")
if ('Location',) not in tables:
    cursor.execute("CREATE TABLE Location ...")
if ('Employee',) not in tables:
    cursor.execute("CREATE TABLE Employee ...")
if ('Education',) not in tables:
    cursor.execute("CREATE TABLE Education ...")
```
- The code checks if four database tables exist: 'Departments', 'Location', 'Employee', and 'Education'. If any of these tables don't exist, it creates them using SQL statements.

#### Enable foreign key constraints:
```python
cursor.execute("PRAGMA foreign_keys = ON")
```
- This line enables foreign key constraints in SQLite, which are used to maintain referential integrity between tables.

#### Define the main function:
```python
def main():
    # Initialize the main application window using Tkinter.
    # Provides options to add new employees, view employee information, and close the application.
```
- The `main()` function initializes the main application window using Tkinter. It provides options to add new employees, view employee information, and close the application.

#### Close the database connection:
```python
def close():
    # Close the database connection and cursor when the user decides to close the application.
```
- The `close()` function is used to close the database connection and cursor when the user decides to close the application.

#### View employee information:
```python
def viewEmployee():
    # Creates a window for viewing employee information.
    # Allows users to input an employee ID and view the corresponding employee's details.
```
- The `viewEmployee()` function creates a window for viewing employee information. It allows users to input an employee ID and view the corresponding employee's details.

#### View employee information (continued):
```python
def view_info():
    # Displays the employee's details when the user enters a valid employee ID.
    # If the employee ID doesn't exist, provides options to add a new employee with that ID, return to the main menu, or close the window.
```
- The `view_info()` function is called to display the employee's details when the user enters a valid employee ID. If the employee ID doesn't exist, the program provides options to add a new employee with that ID, return to the main menu, or close the window.

#### Update employee information:
```python
def update():
    # Creates a window for updating employee information.
    # Displays the current employee details and allows users to input new information.
```
- The `update()` function creates a window for updating employee information. It displays the current employee details and allows users to input new information.

#### Update employee information (continued):
```python
def update_confirm():
    # Confirms and saves the updates made to an employee's information.
    # Returns to the view window with the updated details.
```
- The `update_confirm()` function is called to confirm and save the updates made to an employee's information. It also returns to the view window with the updated details.

#### Delete an employee record:
```python
def delete():
    # Deletes an employee's record when the user selects the "Delete" option.
    # Then returns to the main menu.
```
- The `delete()` function deletes an employee's record when the user selects the "Delete" option. It then returns to the main menu.

#### Insert a new employee:
```python
def insertEmployee():
    # Creates a window for adding a new employee.
    # Provides input fields for various employee details like name, age, salary, department, and location.
    # Allows users to add education details (degree and year of passing).
```
- The `insertEmployee()` function creates a window for adding a new employee. It provides input fields for various employee details like name, age, salary, department, and location. Additionally, it allows users to add education details (degree and year of passing).

#### Insert education details:
```python
def insert_education():
    # Used to insert education details into the database when the "Add Education" button is clicked.
```
- The `insert_education()` function is used to insert education details into the database when the "Add Education" button is clicked.

#### Insert a new employee (continued):
```python
def insert_record():
    # Inserts a new employee record into the database when the "Add Employee" button is clicked.
    # After insertion, it clears the input fields.
```
- The `insert_record()` function inserts a new employee record into the database when the "Add Employee" button is clicked. After insertion, it clears the input fields.

#### Running the main function:
```python
if __name__ == '__main__':
    # Runs the main() function to start the application.
```
- Finally, the program runs the `main()` function to start the application.


## License

This program is licensed under the MIT License - see the [LICENSE](https://github.com/DarkKnight714/EmployeeDatabaseManagementApplication-with-Tkinter/blob/main/LICENSE) file for details.


Enjoy managing your employee database! If you encounter any issues or have questions, feel free to reach out.
