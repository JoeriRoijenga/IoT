import sqlite3 as lite
import sys
con = lite.connect('espData.db')
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM ESP_data;")
