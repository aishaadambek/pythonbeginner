from tkinter import *
from tkinter import ttk
from dbConnect import DBConnect
from delRecord import deleteRecord

class listUsers:

    def __init__(self):
        self._dbConnect = DBConnect()
        self._root = Tk()

        tv = ttk.Treeview(self._root)
        tv.pack()
        tv.heading("#0", text="ID")
        tv.configure(column=('Name', 'Gender', 'Comment'))
        tv.heading("Name", text='Full Name')
        tv.heading("Gender", text='Gender')
        tv.heading("Comment", text='Comment')

        cursor = self._dbConnect.listInfo()
        for row in cursor:
            tv.insert('', 'end', '#{}'.format(row["ID"]), text=row["ID"])
            tv.set('#{}'.format(row["ID"]), 'Name', row["FullName"])
            tv.set('#{}'.format(row["ID"]), 'Gender', row["Gender"])
            tv.set('#{}'.format(row["ID"]), 'Comment', row["Comment"])

        def deleteButton():
            delRecord = deleteRecord()

        delButton = ttk.Button(self._root, text='Delete')
        delButton.pack()
        delButton.config(command=deleteButton)

        self._root.mainloop()
