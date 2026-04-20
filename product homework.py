# Write a Python program to create an application to 
# take two numbers as input from the user and return the product 
# using the Python Tkinter library.


from tkinter import *

window = Tk()
window.title= "Calculate the product"
window.geometry= "400x300"

lbl = Label(text="Hey there! Enter the two numbers for which you want the product", fg = "white", bg = "#ffb6c1", height = 1, width = 300)

num1_lbl = Label(text="First number", bg= "#ffb6c1")
num1_entry = Entry()

num2_lbl = Label(text="Second number", bg= "#ffb6c1")
num2_entry = Entry()


def display():
    num1 = num1_entry.get()
    num2 = num2_entry.get()
    product = int(num1) * int(num2)
    message = "Thank you for filling it in, here is the product: " + str(product)

    text_box.insert(END, message)    

text_box = Text(height= 3)


btn = Button(text="Calculate", command = display, height = 1, bg = "#ffb6c1", fg = "white")

lbl.pack()
num1_lbl.pack()
num2_lbl.pack()
num1_entry.pack()
num2_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()