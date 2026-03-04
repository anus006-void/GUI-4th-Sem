import tkinter as tk

def button_click():
    print("Button clicked")
    label.configure(bg="yellow")
    button2.configure(bg="white")
    print("You Typed:",entry.get())

window = tk.Tk()

window.title("Using Button")
window.geometry("400x300")

button = tk.Button(window,text="Click me",command=lambda:print("Click me"),fg="red",bg="light blue")
button.pack()
button2 = tk.Button(window,text="Click me",command=button_click,fg="blue",bg="yellow")
button2.pack()

label = tk.Label(window,text="Hello World",font=("Times New Roman",25))
label.pack()

entry = tk.Entry(window,width=10,font=("Times New Roman",25))
entry.pack()

window.mainloop()