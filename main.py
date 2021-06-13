import tkinter
from tkinter import StringVar, font, ttk
from tkinter.constants import CENTER, END

root = tkinter.Tk()
root.title('Metric Helper')
root.iconbitmap('ruler.ico')
root.resizable(0,0)

# defining some fonts and colors
field_font = ('Cambria', 12)
bg_color = '#f5cf87'
button_color= '#c75c5c'

root.config(bg=bg_color)

# defining functions
def convert():
  metric_values={
    'femto' : 10 ** -15,
    'pico': 10 ** -12,
    'nano': 10**-9,
    'micro': 10 **- 6,
    'milli': 10**-3,
    'centi': 10**-2,
    'deci': 10**-1,
    'base value': 10**0,
    'deca': 10**1,
    'hecto': 10**2,
    'kil0': 10**3,
    'mega': 10**6,
    'giga': 10**9,
    'tera': 10**12,
    'tera': 10**12,
    'peta': 10**15,  
  }
  # clear the output field
  output_field.delete(0, END)
  # get the values entered by the user
  start_value=float(input_field.get())
  start_prefix = input_combobox.get()
  end_prefix = output_combobox.get()

  base_value = start_value * metric_values[start_prefix]
  end_value = base_value /metric_values[end_prefix]
  # update the output field with answer
  output_field.insert(0, str(end_value))

# defining layout
# creating the input and output entry fields
input_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3)
output_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3)
equal_label = tkinter.Label(root, text='=', font=field_font, bg=bg_color)

input_field.insert(0, "Enter your quantity")
input_field.grid(row=0, column=0, padx=10,pady=10)
equal_label.grid(row=0, column=1,padx=10,pady=10)
output_field.grid(row=0, column=2,padx=10, pady=10)

# create combobox for metric values
metric_list =['femto', 'pico', 'nano', 'micro', 'milli', 'centi', 'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']
# we don't have to expand the metric list in values for combobox - no need of *metric_list
input_combobox= ttk.Combobox(root, values=metric_list, font=field_font, justify=CENTER)
output_combobox= ttk.Combobox(root, values=metric_list, font=field_font, justify=CENTER)
to_label = tkinter.Label(root, text='to', font=field_font, bg=bg_color)

input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)

input_combobox.set('base value')
output_combobox.set('base value')

# create the converion button
convert_button = tkinter.Button(root, text='Convert', font=field_font, bg=button_color,command=convert)
convert_button.grid(row=2, column=0, columnspan=3, pady=10, padx=10, ipadx=50)

root.mainloop()