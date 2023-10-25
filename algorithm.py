import tkinter as tk
import sqlite3

# Initialize a global SQLite database connection and cursor
def creation():
    global cnt
    cnt=sqlite3.connect("employee.sqlite")
    global cursor
    cursor = cnt.cursor()
    cursor.execute(f"PRAGMA table_info({'Departments'})")
    result1 = cursor.fetchall()

    cursor.execute(f"PRAGMA table_info({'Location'})")
    result2 = cursor.fetchall()

    cursor.execute(f"PRAGMA table_info({'Employee'})")
    result3 = cursor.fetchall()

    cursor.execute(f"PRAGMA table_info({'Education'})")
    result4 = cursor.fetchall()

    cursor.execute(f"PRAGMA foreign_keys = ON")

    if len(result1) == 0:
        cnt.execute('''CREATE TABLE Departments(DeptID INTEGER PRIMARY KEY, [Department Name] Text);''')
    if len(result2) == 0:
        cnt.execute('''CREATE TABLE Location(LocID Integer PRIMARY KEY, Location Text);''')
    if len(result3) == 0:
        cnt.execute('''CREATE TABLE Employee(EmpID Integer PRIMARY KEY ,Name Text, Age Integer, Salary Real, DeptID Integer,LocID Integer, FOREIGN KEY(DeptID) REFERENCES Departments(DeptID),FOREIGN KEY(LocID) REFERENCES Location(LocID) );''')  
    if len(result4) == 0:
        cnt.execute('''CREATE TABLE Education(EmpID Integer, [Education Level] Text, [Year of Passing] Integer,FOREIGN KEY(EmpID) REFERENCES Employee(EmpID) );''')

# Function to close gui and close cursor and connection
def close(window):
    window.destroy()
    cursor.close()
    cnt.close()

# Main function to initialize the application
def main():
    creation()

    try: 
        view_window_error.destroy()
    except:
        try:
            view_window2.destroy()
        except:pass

    # Set the window dimensions and position it in the center of the screen
    main_window = tk.Tk()
    main_window.title("Employee Database")
    window_width = 300
    window_height = 100
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    
    # Create buttons for different actions
    insert_button = tk.Button(main_window, text="Add New", command =lambda: insertEmployee(main_window))
    view_button = tk.Button(main_window, text="View", command = lambda: viewEmployee(main_window))
    close_button = tk.Button(main_window, text="Close", command = lambda: close(main_window))

    # Pack the buttons
    insert_button.pack()
    view_button.pack()
    close_button.pack()

    main_window.mainloop()



# Function to insert a new employee
# Part 1: get Emp ID 
def insertEmployee(window):
    # Destroy the main window
    window.destroy()

    # Create a new window
    new_entry_window = tk.Tk()
    new_entry_window.title("Enter Employee Information")

    # Set the window dimensions and position it in the center of the screen
    window_width = 300
    window_height = 100
    screen_width = new_entry_window.winfo_screenwidth()
    screen_height = new_entry_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    new_entry_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  
    
    # Create a label to describe the input field
    label_input = tk.Label(new_entry_window, text="Enter Employee ID to be added")
    label_input.pack()
    
    entry = tk.Entry(new_entry_window)
    entry.pack()
    # Add contents to the new window
    button = tk.Button(new_entry_window, text="Update Info", command = lambda:insert(entry,new_entry_window))
    button.pack()


