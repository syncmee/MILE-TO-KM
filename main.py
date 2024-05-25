from tkinter import *

window = Tk()
window.title("Miles To Kilometer Converter")
window.minsize(100, 100)


#Function
def calculate():
    miles = float(input.get())
    converted = round(miles * 1.609, 2)
    label3.config(text=f"{converted}")


#Input
input = Entry(width=5)
input.grid(column=1, row=0)

#Labels
label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = Label(text="0")
label3.grid(column=1, row=1)
label4 = Label(text="km")
label4.grid(column=2, row=1)

#Buttons

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
