import tkinter as tk

window = tk.Tk()

window.title("Login Window")
window.geometry("500x500")

label = tk.Label(window, text='Initial Text',font=("Times New Roman",25))
label.pack()

current_text = label.cget('text') # Using cget()
print(f'Current text: {current_text}')

current_bg = label.config()['bg'][-1] # Using config() and dictionary access
print(f'Current background: {current_bg}')

window.mainloop()