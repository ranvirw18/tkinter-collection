from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email= email_entry.get()
    password = password_entry.get()
    print(email, password)
    
    if email=="tonystark@gmail.com" and password=="12345":
        messagebox.showinfo("lessgoo, Login Successful")
    else:
        messagebox.showerror("oops, Login Failed")

root = Tk()
root.geometry("350x600")
root.title("login Form")
root.config(bg="#0096DC")

# Open and resize the image
img = Image.open("flipk1.png")
resized_img = img.resize((70, 70))  # width, height
img_tk = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img_tk)
img_label.pack()

text_label=Label(root, text="Flipkart", font=("Verdana", 24, "bold") , bg="#0096DC", fg="white")
text_label.pack()

email_label = Label(root, text="Enter Email", font=("Arial", 12, "bold"), bg="#0096DC", fg="white")
email_label.pack(pady=(20,5))

email_entry = Entry(root, width=50, font=("Arial", 12))
email_entry.pack(ipady=6, pady=(1,15))

password_label = Label(root, text="Enter Password", font=("Arial", 12, "bold"), bg="#0096DC", fg="white")
password_label.pack(pady=(20,4))

password_entry = Entry(root, width=50, font=("Arial", 12), show="*")
password_entry.pack(ipady=6, pady=(1,15))

login_button = Button(root, text="Login", font=("Arial", 12, "bold"), bg="#FF9900", fg="white", width=20, command=handle_login)
login_button.pack(pady=(20,10))

root.mainloop()