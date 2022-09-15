
print("Testing in Progress")
from tkinter import Tk, Label
from datetime import datetime

window = Tk()
window.title("Digital Clock")
window.configure(bg="red")
window.geometry("600x300")

window.configure(bg="darkgreen")
label = Label(window, font=("Arial Black",78,"bold"), bg="darkgreen", fg="white")
label.pack(pady=100)

def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500,clock)

clock()
window.mainloop()
