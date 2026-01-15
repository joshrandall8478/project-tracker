import sqlite3

# Initialize database based off schema.sql script
conn = sqlite3.connect('db/db.db')
with open('schema.sql') as f:
    conn.executescript(f.read())

# Commit all changes and close connection
conn.commit()
conn.close()
