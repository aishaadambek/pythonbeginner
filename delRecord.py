from tkinter import *
from tkinter import ttk
from dbConnect import DBConnect
from tkinter import messagebox


class deleteRecord:

    def __init__(self):
        self._dbConnect = DBConnect()
        self._root = Tk()

        ttk.Label(self._root, text='Enter ID to delete: ').grid(row=0, column=0, pady=10, padx=10)
        entry = ttk.Entry(self._root, width=30, font=('Arial', 14))
        entry.grid(row=0, column=1)
        delButton = ttk.Button(self._root, text='Delete')
        delButton.grid(row=0, column=2)

        def delete():
            idEntry = int(entry.get())
            self._dbConnect.deleteRecord(idEntry)
            entry.delete()
            messagebox.showinfo(title="Record deleted",
                                message="Record with ID {} was successfully deleted!".format(idEntry))


        delButton.config(command=delete)