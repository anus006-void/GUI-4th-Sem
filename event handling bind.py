import tkinter as tk

window = tk.Tk()

def handle_click(event):
    print(f'Button pressed at X- {event.x}, Y= {event.y}')
    button.config(bg='green')

def handle_key(event):
    print(f'Key pressed: {event.char}')

button = tk.Button(window, text='Click Me')
button.pack()

entry = tk.Entry(window)
entry.pack()

# Bind a function to a left mouse click on the button
button.bind('<Button-1>', handle_click)

# Bind a function to any key press on the entry widget
entry.bind('<Key>', handle_key)

window.mainloop()