# Part 2: take info and if already exist option to view, return to menu and close
def insert(entry, window):
    id =entry.get()
    # Checking if the Emp ID already exists
    cursor.execute("SELECT COUNT(*) FROM Employee WHERE EmpID = ?", (id,))
    res = cursor.fetchone()[0]

    if res != 0:
        # Emp Id already exists
        window.destroy()
        global view_window_error
        view_window_error = tk.Tk()
        view_window_error.title("Error")

        # Set the window dimensions and position it in the center of the screen
        window_width = 300
        window_height = 120
        screen_width = view_window_error.winfo_screenwidth()
        screen_height = view_window_error.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        view_window_error.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}") 
    
        # Create a label
        label_input = tk.Label(view_window_error, text="Entered Employee ID already exists in the database", fg="red")
        label_input.pack()     

        # Buttons for viewing, returning back to main menu and close 
        view_button = tk.Button(view_window_error, text="View the info", command = lambda:view_info(id,view_window_error))
        return_button = tk.Button(view_window_error, text="Return", command = main)
        close_button = tk.Button(view_window_error, text="Close", command = lambda: close(view_window_error))

        view_button.pack() 
        return_button.pack() 
        close_button.pack() 

    else:
        # Create a new window 
        window.destroy()
        view_window = tk.Tk()
        view_window.title("Insert Employee Information")
    
        # Set the window dimensions and position it in the center of the screen
        window_width = 300
        window_height = 360
        screen_width = view_window.winfo_screenwidth()
        screen_height = view_window.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        view_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}") 

        # Labels and input fields for employee details
        table_label = tk.Label(view_window, text="Input Data(Input is Case Sensitive) ")
        table_label.pack()

        entry_name_label = tk.Label(view_window, text="Name:")
        entry_name_label.pack()
        entry_name = tk.Entry(view_window)
        entry_name.pack()
 
        entry_age_label = tk.Label(view_window, text="Age:")
        entry_age_label.pack()
        entry_age = tk.Entry(view_window)
        entry_age.pack()

        entry_sal_label = tk.Label(view_window, text="Sal:")
        entry_sal_label.pack()
        entry_sal = tk.Entry(view_window)
        entry_sal.pack()

        entry_dep_label = tk.Label(view_window, text="Department:")
        entry_dep_label.pack()
        entry_dep = tk.Entry(view_window)
        entry_dep.pack()

        entry_loc_label = tk.Label(view_window, text="Location:")
        entry_loc_label.pack()
        entry_loc = tk.Entry(view_window)
        entry_loc.pack()

        entry_edulvl_label = tk.Label(view_window, text="Education Level:")
        entry_edulvl_label.pack()
        entry_edulvl = tk.Entry(view_window)
        entry_edulvl.pack()

        entry_yr_label = tk.Label(view_window, text="Year of passing:")
        entry_yr_label.pack()
        entry_yr = tk.Entry(view_window)
        entry_yr.pack()
   
        # Button to insert info
        button = tk.Button(view_window, text="Insert Info", command = lambda:insert_info(id,view_window, entry_name, entry_sal, entry_age, entry_dep, entry_loc, entry_edulvl, entry_yr))
        button.pack()

# Part 3: inserting info into db from fn insert_info() in Part 2.1.2




# Function to view employee details
# Part 1:get Emp ID 
def viewEmployee(main_window):
    # Destroy the main window
    main_window.destroy()

    # Create new window for id input
    view_window = tk.Tk()
    view_window.title("View Employee Information")

    # Set the window dimensions and position it in the center of the screen
    window_width = 300
    window_height = 100
    screen_width = view_window.winfo_screenwidth()
    screen_height = view_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    view_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  

    # Create a label to describe the input field
    label_input = tk.Label(view_window, text="Enter Employee ID whose data is to be displayed")
    label_input.pack()
    
    entry = tk.Entry(view_window)
    entry.pack()

    # Add a button to view the information
    button = tk.Button(view_window, text="View", command=lambda:view_info(entry,view_window))
    button.pack()

