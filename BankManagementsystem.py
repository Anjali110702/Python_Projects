import tkinter as tk


class BankManagementSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank Management System")
        self.bank_system = BankManagementSystem()
        
        self.master.configure(bg="#000000")          
        btn_color = "#800080"

        self.label_acc_holder = tk.Label(master, text="Account Holder:", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_acc_holder.pack(pady=10)

        self.entry_acc_holder = tk.Entry(master, font=("Arial", 12))
        self.entry_acc_holder.pack(pady=5)

        self.label_acc_no = tk.Label(master, text="Account Number:", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_acc_no.pack(pady=10)

        self.entry_acc_no = tk.Entry(master, font=("Arial", 12))
        self.entry_acc_no.pack(pady=5)

        self.bank_system.new_user("Initial Account", "000001", 1000)

        self.create_btn = tk.Button(master, text="Create Account", command=self.create_account, bg=btn_color, fg="#FFFFFF", font=("Arial", 12))
        self.create_btn.pack(pady=10)

        self.display_btn = tk.Button(master, text="Display Balance", command=self.display_balance, bg=btn_color, fg="#FFFFFF", font=("Arial", 12))
        self.display_btn.pack(pady=10)

        self.withdraw_btn = tk.Button(master, text="Withdraw", command=self.open_withdraw_window, bg=btn_color, fg="#FFFFFF", font=("Arial", 12))
        self.withdraw_btn.pack(pady=10)

        self.credit_btn = tk.Button(master, text="Credit", command=self.open_credit_window, bg=btn_color, fg="#FFFFFF", font=("Arial", 12))
        self.credit_btn.pack(pady=10)

        self.update_btn = tk.Button(master, text="Update Account Holder", command=self.open_update_window, bg=btn_color, fg="#FFFFFF", font=("Arial", 12))
        self.update_btn.pack(pady=10)

        self.result_label = tk.Label(master, text="", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.center_widgets()


        window_width = 600
        window_height = 400
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.master.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        self.master.pack_propagate(0)  
        self.master.protocol("WM_DELETE_WINDOW", self.master.quit)
        self.master.bind("<Configure>", self.on_window_resize)

    def center_widgets(self):
        for widget in self.master.winfo_children():
            widget.pack_configure(anchor="center")

    def create_account(self):
        acc_holder = self.entry_acc_holder.get().strip()
        acc_no = self.entry_acc_no.get().strip()
        if acc_holder and acc_no:  
            self.bank_system.new_user(acc_holder, acc_no, 1000)  
            self.result_label.config(text=f"{acc_holder} account created with initial balance 1000.")
        else:
            self.result_label.config(text="Please enter both account holder and account number.")

    def display_balance(self):
        acc_no = self.entry_acc_no.get().strip()
        if acc_no:  
            balance = self.bank_system.display_balance(acc_no)
            if balance != "Account not found.":
                self.result_label.config(text=f"Balance for account {acc_no}: {balance}")
            else:
                self.result_label.config(text=balance)
        else:
            self.result_label.config(text="Please enter account number.")

    def open_withdraw_window(self):
        acc_no = self.entry_acc_no.get().strip()
        if acc_no: 
            withdraw_window = WithdrawWindow(self.master, self.bank_system, self.result_label, self.display_balance)
        else:
            self.result_label.config(text="Please enter account number.")

    def open_credit_window(self):
        acc_no = self.entry_acc_no.get().strip()
        if acc_no:  
            credit_window = CreditWindow(self.master, self.bank_system, self.result_label, self.display_balance)
        else:
            self.result_label.config(text="Please enter account number.")

    def open_update_window(self):
        acc_no = self.entry_acc_no.get().strip()
        if acc_no:  
            update_window = UpdateWindow(self.master, self.bank_system, self.result_label)
        else:
            self.result_label.config(text="Please enter account number.")

    def on_window_resize(self, event):
        current_width = self.master.winfo_width()
        current_height = self.master.winfo_height()

        
        font_size = min(current_width, current_height) // 40

        for widget in self.master.winfo_children():
            if isinstance(widget, (tk.Label, tk.Entry, tk.Button)):
                widget.config(font=("Arial", font_size))

class WithdrawWindow:
    def __init__(self, master, bank_system, result_label, display_balance):
        self.master = master
        self.withdraw_window = tk.Toplevel(master)
        self.withdraw_window.title("Withdraw")
        self.bank_system = bank_system
        self.result_label = result_label
        self.display_balance = display_balance

        self.withdraw_window.configure(bg="#000000")  

        self.label_acc_no = tk.Label(self.withdraw_window, text="Account Number:", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_acc_no.pack(pady=10)

        self.entry_acc_no = tk.Entry(self.withdraw_window, font=("Arial", 12))
        self.entry_acc_no.pack(pady=5)

        self.label_amount = tk.Label(self.withdraw_window, text="Amount:", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_amount.pack(pady=10)

        self.entry_amount = tk.Entry(self.withdraw_window, font=("Arial", 12))
        self.entry_amount.pack(pady=5)

        self.withdraw_btn = tk.Button(self.withdraw_window, text="Withdraw", command=self.withdraw_money, bg="#800080", fg="#FFFFFF", font=("Arial", 12))
        self.withdraw_btn.pack(pady=10)

    def withdraw_money(self):
        acc_no = self.entry_acc_no.get()
        amount = int(self.entry_amount.get())
        result = self.bank_system.withdraw_money(acc_no, amount)
        self.result_label.config(text=result)
        if result != "Insufficient funds." and result != "Account not found.":
            self.display_balance()
        self.withdraw_window.destroy()

class CreditWindow:
    def __init__(self, master, bank_system, result_label, display_balance):
        self.master = master
        self.credit_window = tk.Toplevel(master)
        self.credit_window.title("Credit")
        self.bank_system = bank_system
        self.result_label = result_label
        self.display_balance = display_balance

        self.credit_window.configure(bg="#000000") 

        self.label_acc_no = tk.Label(self.credit_window, text="Account Number:", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_acc_no.pack(pady=10)

        self.entry_acc_no = tk.Entry(self.credit_window, font=("Arial", 12))
        self.entry_acc_no.pack(pady=5)

        self.label_amount = tk.Label(self.credit_window, text="Amount:", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_amount.pack(pady=10)

        self.entry_amount = tk.Entry(self.credit_window, font=("Arial", 12))
        self.entry_amount.pack(pady=5)

        self.credit_btn = tk.Button(self.credit_window, text="Credit", command=self.credit_amount, bg="#800080", fg="#FFFFFF", font=("Arial", 12))
        self.credit_btn.pack(pady=10)

    def credit_amount(self):
        acc_no = self.entry_acc_no.get()
        amount = int(self.entry_amount.get())
        result = self.bank_system.credit_amount(acc_no, amount)
        self.result_label.config(text=result)
        if result != "Account not found.":
            self.display_balance()
        self.credit_window.destroy()

class UpdateWindow:
    def __init__(self, master, bank_system, result_label):
        self.master = master
        self.update_window = tk.Toplevel(master)
        self.update_window.title("Update Account Holder")
        self.bank_system = bank_system
        self.result_label = result_label

        self.update_window.configure(bg="#000000")  # Set background color to bright black

        self.label_acc_no = tk.Label(self.update_window, text="Account Number:", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_acc_no.pack(pady=10)

        self.entry_acc_no = tk.Entry(self.update_window, font=("Arial", 12))
        self.entry_acc_no.pack(pady=5)

        self.label_new_holder = tk.Label(self.update_window, text="New Account Holder:", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_new_holder.pack(pady=10)

        self.entry_new_holder = tk.Entry(self.update_window, font=("Arial", 12))
        self.entry_new_holder.pack(pady=5)

        self.update_btn = tk.Button(self.update_window, text="Update", command=self.update_acc_holder, bg="#800080", fg="#FFFFFF", font=("Arial", 12))
        self.update_btn.pack(pady=10)

    def update_acc_holder(self):
        acc_no = self.entry_acc_no.get()
        new_holder = self.entry_new_holder.get()
        result = self.bank_system.update_acc_holder(acc_no, new_holder)
        self.result_label.config(text=result)
        self.update_window.destroy()

class BankManagementSystem:
    def __init__(self):
        self.accounts = {}

    def new_user(self, acc_holder, acc_no, balance):
        self.accounts[acc_no] = {"acc_holder": acc_holder, "balance": balance}

    def display_balance(self, acc_no):
        if acc_no in self.accounts:
            return self.accounts[acc_no]["balance"]
        else:
            return "Account not found."

    def withdraw_money(self, acc_no, amount):
        if acc_no in self.accounts:
            if self.accounts[acc_no]["balance"] >= amount:
                self.accounts[acc_no]["balance"] -= amount
                return f"Withdrew {amount} from account {acc_no}. Current balance is {self.accounts[acc_no]['balance']}"
            else:
                return "Insufficient funds."
        else:
            return "Account not found."

    def credit_amount(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no]["balance"] += amount
            return f"Credited {amount} to account {acc_no}. Current balance is {self.accounts[acc_no]['balance']}"
        else:
            return "Account not found."

    def update_acc_holder(self, acc_no, new_holder):
        if acc_no in self.accounts:
            self.accounts[acc_no]["acc_holder"] = new_holder
            return f"Updated account holder of account {acc_no} to {new_holder}."
        else:
            return "Account not found."

def main():
    root = tk.Tk()
    app = BankManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
