import sqlite3


class DBConnect:

    def __init__(self):
        self._db = sqlite3.connect("Reservation.db")
        self._db.row_factory = sqlite3.Row
        self._db.execute("create table if not exists Reservation(ID integer primary key autoincrement,"
                         "FullName text, Gender text, Comment text)")
        self._db.commit()

    def add(self, name, gender, comment):
        self._db.row_factory = sqlite3.Row
        # add records
        self._db.execute("insert into Reservation(FullName, Gender, Comment) values(?,?,?)",
                         (name, gender, comment))
        self._db.commit()
        return "Record is added"

    def listInfo(self):
        cursor = self._db.execute("select * from Reservation")
        return cursor

    def deleteRecord(self, ID):
        self._db.row_factory = sqlite3.Row
        # delete a record
        self._db.execute("delete from Reservation where ID = {}".format(ID))
        self._db.commit()
        return "Record is deleted"

    def updateRecord(self, ID, comment):
        self._db.row_factory = sqlite3.Row
        # update a record
        self._db.execute("update Reservation set Comment = ? where ID = ?",
                         (comment, ID))
        self._db.commit()
        return "Record is updated"