# Part 2: display information with option to update, delete, return to menu, close and if doesn't exist option to add, return to menu and close
def view_info(entry,view_window):
    try: 
        id = entry.get()
    except: id =entry

    # Check if the employee ID exists
    cursor.execute("SELECT COUNT(*) FROM Employee WHERE EmpID = ?", (id,))
    res = cursor.fetchone()[0]

    if res == 0:
        view_window.destroy()
        global view_window_error
        view_window_error = tk.Tk()
        view_window_error.title("Error")

        # Set the window dimensions and position it in the center of the screen
        window_width = 300
        window_height = 120
        screen_width = view_window_error.winfo_screenwidth()
        screen_height = view_window_error.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        view_window_error.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  

        # Create an error message label
        label_input = tk.Label(view_window_error, text="Entered Employee ID doesn't exists in the database", fg="red")
        label_input.pack()  

        # Create buttons to add as a new employee, return to the main menu, or close the window
        new_button = tk.Button(view_window_error, text="Add as new", command = lambda:insert_employee(id))
        return_button = tk.Button(view_window_error, text="Return", command = main)
        close_button = tk.Button(view_window_error, text="Close", command = lambda: close(view_window_error))

        new_button.pack() 
        return_button.pack() 
        close_button.pack() 

    else:
        # Employee ID exists, show their details
        view_window.destroy()
        global view_window2
        view_window2 = tk.Tk()
        view_window2.title("Employee Data")

        # Set the window dimensions and position it in the center of the screen       
        window_width = 300
        window_height = 280
        screen_width = view_window2.winfo_screenwidth()
        screen_height = view_window2.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        view_window2.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Retrieve employee details
        cursor.execute("SELECT * FROM Employee WHERE EmpID = ?", (id,))
        existing_info = cursor.fetchone()

        # Create labels to display employee information    
        existing_id_label = tk.Label(view_window2, text="ID: " +str( existing_info[0]))
        existing_id_label.pack()
        
        existing_name_label = tk.Label(view_window2, text="Name: " + existing_info[1])
        existing_name_label.pack()

        existing_age_label = tk.Label(view_window2, text="Age: " + str(existing_info[2]))
        existing_age_label.pack()

        existing_salary_label = tk.Label(view_window2, text="Salary: " + str(existing_info[3]))
        existing_salary_label.pack()

        cursor.execute("SELECT [Department Name] FROM Departments WHERE DeptID = ?", (existing_info[4],))
        existing_dep_info = cursor.fetchone()
        existing_dep_label = tk.Label(view_window2, text="Department: " + existing_dep_info[0])
        existing_dep_label.pack()

        cursor.execute("SELECT Location FROM Location WHERE LocID = ?", (existing_info[5],))
        existing_loc_info = cursor.fetchone()
        existing_loc_label = tk.Label(view_window2, text="Location: " + existing_loc_info[0])
        existing_loc_label.pack()

        cursor.execute("SELECT [Education Level], [Year of Passing] FROM Education WHERE EmpID = ?", (id,))
        existing_edu_info = cursor.fetchone()
        existing_edu_label = tk.Label(view_window2, text="Education Level: " + existing_edu_info[0])
        existing_edu_label.pack()

        existing_yrop_label = tk.Label(view_window2, text="Yr of Passing: " + str(existing_edu_info[1]))
        existing_yrop_label.pack()
        
        # Add an option to update employee information
        update_button = tk.Button(view_window2, text="Update", command = lambda: update_emp(id))
        update_button.pack() 

        # Add an option to delete employee information
        delete_button = tk.Button(view_window2, text="Delete", command = lambda:confirm_del(id,view_window2))
        delete_button.pack()   

        # Add a button to return to the main menu
        return_button = tk.Button(view_window2, text="Return", command = main)
        return_button.pack() 

        # Add a button to close
        close_button = tk.Button(view_window2, text="Close", command = lambda: close(view_window2))
        close_button.pack() 



