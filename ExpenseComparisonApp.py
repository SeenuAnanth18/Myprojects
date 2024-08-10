import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Dictionary to store monthly expenses
monthly_expenses = {}

def calculate_expenses():
    # Get values from the entry widgets
    rent = float(entry_rent.get())
    groceries = float(entry_groceries.get())
    utilities = float(entry_utilities.get())
    entertainment = float(entry_entertainment.get())
    healthcare=float(entry_healthcare.get()) 
    transportation=float(entry_transportation.get())

    # Calculate total expenses
    total_expenses = rent + groceries + utilities + entertainment + healthcare +transportation

    # Store the expenses in the dictionary
    month = month_var.get()
    monthly_expenses[month] = {
        'Rent': rent,
        'Groceries': groceries,
        'Utilities': utilities,
        'Entertainment': entertainment,
        'Healthcare' : healthcare, 
        'Transportation': transportation,
        'Total': total_expenses
    }

    # Update the result label
    result_label.config(text=f"Total Expenses for {month}: ${total_expenses:.2f}")

    # Create a pie chart
    labels = ['Rent', 'Groceries', 'Utilities', 'Entertainment','Healthcare','Transportation']
    sizes = [rent, groceries, utilities, entertainment, healthcare, transportation]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart in a new window
    new_window = tk.Toplevel(window)
    new_window.title(f"Pie Chart for {month}")
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Create a button to return to the main window
    return_button = ttk.Button(new_window, text="Return to Main Window", command=new_window.destroy)
    return_button.pack()

def compare_expenses():
    # Compare expenses for two months
    month1 = month1_var.get()
    month2 = month2_var.get()

    if month1 in monthly_expenses and month2 in monthly_expenses:
        expenses1 = monthly_expenses[month1]['Total']
        expenses2 = monthly_expenses[month2]['Total']

        comparison_label.config(text=f"Comparison: {month1} vs {month2}\n"
                                     f"{month1} Expenses: ${expenses1:.2f}\n"
                                     f"{month2} Expenses: ${expenses2:.2f}")
        if expenses1 > expenses2:
          comparison_label.config(text=comparison_label.cget('text') +
                                   f"\n{month1} expenses are higher than {month2}.")
        elif expenses1 < expenses2:
          comparison_label.config(text=comparison_label.cget('text') +
                                   f"\n{month2} expenses are higher than {month1}.")
        else:
          comparison_label.config(text=comparison_label.cget('text') +
                                   "\nExpenses for both months are equal.")
    else:
        comparison_label.config(text="Please select valid months for comparison.")
def expense_suggestion():
  if not monthly_expenses:
      suggestion_label.config(text="Please enter expenses for both months to compare.")
      return

  month1 = month1_var.get()
  month2 = month2_var.get()

  if month1 in monthly_expenses and month2 in monthly_expenses:
      expenses1 = monthly_expenses[month1]['Total']
      expenses2 = monthly_expenses[month2]['Total']

      if expenses1 > expenses2:
          suggestion_label.config(text=f"Suggestion: Consider budgeting more in {month1}.")
      elif expenses1 < expenses2:
          suggestion_label.config(text=f"Suggestion: Consider budgeting more in {month2}.")
      else:
          suggestion_label.config(text="Expenses for both months are equal.")
  else:
      suggestion_label.config(text="Please select valid months for comparison.")

# Create a label to display the suggestion

# Create the main window
window = tk.Tk()
window.title("Monthly Expenses Calculator")
window.geometry("600x450")
window.configure(bg='oldlace')
# Create entry widgets for expenses
entry_rent = ttk.Entry(window, width=10)
entry_groceries = ttk.Entry(window, width=10)
entry_utilities = ttk.Entry(window, width=10)
entry_entertainment = ttk.Entry(window, width=10)
entry_healthcare = ttk.Entry(window, width=10)
entry_transportation = ttk.Entry(window, width=10)
# Create labels for entry widgets
label_rent = ttk.Label(window, text="Rent:", font=('Arial', 10, 'bold'))
label_groceries = ttk.Label(window, text="Groceries:")
label_utilities = ttk.Label(window, text="Utilities:")
label_entertainment = ttk.Label(window, text="Entertainment:")
label_healthcare = ttk.Label(window, text="Healthcare:")
label_transportation = ttk.Label(window, text="Transportation:")
# Create a button to calculate expenses
calculate_button = ttk.Button(window, text="Calculate", command=calculate_expenses,)

# Create a label to display the result
result_label = ttk.Label(window, text="Total Expenses: Rs 0.00")

# Create labels for user input
user_input_label = ttk.Label(window, text="Enter Monthly Expenses:",foreground='white', background='blue')
user_input_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create a dropdown menu for month selection
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_var = tk.StringVar(value=months[0])
month_dropdown = ttk.Combobox(window, textvariable=month_var, values=months, state="readonly")

# Create labels for comparison
compare_label = ttk.Label(window, text="Compare Expenses:",foreground='white', background='blue')
compare_label.grid(row=5, column=0, columnspan=2, pady=10)

# Create dropdown menus for month comparison
month1_var = tk.StringVar(value=months[0])
month2_var = tk.StringVar(value=months[0])
month1_dropdown = ttk.Combobox(window, textvariable=month1_var, values=months, state="readonly")
month2_dropdown = ttk.Combobox(window, textvariable=month2_var, values=months, state="readonly")

# Create a button to compare expenses
compare_button = ttk.Button(window, text="Compare", command=compare_expenses)

# Create a label to display the comparison result
comparison_label = ttk.Label(window, text="Comparison: ",foreground='black', background='magenta')

# Place widgets in the window using the grid layout
label_rent.grid(row=1, column=0, padx=5, pady=5)
entry_rent.grid(row=1, column=1, padx=5, pady=5)
label_groceries.grid(row=2, column=0, padx=5, pady=5)
entry_groceries.grid(row=2, column=1, padx=5, pady=5)
label_utilities.grid(row=3, column=0, padx=5, pady=5)
entry_utilities.grid(row=3, column=1, padx=5, pady=5)
label_entertainment.grid(row=4, column=0, padx=5, pady=5)
entry_entertainment.grid(row=4, column=1, padx=5, pady=5)
label_healthcare.grid(row=5, column=0, padx=5, pady=5)
entry_healthcare.grid(row=5, column=1, padx=5, pady=5)
label_transportation.grid(row=6, column=0, padx=5, pady=5)
entry_transportation.grid(row=6, column=1, padx=5, pady=5)
calculate_button.grid(row=8, column=0, columnspan=2, pady=10)
result_label.grid(row=8, column=2, columnspan=2, pady=10)

user_input_label.grid(row=7, column=0, columnspan=2, pady=10)
month_dropdown.grid(row=7, column=2, columnspan=2, pady=5)

compare_label.grid(row=9, column=0, columnspan=2, pady=10)
month1_dropdown.grid(row=9, column=2, pady=5)
month2_dropdown.grid(row=9, column=3, pady=5)
compare_button.grid(row=10, column=0, columnspan=2, pady=5)
comparison_label.grid(row=10, column=2, columnspan=2, pady=5)

suggestion_label = ttk.Label(window, text="Comparison Suggestion: ",foreground='black', background='magenta')
suggestion_label.grid(row=11, column=0, columnspan=4, pady=10)

# Create a button to show the expense suggestion
suggestion_button = ttk.Button(window, text="Suggestion", command=expense_suggestion)
suggestion_button.grid(row=12, column=0, columnspan=4, pady=10)
# Start the Tkinter event loop
window.mainloop()