import tkinter
from tkinter import font

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

# defining layout
# creating the input and output entry fields
input_field = tkinter.Entry(root, width=20, font=field_font)
output_field = tkinter.Entry(root, width=20, font=field_font)
equal_label = tkinter.Label(root, text='=', font=field_font, bg=bg_color)

input_field.grid(row=0, column=0)
equal_label.grid(row=0, column=1)
output_field.grid(row=0, column=2)

input_field.insert(0, 'Enter your quntity')

root.mainloop()