# Function to insert employee details
# Part 2.1.1 Taking info for inserting info
def insert_employee(id):
    view_window_error.destroy()

    # Create a new window 
    insert_window = tk.Tk()
    insert_window.title("Insert Employee Information")

    # Set the window dimensions and position it in the center of the screen
    window_width = 300
    window_height = 380
    screen_width = insert_window.winfo_screenwidth()
    screen_height = insert_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    insert_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  

    # Labels and input fields
    table_label = tk.Label(insert_window, text="Input Data (Input is Case Sensitive)")
    table_label.pack()

    entry_name_label = tk.Label(insert_window, text="Name:")
    entry_name_label.pack()
    entry_name = tk.Entry(insert_window)
    entry_name.pack()
 
    entry_age_label = tk.Label(insert_window, text="Age:")
    entry_age_label.pack()
    entry_age = tk.Entry(insert_window)
    entry_age.pack()

    entry_sal_label = tk.Label(insert_window, text="Sal:")
    entry_sal_label.pack()
    entry_sal = tk.Entry(insert_window)
    entry_sal.pack()

    entry_dep_label = tk.Label(insert_window, text="Department:")
    entry_dep_label.pack()
    entry_dep = tk.Entry(insert_window)
    entry_dep.pack()

    entry_loc_label = tk.Label(insert_window, text="Location:")
    entry_loc_label.pack()
    entry_loc = tk.Entry(insert_window)
    entry_loc.pack()

    entry_edulvl_label = tk.Label(insert_window, text="Education Level:")
    entry_edulvl_label.pack()
    entry_edulvl = tk.Entry(insert_window)
    entry_edulvl.pack()

    entry_yr_label = tk.Label(insert_window, text="Year of passing:")
    entry_yr_label.pack()
    entry_yr = tk.Entry(insert_window)
    entry_yr.pack()
   
    # Add contents to the new window
    button = tk.Button(insert_window, text="Insert Info", command = lambda:insert_info(id,insert_window, entry_name, entry_sal, entry_age, entry_dep, entry_loc, entry_edulvl, entry_yr))
    button.pack()

# Part 2.1.2 Inserting info into the database
def insert_info(id,insert_window, entry_name, entry_sal, entry_age, entry_dep, entry_loc, entry_edulvl, entry_yr):
    name_value = entry_name.get()
    age_value = entry_age.get()
    sal_value = entry_sal.get()
    dep_value = entry_dep.get()
    loc_value = entry_loc.get()
    edulevel_value = entry_edulvl.get()
    yrofpass_value = entry_yr.get()

    cursor.execute("Select DeptID From Departments WHERE [Department Name] = ?", (dep_value,))
    result = cursor.fetchall()
    if len(result) == 0:
        cursor.execute("Insert into Departments([Department Name]) Values(?)", (dep_value,))
        cursor.execute("Select * From Departments WHERE [Department Name] = ?", (dep_value,))
        result = cursor.fetchone()[0]
    else:
        cursor.execute("Select * From Departments WHERE [Department Name] = ?", (dep_value,))
        result = cursor.fetchone()[0]

    cursor.execute("Select LocID From Location WHERE Location = ?", (loc_value,))
    result2 = cursor.fetchall()
    if len(result2) == 0:
        cursor.execute("Insert into Location([Location]) Values(?)", (loc_value,))
        cursor.execute("Select LocID From Location WHERE Location = ?", (loc_value,))
        result2 = cursor.fetchone()[0]
    else:
        cursor.execute("Select * From Location WHERE Location = ?", (loc_value,))
        result2 = cursor.fetchone()[0]
 

    cursor.execute("Insert into Employee(EmpID, Name, Age, Salary, DeptID, LocID) Values(?,?,?,?,?,?)", (id,name_value,age_value,sal_value,result,result2))
    cursor.execute("Insert into Education(EmpID, [Education Level], [Year of Passing]) Values(?,?,?)", (id,edulevel_value,yrofpass_value))

    cnt.commit()
    view_info(id,insert_window)
# after executing moves into view for displaying the recently inserted info



