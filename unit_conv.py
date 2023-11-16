import tkinter as tk
from tkinter import ttk, messagebox

def update_units(*args):
    category = combo_category.get()
    units = UNIT_CATEGORIES.get(category, [])
    
    combo_source['values'] = units
    combo_target['values'] = units
    combo_source.set(units[0] if units else '')
    combo_target.set(units[1] if len(units) > 1 else '')

def convert():
    category = combo_category.get()
    conversion_function = CONVERSION_FUNCTIONS.get(category)
    
    if conversion_function:
        conversion_function()
    else:
        messagebox.showerror('Error', 'Invalid category selected.')

def generic_conversion(convert_function):
    try:
        value = float(entry_value.get())
        source_unit = combo_source.get()
        target_unit = combo_target.get()

        if source_unit == target_unit:
            messagebox.showwarning('Warning', 'Source and target units are the same.')
            return

        result = convert_function(value, source_unit, target_unit)

        label_result.config(text=f'Result: {result:.2f} {target_unit}')
    except ValueError:
        messagebox.showerror('Error', 'Invalid input. Please enter a numeric value.')

def convert_temperature():
    generic_conversion(lambda value, source, target: (value * 9/5) + 32 if source == 'Celsius' and target == 'Fahrenheit' else (value - 32) * 5/9)

def convert_length():
    generic_conversion(lambda value, source, target: value * 3.281 if source == 'Meters' and target == 'Feet' else value / 3.281)

def convert_weight():
    generic_conversion(lambda value, source, target: value * 2.205 if source == 'Kilograms' and target == 'Pounds' else value / 2.205)

UNIT_CATEGORIES = {
    'Temperature': ['Celsius', 'Fahrenheit'],
    'Length': ['Meters', 'Feet'],
    'Weight': ['Kilograms', 'Pounds'],
}

CONVERSION_FUNCTIONS = {
    'Temperature': convert_temperature,
    'Length': convert_length,
    'Weight': convert_weight,
}

window = tk.Tk()
window.title('Unit Converter')

label_instruction = tk.Label(window, text='Enter value and select units for conversion:')
label_instruction.pack(pady=10)

entry_value = tk.Entry(window, width=10)
entry_value.pack(pady=5)

combo_category = ttk.Combobox(window, values=list(UNIT_CATEGORIES.keys()))
combo_category.set('Temperature')
combo_category.pack(pady=5)
combo_category.bind('<<ComboboxSelected>>', update_units)
combo_source = ttk.Combobox(window, values=UNIT_CATEGORIES['Temperature'])
combo_source.set('Celsius')
combo_source.pack(pady=5)

label_to = tk.Label(window, text='to')
label_to.pack()
combo_target = ttk.Combobox(window, values=UNIT_CATEGORIES['Temperature'])
combo_target.set('Fahrenheit')
combo_target.pack(pady=5)

button_convert = tk.Button(window, text='Convert', command=convert)
button_convert.pack(pady=10)

result_frame = ttk.LabelFrame(window, text='Result')
result_frame.pack(pady=10)
label_result = tk.Label(result_frame, text='Result:')
label_result.pack()

window.mainloop()
