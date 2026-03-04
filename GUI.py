import tkinter as tk

window=tk.Tk()

window.title("My 1st GUI")
window.geometry("400x200")

label=tk.Label(window,text="Hello, Tkinter!",font=("Arial",15),fg="black",bg="yellow")
label.pack()
label1=tk.Label(window,text="How are you, Tkinter!",font=("Arial",15))
label1.pack()
label2=tk.Label(window,text="Bye, tkinter!",font=("Arial",15))
label2.pack()

window.mainloop()