# Function to update employee details
# Part 2.2.1 Taking info for updating info
def update_emp(id):
    # Destroy the main window
    view_window2.destroy()

    # Create update window 
    update_window = tk.Tk()
    update_window.title("Update Employee Information (Input is Case Sensitive)")

    window_width = 480
    window_height = 220
    screen_width = update_window.winfo_screenwidth()
    screen_height = update_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    update_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  

    # Create labels to describe the input field and show current info
    table_label = tk.Label(update_window, text="Only input data to be changed ")
    table_label.grid(row=0,column=0)

    cursor.execute("SELECT * FROM Employee WHERE EmpID = ?", (id,))
    existing_info = cursor.fetchone()

    cursor.execute("SELECT [Department Name] FROM Departments WHERE DeptID = ?", (existing_info[4],))
    existing_dep_info = cursor.fetchone()

    cursor.execute("SELECT Location FROM Location WHERE LocID = ?", (existing_info[5],))
    existing_loc_info = cursor.fetchone()

    cursor.execute("SELECT [Education Level], [Year of Passing] FROM Education WHERE EmpID = ?", (id,))
    existing_edu_info = cursor.fetchone()


    existing_id_label = tk.Label(update_window, text="ID: " +str( existing_info[0]))
    existing_id_label.grid(row=1,column=1)    
    
    existing_name_label = tk.Label(update_window, text="Name: " + existing_info[1])
    existing_name_label.grid(row=2,column=0)  
    
    entry1_label = tk.Label(update_window, text="Name:")
    entry1_label.grid(row=2,column=1)  
    entry1 = tk.Entry(update_window)
    entry1.grid(row=2,column=3)  

    existing_age_label = tk.Label(update_window, text="Age: " + str(existing_info[2]))
    existing_age_label.grid(row=4,column=0)  

    entry2_label = tk.Label(update_window, text="Age:")
    entry2_label.grid(row=4,column=1)  
    entry2 = tk.Entry(update_window)
    entry2.grid(row=4,column=3)  

    existing_salary_label = tk.Label(update_window, text="Salary: " + str(existing_info[3]))
    existing_salary_label.grid(row=6,column=0)  
 
    entry3_label = tk.Label(update_window, text="Salary:")
    entry3_label.grid(row=6,column=1)  
    entry3 = tk.Entry(update_window)
    entry3.grid(row=6,column=3)  

    existing_dep_label = tk.Label(update_window, text="Department: " + existing_dep_info[0])
    existing_dep_label.grid(row=8,column=0)  
    
    entry4_label = tk.Label(update_window, text="Department:")
    entry4_label.grid(row=8,column=1)  
    entry4 = tk.Entry(update_window)
    entry4.grid(row=8,column=3)  

    existing_loc_label = tk.Label(update_window, text="Location: " + existing_loc_info[0])
    existing_loc_label.grid(row=10,column=0)  

    entry5_label = tk.Label(update_window, text="Location:")
    entry5_label.grid(row=10,column=1)  
    entry5 = tk.Entry(update_window)
    entry5.grid(row=10,column=3)  

    existing_edu_label = tk.Label(update_window, text="Education Level: " + existing_edu_info[0])
    existing_edu_label.grid(row=12,column=0)  
        
    entry6_label = tk.Label(update_window, text="Education Level:")
    entry6_label.grid(row=12,column=1)  
    entry6 = tk.Entry(update_window)
    entry6.grid(row=12,column=3)  

    existing_yrop_label = tk.Label(update_window, text="Yr of Passing: " + str(existing_edu_info[1]))
    existing_yrop_label.grid(row=14,column=0)  
    
    entry7_label = tk.Label(update_window, text="Year of passing:")
    entry7_label.grid(row=14,column=1)  
    entry7 = tk.Entry(update_window)
    entry7.grid(row=14,column=3)  


    # Add contents to the new window
    button = tk.Button(update_window, text="Update Info", command = lambda:updating_view(id,entry1, entry2, entry3, entry4, entry5, entry6, entry7,update_window))
    button.grid(row=16,column=1) 

