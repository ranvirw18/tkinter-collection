from tkinter import *
from tkinter import messagebox
import random 

root= Tk()
root.title("lucky friend wheel")
root.geometry("500x500")
root.configure(bg="coral")

head1=Label(root, text= "😀LUCKY FRIEND WHEEL😀", font=("Arial", 16, "bold"), fg="Red", bg="coral").pack(pady=10)

entry=Entry(root, font=("Arial", 14))
entry.pack(pady=5)

friends_listbox = Listbox(root,font=("Arial", 14, "bold"), bg="cyan" )
friends_listbox.pack(pady=5,fill="both", expand="True")

def add_friend():
    name = entry.get()
    if name.strip():
        friends_listbox.insert(0, name)
        entry.delete(0, END)
    else: 
        messagebox.showwarning("warning", "enter a name")

def spin_wheel():
    friends= friends_listbox.get(0, END)
    if friends:
        lucky_friend= random.choice(friends)
        result_label.config(text=f"lucky friend is 😉 : {lucky_friend}")
        
btn1=Button(root, text="add friend", command=add_friend, font=("Arial", 10, "bold") )
btn1.pack(pady=5)

btn2=Button(root, text="spin", command=spin_wheel,font=("Arial", 10, "bold"))
btn2.pack(pady=10)

result_label=Label(root, text="",bg="coral", font=("Arial", 14, "bold"))
result_label.pack(pady=10)


root.mainloop()
