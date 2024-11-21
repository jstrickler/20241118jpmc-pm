import sqlite3

conn = None

try:
    conn = sqlite3.connect("weasels.db")
except Exception as err:
    print(err)
    exit(1)
else:
    cur = conn.cursor()
    # query here....
finally: # close connections, remove temp files and folders
    if conn:
        conn.close()