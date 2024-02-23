import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class LibraryManagementSystem:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, no_of_copies):
        book = {
            "title": title,
            "author": author,
            "no_of_copies": no_of_copies,
            "available_copies": no_of_copies
        }
        self.books.append(book)
        return f"\n{title} book has been added successfully"

    def display_books(self):
        return self.books

    def borrow_book(self, title):
        book = self.find_book(title)
        if book is not None and book["available_copies"] > 0:
            book["available_copies"] -= 1
            return f"\n{title} book has been borrowed successfully!"
        else:
            return f"\n{title} book is not available in the library"

    def return_book(self, title):
        book = self.find_book(title)
        if book is not None and book["available_copies"] < book["no_of_copies"]:
            book["available_copies"] += 1
            return f"\n{title} book has been returned successfully!"
        else:
            return f"\n{title} book does not belong to the library"

    def find_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return book
        return None

class LibraryManagementGUI:
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")
        master.configure(bg="#FFFACD")  # Cream background
        self.btn_bg_color = "#00FFFF"  # Red color for buttons

        # Load background image
        self.background_image = Image.open("bg.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(master, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.lms = LibraryManagementSystem()
        self.center_widgets()
        master.bind("<Configure>", self.on_window_resize)

    def center_widgets(self):
        self.label = tk.Label(self.master, text="WELCOME TO LIBRARY MANAGEMENT SYSTEM!!!!!", font=("Helvetica", 20))
        self.label.pack(pady=(50, 10))  # Adjust vertical padding to center the label

        for button_text, command in [("Add book", self.open_add_book_window), 
                                     ("Display books", self.open_display_books_window), 
                                     ("Borrow book", self.open_borrow_book_window), 
                                     ("Return book", self.open_return_book_window), 
                                     ("Exit", self.master.quit)]:
            button = tk.Button(self.master, text=button_text, command=command, bg=self.btn_bg_color, font=("Helvetica", 14))
            button.pack(pady=5)

    def on_window_resize(self, event):
        width = self.master.winfo_width()
        font_size = int(width / 50)  # Adjust the font size based on window width
        self.label.config(font=("Helvetica", font_size))
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(font=("Helvetica", int(font_size * 0.7)))
            elif isinstance(widget, tk.Toplevel):
                self.apply_window_properties(widget, font_size)

    def apply_window_properties(self, window, font_size):
        window.configure(bg="#FFFACD")  # Cream background
        for widget in window.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(font=("Helvetica", font_size))
            elif isinstance(widget, (ttk.Treeview, tk.Entry)):
                widget.config(font=("Helvetica", int(font_size * 0.7)))
            elif isinstance(widget, tk.Button):
                widget.config(bg=self.btn_bg_color, font=("Helvetica", int(font_size * 0.7)))

    def open_add_book_window(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Add Book")

        self.title_label = tk.Label(self.add_window, text="Title:")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(self.add_window)
        self.title_entry.grid(row=0, column=1)

        self.author_label = tk.Label(self.add_window, text="Author:")
        self.author_label.grid(row=1, column=0)
        self.author_entry = tk.Entry(self.add_window)
        self.author_entry.grid(row=1, column=1)

        self.copies_label = tk.Label(self.add_window, text="Number of Copies:")
        self.copies_label.grid(row=2, column=0)
        self.copies_entry = tk.Entry(self.add_window)
        self.copies_entry.grid(row=2, column=1)

        self.add_button = tk.Button(self.add_window, text="Add", command=self.add_book, bg="#FF0000")  # Red color for this button
        self.add_button.grid(row=3, columnspan=2, pady=5)

        self.apply_window_properties(self.add_window, 14)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        copies = self.copies_entry.get()
        if title and author and copies.isdigit():
            copies = int(copies)
            message = self.lms.add_book(title, author, copies)
            messagebox.showinfo("Add Book", message)
            self.add_window.destroy()
        else:
            messagebox.showerror("Error", "Please enter valid input for all fields.")

    def open_display_books_window(self):
        self.display_window = tk.Toplevel(self.master)
        self.display_window.title("Display Books")

        books = self.lms.display_books()
        self.tree = ttk.Treeview(self.display_window, columns=("Title", "Author", "Available Copies"))
        self.tree.heading("#0", text="Index")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Available Copies", text="Available Copies")
        for i, book in enumerate(books):
            self.tree.insert('', 'end', text=i, values=(book['title'], book['author'], book['available_copies']))
        self.tree.pack(pady=5)

        self.apply_window_properties(self.display_window, 14)

    def open_borrow_book_window(self):
        self.borrow_window = tk.Toplevel(self.master)
        self.borrow_window.title("Borrow Book")

        self.title_label = tk.Label(self.borrow_window, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.borrow_window)
        self.title_entry.pack()

        self.borrow_button = tk.Button(self.borrow_window, text="Borrow", command=self.borrow_book, bg="#FF0000")  # Red color for this button
        self.borrow_button.pack(pady=5)

        self.apply_window_properties(self.borrow_window, 14)

    def borrow_book(self):
        title = self.title_entry.get()
        message = self.lms.borrow_book(title)
        messagebox.showinfo("Borrow Book", message)
        self.borrow_window.destroy()

    def open_return_book_window(self):
        self.return_window = tk.Toplevel(self.master)
        self.return_window.title("Return Book")

        self.title_label = tk.Label(self.return_window, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.return_window)
        self.title_entry.pack()

        self.return_button = tk.Button(self.return_window, text="Return", command=self.return_book, bg="#FF0000")  # Red color for this button
        self.return_button.pack(pady=5)

        self.apply_window_properties(self.return_window, 14)

    def return_book(self):
        title = self.title_entry.get()
        message = self.lms.return_book(title)
        messagebox.showinfo("Return Book", message)
        self.return_window.destroy()

root = tk.Tk()
my_gui = LibraryManagementGUI(root)
root.mainloop()
