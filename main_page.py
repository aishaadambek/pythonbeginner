from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbConnect import DBConnect
from listReservation import listUsers

dbConnect = DBConnect()

root = Tk()
root.configure(background='#015692')
root.title('Reservation')

#style
style = ttk.Style()
style.theme_use('classic')
style.configure('TLabel', background='#015692', foreground='white')
style.configure('TButton', background='#015692', foreground='white')
style.configure('TRadiobutton', background='#015692', foreground='white')

ttk.Label(root, text='Full name: ').grid(row=0, column=0, pady=10, padx=10)
ttk.Label(root, text='Gender: ').grid(row=1, column=0)
ttk.Label(root, text='Comment: ').grid(row=2, column=0)

etFullName = ttk.Entry(root, width=30, font=('Arial', 14))
etFullName.grid(row=0, column=1, columnspan=3, pady=10)

spanGender = StringVar()
spanGender.set('Male')
ttk.Radiobutton(root, text='Male', variable=spanGender, value='Male').grid(row=1, column=1)
ttk.Radiobutton(root, text='Female', variable=spanGender, value='Female').grid(row=1, column=2)
ttk.Radiobutton(root, text='Other', variable=spanGender, value='Other').grid(row=1, column=3)

textComments = Text(root, width=30, height=15, font=('Arial', 14))
textComments.grid(row=2, column=1, columnspan=3, pady=10)

submitButton = ttk.Button(root, text='Submit')
submitButton.grid(row=3, column=4)


def buttonClick():
    print("Full name: {}".format(etFullName.get()))
    print("Gender: {}".format(spanGender.get()))
    print("Comments: {}".format(textComments.get(1.0, 'end')))
    msg = dbConnect.add(etFullName.get(), spanGender.get(), textComments.get(1.0, 'end'))
    messagebox.showinfo(title='Add Info', message=msg)
    etFullName.delete(0, 'end')
    textComments.delete(1.0, 'end')


def buttonList():
    listUsersVar = listUsers()


submitButton.config(command=buttonClick)


listAllButton = ttk.Button(root, text='List everything')
listAllButton.grid(row=3, column=3)
listAllButton.config(command=buttonList)

root.mainloop()


