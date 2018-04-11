import sqlite3


class DatabaseManager(object):
    def __init__(self, db):
        """
        Creates a Cursor object for use throughout the program.
        It can only be used to perform queries, anything else is superfluous
        :param db: The path to the database file
        """
        self.conn = sqlite3.connect(db)
        self.conn.commit()
        self.cur = self.conn.cursor()

    def query(self, *arg):
        """
        Executes a query passed in by using the DatabaseManager object
        :param arg: The query to be executed by the Cursor object
        :return: the Cursor object
        """
        self.cur.execute(*arg)
        return self.cur

    def commit(self):
        """
        Commits all changes to database
        :return: the Cursor object
        """
        self.conn.commit()
        return self.cur

    def __del__(self):
        """
        Overrides the close method for the cursor, and ensure proper disconnection from the database
        """
        self.conn.close()
