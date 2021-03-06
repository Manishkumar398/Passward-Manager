from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#---------------------------FIND PASSWORD---------------------------------#
def find_password():
    website=web_input.get()
    try:
        with open("data.json") as file:
            data=json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="error",message="empty file,file not available")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\npassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"no details for {website} exit")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters) ]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_letters+password_numbers+password_symbols
    random.shuffle(password_list)

    password="".join(password_list)
    password_input.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website=web_input.get()
    email=email_user_input.get()
    password=password_input.get()
    new_data={
        website:{


        "email":email,
        "password":password
        }
    }

    if len(website)==0 or len(password)==0:
       messagebox.showinfo(title="oops",message="something missing")
    else:
        try:
            with open("data.json","r") as file:
                #Reading old file
                data=json.load(file)
        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data,file,indent=4)


        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.json","w") as file:
                #saving updated data
                json.dump(data,file,indent=4)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
#canvas
canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)


#label
website_label=Label(text="Website: ")
website_label.grid(column=0,row=1)
email_user_label=Label(text="Email/Username:")
email_user_label.grid(column=0,row=2)
passward_label=Label(text="Passward")
passward_label.grid(column=0,row=3)
#entry
web_input=Entry(width=21)
web_input.focus()
web_input.grid(column=1,row=1)
email_user_input=Entry(width=35)
email_user_input.insert(28,string="@gmail.com")
email_user_input.grid(column=1,row=2,columnspan=2)
password_input=Entry(width=21)
password_input.grid(column=1, row=3, )
#button
password_button=Button(text="Generate Passward", command=password_generator)
password_button.grid(column=2, row=3, columnspan=1)
add_button=Button(text="Add",width=36,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)
search_button=Button(text="Search",width=14,command=find_password)
search_button.grid(column=2,row=1)





window.mainloop()
