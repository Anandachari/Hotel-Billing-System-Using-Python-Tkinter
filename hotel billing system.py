from tkinter import *

# main window
window = Tk()
window.geometry("700x600")
window.title("Anand Cafeteria")

# ---- Title ----
title_label = Label(window, text="Cafeteria", font=("Times", 30, "bold"), fg="blue")
title_label.pack(pady=10)

# ---- Menu Section ----
label1 = Label(window, text="Menu", font=("Times", 24, "bold"))
label1.place(x=550, y=70)

label2 = Label(window, text="Aloo Paratha - Rs 30", font=("Times", 18))
label2.place(x=450, y=120)

label3 = Label(window, text="Samosa - Rs 15", font=("Times", 18))
label3.place(x=450, y=160)

label4 = Label(window, text="Tea - Rs 10", font=("Times", 18))
label4.place(x=450, y=200)

label5 = Label(window, text="Coffee - Rs 20", font=("Times", 18))
label5.place(x=450, y=240)

# ---- Billing Section ----
label10 = Label(window, text="Enter Quantity", font=("Times", 18))
label10.place(x=240, y=90)

# entries for each item
e1 = Entry(window)   # Aloo Paratha
e1.place(x=240, y=130)

e2 = Entry(window)   # Samosa
e2.place(x=240, y=170)

e3 = Entry(window)   # Tea
e3.place(x=240, y=210)

e4 = Entry(window)   # Coffee
e4.place(x=240, y=250)

# function to calculate bill
def calculate():
    # Calculate total in one line, treating empty entries as 0
    Aloo  =int(e1.get() or 0)
    Samosa=int(e2.get() or 0)
    Tea   =int(e3.get() or 0)
    Coffee=int(e4.get() or 0)
    total = (Aloo* 30) + (Samosa* 15) + (Tea* 10) + (Coffee* 20)

    # Display the final total
    result_label.config(text=f"Total Bill = Rs {total}")

# function to clear
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    result_label.config(text="")

# button for bill
b1 = Button(window, text="Bill", command=calculate, width=10, bg="green", fg="white")
b1.place(x=100, y=350)

# clear button
b2 = Button(window, text="Clear", command=clear, width=10, bg="red", fg="white")
b2.place(x=220, y=350)

# result label
result_label = Label(window, text="", font=("Times", 16, "bold"), justify=LEFT)
result_label.place(x=100, y=400)

window.mainloop()
