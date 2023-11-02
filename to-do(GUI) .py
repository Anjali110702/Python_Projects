from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title('To-Do List App')
ws.geometry('1920x1080')
ws['bg'] = '#F0F0F0'

# Create a top and bottom frame
bottom_frame = Frame(ws)
bottom_frame.pack(side=BOTTOM, padx=10, pady=10)
top_frame = Frame(ws)
top_frame.pack(side=BOTTOM, padx=10, pady=10)

# Create a label for the top table (To-Do List)
top_label = Label(top_frame, text="To-Do List", font=("Arial", 14, "bold"))
top_label.grid(row=0, column=0, sticky=W)

# Frame for the top table (To-Do List)
top_left_frame = Frame(top_frame)
top_left_frame.grid(row=1, column=0, padx=10, pady=10)


# Scrollbars for the top table
top_scroll_y = Scrollbar(top_left_frame)
top_scroll_y.pack(side=RIGHT, fill=Y)
top_scroll_x = Scrollbar(top_left_frame, orient='horizontal')
top_scroll_x.pack(side=BOTTOM, fill=X)

# Create the top table (To-Do List)
top_table = ttk.Treeview(
    top_left_frame,
    yscrollcommand=top_scroll_y.set,
    xscrollcommand=top_scroll_x.set,
    selectmode='browse',
    columns=('Priority', 'Task', 'Description', 'Due Date')
)
top_table.pack(fill='both', expand=True)
top_scroll_y.config(command=top_table.yview)
top_scroll_x.config(command=top_table.xview)

# Define the columns for the top table
top_table.column("#0", width=0, stretch=NO)
top_table.column("Priority", anchor=CENTER, width=120)
top_table.column("Task", anchor=CENTER, width=250)
top_table.column("Description", anchor=CENTER, width=250)
top_table.column("Due Date", anchor=CENTER, width=120)

# Create headings for the top table
top_table.heading("#0", text="", anchor=CENTER)
top_table.heading("Priority", text="Priority", anchor=CENTER)
top_table.heading("Task", text="Task", anchor=CENTER)
top_table.heading("Description", text="Description", anchor=CENTER)
top_table.heading("Due Date", text="Due Date", anchor=CENTER)

# Create a label for the bottom table (Completed Tasks)
bottom_label = Label(bottom_frame, text="Completed Tasks", font=("Arial", 14, "bold"))
bottom_label.pack(side=TOP, anchor=W)

# Frame for the bottom table (Completed Tasks)
bottom_left_frame = Frame(bottom_frame)
bottom_left_frame.pack(side=TOP, padx=10, pady=10)

# Scrollbars for the bottom table
bottom_scroll_y = Scrollbar(bottom_left_frame)
bottom_scroll_y.pack(side=RIGHT, fill=Y)
bottom_scroll_x = Scrollbar(bottom_left_frame, orient='horizontal')
bottom_scroll_x.pack(side=BOTTOM, fill=X)

# Create the bottom table (Completed Tasks)
bottom_table = ttk.Treeview(
    bottom_left_frame,
    yscrollcommand=bottom_scroll_y.set,
    xscrollcommand=bottom_scroll_x.set,
    selectmode='browse',
    columns=('Priority', 'Task', 'Description')
)
bottom_table.pack(fill='both', expand=True)
bottom_scroll_y.config(command=bottom_table.yview)
bottom_scroll_x.config(command=bottom_table.xview)

# Define the columns for the bottom table
bottom_table.column("#0", width=80, anchor=CENTER) 
bottom_table.column("Priority", anchor=CENTER, width=120)
bottom_table.column("Task", anchor=CENTER, width=250)
bottom_table.column("Description", anchor=CENTER, width=250)

# Create headings for the bottom table
bottom_table.heading("#0", text="", anchor=CENTER)
bottom_table.heading("Priority", text="Priority", anchor=CENTER)
bottom_table.heading("Task", text="Task", anchor=CENTER)
bottom_table.heading("Description", text="Description", anchor=CENTER)


# Input fields
frame = Frame(ws)
frame.pack(pady=20)

priority = Label(frame, text="Priority")
priority.grid(row=0, column=0)

taskname = Label(frame, text="Task")
taskname.grid(row=0, column=1)

task_disc = Label(frame, text="Description")
task_disc.grid(row=0, column=2)

due_date = Label(frame, text="Due Date")
due_date.grid(row=0, column=3)

priority_entry = Entry(frame)
priority_entry.grid(row=1, column=0)

taskname_entry = Entry(frame)
taskname_entry.grid(row=1, column=1)

task_disc_entry = Entry(frame)
task_disc_entry.grid(row=1, column=2)

due_date_entry = Entry(frame)
due_date_entry.grid(row=1, column=3)

# Functions
def input_record():
    priority = priority_entry.get()
    task = taskname_entry.get()
    description = task_disc_entry.get()
    due_date = due_date_entry.get()
    
    top_table.insert('', 'end', values=(priority, task, description, due_date))
    
    # Clear entry fields
    priority_entry.delete(0, END)
    taskname_entry.delete(0, END)
    task_disc_entry.delete(0, END)
    due_date_entry.delete(0, END)
   

def select_record():
    selected = top_table.focus()
    values = top_table.item(selected, 'values')
    priority_entry.delete(0, END)
    taskname_entry.delete(0, END)
    task_disc_entry.delete(0, END)
    due_date_entry.delete(0, END)  
    
    priority_entry.insert(0, values[0])
    taskname_entry.insert(0, values[1])
    task_disc_entry.insert(0, values[2])
    due_date_entry.insert(0, values[3])

def update_record():
    selected = top_table.focus()
    values = top_table.item(selected, 'values')
    values = (
        priority_entry.get(),
        taskname_entry.get(),
        task_disc_entry.get(),
        due_date_entry.get()
    )
    
    top_table.item(selected, values=values)

    # Clear entry fields
    priority_entry.delete(0, END)
    taskname_entry.delete(0, END)
    task_disc_entry.delete(0, END)
    due_date_entry.delete(0, END)


def remove():
    selected = top_table.selection()
    for item in selected:
        top_table.delete(item)

def move_selected_row():
    selected = top_table.selection()
    for item in selected:
        values = top_table.item(item, 'values')
        bottom_table.insert('', 'end', values=values)
        
        top_table.delete(item)

def exit_program():
    ws.destroy()


# Buttons (placed on the left side of the tables)
Input_button = Button(ws, text="Add Task", bg="orange", command=input_record)
Input_button.pack()
select_button = Button(top_left_frame, text="Select Task", bg="orange", command=select_record)
select_button.pack(side=LEFT, padx=5)
edit_button = Button(top_left_frame, text="Update Task", bg="orange", command=update_record)
edit_button.pack(side=LEFT, padx=5)

remove_button = Button(top_left_frame, text="Remove Task", bg="orange", command=remove)
remove_button.pack(side=LEFT, padx=5)

move_button = Button(top_left_frame, text="Mark As Completed", bg="orange", command=move_selected_row)
move_button.pack(side=LEFT, padx=5)

# Exit button
exit_button = Button(bottom_left_frame, text="Exit", bg="RED", command=exit_program)
exit_button.pack(side=BOTTOM, padx=10, pady=10)

ws.mainloop()
