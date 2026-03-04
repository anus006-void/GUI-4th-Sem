import tkinter as tk

def login():
    if (entry_UserName.get() == "admin") & (entry_Password.get() == "admin"):
        label_status.config(text = "Login Successful")
    else:
        label_status.config(text = "Login Unsuccessful")

window=tk.Tk()

window.title("Login Window")
window.geometry("500x500")

label = tk.Label(window,text="Welcome!",font=("Times New Roman",25),fg="white",bg="black")
label.pack(padx=5,pady=5)

label_UserName = tk.Label(window,text="UserName",font=("Arial",20),fg="green",bg="light blue")
label_UserName.pack(padx=5,pady=5)
entry_UserName = tk.Entry(window,width=10,font=("Times New Roman",20),bg="light blue")
entry_UserName.pack(padx=5,pady=5)

label_Password = tk.Label(window,text="Password",font=("Arial",20),fg="green",bg="light blue")
label_Password.pack(padx=5,pady=5)
entry_Password = tk.Entry(window,width=10,font=("Times New Roman",20),bg="light blue")
entry_Password.pack(padx=5,pady=5)

button = tk.Button(window,command=login,text="Login",font=("Times New Roman",20),fg="blue",bg="light gray")
button.pack(padx=5,pady=5)

label_status = tk.Label(window,text="Status",font=("Times New Roman",20))
label_status.pack()

test = tk.Button(window,command=lambda: print("Thank You"),text='Done?',font=("Times New Roman",20),fg="blue",bg="light gray",padx=5,pady=5)
test.pack()

window.mainloop()