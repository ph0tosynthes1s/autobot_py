import sqlite3
import re
import datetime
import csv

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_purchase(self, user_id, username, msg_id, date, chat_id):
        with self.connection:
            self.cursor.execute("INSERT INTO 'purchases' ('user_id', 'username', msg_id, date, chat_id) VALUES (?,?,?,?,?)", (user_id, username, msg_id, date, chat_id))

    def add_pts(self, user_id, username, msg_id, date, chat_id):
        with self.connection:
            self.cursor.execute(
                "INSERT INTO 'pts' ('user_id', 'username', msg_id, date, chat_id) VALUES (?,?,?,?,?)",
                (user_id, username, msg_id, date, chat_id))

    def get_full_purchase(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM full_purchases WHERE user_id = ? ORDER BY date DESC", (user_id,)).fetchall()
            records = []
            for row in result:
                records.append({'purchase':row[3], 'date':row[4]})
            return records

    def get_history(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM history WHERE username = ? ORDER BY date DESC", (user_id,)).fetchall()
            return result

    def get_history_today(self, user_id, date):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM history WHERE  username = ? ORDER BY date DESC", (user_id,)).fetchall()
            records = []
            for row in result:
                if date in row[4]:
                    records.append((row[0], row[1], row[2], row[3], row[4], row[5]))
                else:
                    print('none')
            return records

    def create_csv(self,):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM full_purchases", ()).fetchall()
            with open("All_history.csv", "w", newline='', encoding="utf-8") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in self.cursor.description])
                csv_writer.writerows(result)



