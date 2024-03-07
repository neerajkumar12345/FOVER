
from tkinter import ttk
import tkinter as tk
import ex
win=tk.Tk()
win.title('first_tkinter')

#create labels
#widgets --> label, button, radio button
name_label=ttk.Label(win, text='Enter your name :')
name_label.grid(row=0, column=0, sticky=tk.W)

email_label=ttk.Label(win, text='Enter your email :')
email_label.grid(row=1, column=0, sticky=tk.W)


age_label=ttk.Label(win, text='Enter your age :')
age_label.grid(row=2, column=0, sticky=tk.W)

#create entry box

name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable = name_var)
name_entrybox.grid(row=0, column=1)


email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=16, textvariable = email_var)
email_entrybox.grid(row=1, column=1)


age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable = age_var)
age_entrybox.grid(row=2, column=1)

# create combobox
gender_combobox=ttk.Combobox(win, width=16)
gender_combobox['values']=('Male','Female', 'other')
gender_combobox(row=3, column=0)

'''
#create button
def action():
    username=name_var.get()
    userage=age_var.get()
    user_email=email_var.get()
    print(f'{username} is {userage} year old, {user_email}')

Submit_button = ttk.Button(win, text= 'Submit', command=action)
Submit_button.grid(row=3, column=1)



'''
#create button
def action():

    print(ex.facerecognition())

Submit_button = ttk.Button(win, text= 'Submit', command=action)
Submit_button.grid(row=3, column=1)








    

win.mainloop()