# Part 2.2.2 Updating info into the database
def updating_view(id,entry1, entry2, entry3, entry4, entry5, entry6, entry7,view_window):
    name_value = entry1.get()
    age_value = entry2.get()
    sal_value = entry3.get()
    dep_value = entry4.get()
    loc_value = entry5.get()
    edulevel_value = entry6.get()
    yrofpass_value = entry7.get()

    if len(name_value) !=0:
        cursor.execute("Update Employee SET Name = ? WHERE EmpID = ?", (name_value, id))
    if len(age_value) !=0:
        cursor.execute("Update Employee SET Age = ? WHERE EmpID = ?", (age_value, id))
    if len(sal_value) !=0:    
        cursor.execute("Update Employee SET Salary = ? WHERE EmpID = ?", (sal_value, id))
    if len(edulevel_value) !=0:     
        cursor.execute("Update Education SET [Education Level] = ? WHERE EmpID = ?", (edulevel_value, id))
    if len(yrofpass_value) !=0:  
        cursor.execute("Update Education SET [Year of Passing] = ? WHERE EmpID = ?", (yrofpass_value, id))
    if len(dep_value) !=0:
        cursor.execute("Select DeptID From Departments WHERE [Department Name] = ?", (dep_value,))
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute("Insert into Departments([Department Name]) Values(?)", (dep_value,))
            cursor.execute("Select * From Departments WHERE [Department Name] = ?", (dep_value,))
            result = cursor.fetchone()[0]
        else:
            cursor.execute("Select * From Departments WHERE [Department Name] = ?", (dep_value,))
            result = cursor.fetchone()[0]
        update_query = "UPDATE Employee SET DeptID = ? WHERE EmpID = ?"
        cursor.execute(update_query, (result, id))

    if len(loc_value) !=0:
        cursor.execute("Select LocID From Location WHERE Location = ?", (loc_value,))
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute("Insert into Location([Location]) Values(?)", (loc_value,))
            cursor.execute("Select LocID From Location WHERE Location = ?", (loc_value,))
            result = cursor.fetchone()[0]
        else:
            cursor.execute("Select * From Location WHERE Location = ?", (loc_value,))
            result = cursor.fetchone()[0]
        update_query = "UPDATE Employee SET LocID = ? WHERE EmpID = ?"
        cursor.execute(update_query, (result, id))

    cnt.commit()
    view_info(id,view_window)



# Function to delete employee details
# Part 2.3.1 Confirming if user wants to really delete the information
def confirm_del(id,window):

    window.destroy()

    view_window2 = tk.Tk()
    view_window2.title("Employee Data")
    
    # Set the window dimensions and position it in the center of the screen
    window_width = 480
    window_height = 220
    screen_width = view_window2.winfo_screenwidth()
    screen_height = view_window2.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    view_window2.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}") 

    confirm_label = tk.Label(view_window2, text=" Confirm Deleting this Employee Entry", fg="red")
    confirm_label.pack()
    cursor.execute("SELECT * FROM Employee WHERE EmpID = ?", (id,))
    existing_info = cursor.fetchone()
        
    existing_id_label = tk.Label(view_window2, text="ID: " +str( existing_info[0]))
    existing_id_label.pack()
        
    existing_name_label = tk.Label(view_window2, text="Name: " + existing_info[1])
    existing_name_label.pack()

    existing_age_label = tk.Label(view_window2, text="Age: " + str(existing_info[2]))
    existing_age_label.pack()

    existing_salary_label = tk.Label(view_window2, text="Salary: " + str(existing_info[3]))
    existing_salary_label.pack()

    cursor.execute("SELECT [Department Name] FROM Departments WHERE DeptID = ?", (existing_info[4],))
    existing_dep_info = cursor.fetchone()
    existing_dep_label = tk.Label(view_window2, text="Department: " + existing_dep_info[0])
    existing_dep_label.pack()

    cursor.execute("SELECT Location FROM Location WHERE LocID = ?", (existing_info[5],))
    existing_loc_info = cursor.fetchone()
    existing_loc_label = tk.Label(view_window2, text="Location: " + existing_loc_info[0])
    existing_loc_label.pack()

    cursor.execute("SELECT [Education Level], [Year of Passing] FROM Education WHERE EmpID = ?", (id,))
    existing_edu_info = cursor.fetchone()
    existing_edu_label = tk.Label(view_window2, text="Education Level: " + existing_edu_info[0])
    existing_edu_label.pack()

    existing_yrop_label = tk.Label(view_window2, text="Yr of Passing: " + str(existing_edu_info[1]))
    existing_yrop_label.pack()


    delete_button = tk.Button(view_window2, text="Delete", command = lambda:delete_emp(id,view_window2))
    delete_button.pack()   

# Part 2.3.2 Deleting the info
def delete_emp(id,window):
    cursor.execute("SELECT COUNT(*) FROM Employee WHERE EmpID = ?", (id,))
    res = cursor.fetchone()[0]

    if res != 0:
        cnt.execute("BEGIN")
        cnt.execute("DELETE FROM Education WHERE EmpID = ?", (id,))
        cnt.execute("DELETE FROM Employee WHERE EmpID = ?", (id,))
        cnt.commit()
    window.destroy()
    main()
