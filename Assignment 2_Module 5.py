# code sourced inspired by https://youtu.be/7w7ITwOgUAE?si=uSqkJzyLGj7IXyhd, a simple expense tracker using tkinter for the GUI
# matpotlib for the pie chart to compare expenses and panda for data visualization.

import tkinter as tk  # Import the tkinter module with an alias tk
from tkinter import ttk  # Import themed tkinter widgets
from tkinter import messagebox  # Import messagebox for displaying messages
import matplotlib.pyplot as plt  # Import matplotlib for data visualization
from collections import defaultdict  # Import defaultdict for handling default values in dictionaries
import pandas as pd  # Import pandas for data manipulation and analysis


class ExpenseTrackerApp:  # Define a class named ExpenseTrackerApp
    def __init__(self, root):  # Define the initialization method with root as a parameter
        self.root = root  # Assign the root window to an instance variable
        self.root.title("Expense Tracker")  # Set the title of the root window
        self.root.geometry("600x400")  # Set the size of the root window

        self.expense_categories = ['Food', 'Transportation', 'Housing', 'Utilities', 'Entertainment', 'Healthcare', 'Others']  # Define expense categories
        self.expense_data = defaultdict(int)  # Initialize a defaultdict to store expense data with default value 0

        self.create_gui()  # Call the method to create the GUI

    def create_gui(self):  # Define a method to create the GUI
        # Create label and dropdown for selecting expense category
        self.category_label = ttk.Label(self.root, text="Select Category:")  # Create a label widget
        self.category_label.grid(row=0, column=0, padx=10, pady=10)  # Place the label using grid layout manager
        self.category_var = tk.StringVar()  # Create a StringVar to store the selected category
        self.category_dropdown = ttk.Combobox(self.root, values=self.expense_categories, textvariable=self.category_var)  # Create a dropdown widget
        self.category_dropdown.grid(row=0, column=1, padx=10, pady=10)  # Place the dropdown using grid layout manager

        # Create label and entry for entering expense amount
        self.amount_label = ttk.Label(self.root, text="Enter Amount:")  # Create a label widget
        self.amount_label.grid(row=1, column=0, padx=10, pady=10)  # Place the label using grid layout manager
        self.amount_var = tk.StringVar()  # Create a StringVar to store the entered amount
        self.amount_entry = ttk.Entry(self.root, textvariable=self.amount_var)  # Create an entry widget
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)  # Place the entry using grid layout manager

        # Create button to add expense
        self.add_button = ttk.Button(self.root, text="Add Expense", command=self.add_expense)  # Create a button widget
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  # Place the button using grid layout manager

        # Create button to show expense chart
        self.show_chart_button = ttk.Button(self.root, text="Show Chart", command=self.show_chart)  # Create a button widget
        self.show_chart_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)  # Place the button using grid layout manager

        # I also had to add a button to save the file as an excel, I just copied the other buttons and updated it to
        # Save Report
        self.save_button = ttk.Button(self.root, text="Save Report", command=self.save_report)  # Create a button widget
        self.save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)  # Place the button using grid layout manager

        # Create button to close the application
        self.close_button = ttk.Button(self.root, text="Close", command=self.root.destroy)  # Create a button widget
        self.close_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)  # Place the button using grid layout manager

    def add_expense(self):  # Define a method to add expense
        category = self.category_var.get()  # Get the selected category
        amount = self.amount_var.get()  # Get the entered amount
        if category and amount:  # Check if both category and amount are entered
            self.expense_data[category] += float(amount)  # Add the expense to the corresponding category
            messagebox.showinfo("Success", "Expense added successfully!")  # Show a success message
            self.amount_var.set("")  # Clear the amount entry field
        else:
            messagebox.showerror("Error", "Please select a category and enter the amount.")  # Show an error message if category or amount is missing

    def show_chart(self):  # Define a method to show expense chart
        categories = []  # Create an empty list to store categories
        amounts = []  # Create an empty list to store amounts
        for category, amount in self.expense_data.items():  # Iterate through expense data
            if amount > 0:  # Check if the amount is greater than zero
                categories.append(category)  # Add the category to the list
                amounts.append(amount)  # Add the amount to the list

        if categories:  # Check if there are categories with non-zero amounts
            plt.figure(figsize=(8, 6))  # Create a new figure for the chart
            plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)  # Plot a pie chart
            plt.axis('equal')  # Set the aspect ratio to be equal
            plt.title('Monthly Expenses')  # Set the title of the chart
            plt.show()  # Show the chart
        else:
            messagebox.showwarning("Warning", "No expenses recorded to show chart.")  # Show a warning message if no expenses are recorded

# I added this function to save expense report as Excel file, I just looked up how to save inputs as Excel files
# in python. save_report is defined and earlier I created a button to execute the function.
    def save_report(self):  # Define a method to save expense report
        df = pd.DataFrame(list(self.expense_data.items()), columns=['Category', 'Amount'])  # Create a DataFrame from expense data
        file_path = "expense_report.xlsx"  # Define the file path for the report
        df.to_excel(file_path, index=False)  # Save the DataFrame as an Excel file
        messagebox.showinfo("Report Saved", f"Expense report saved successfully as {file_path}")  # Show a message confirming report saving

if __name__ == "__main__":  # Check if the script is executed directly
    root = tk.Tk()  # Create the root window
    app = ExpenseTrackerApp(root)  # Create an instance of ExpenseTrackerApp
    root.mainloop()  # Start the main event loop