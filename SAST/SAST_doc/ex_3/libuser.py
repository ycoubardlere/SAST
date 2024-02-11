import sqlite3

def login(username, password):
    conn = sqlite3.connect('db_users.sqlite')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()

    if user:
        return user['username']
    else:
        return False

def create(username, password):
    conn = sqlite3.connect('db_users.sqlite')
    c = conn.cursor()

    c.execute("INSERT INTO users (username, password, failures, mfa_enabled, mfa_secret) VALUES (?, ?, ?, ?, ?)", (username, password, 0, 0, ''))

    conn.commit()
    conn.close()

def userlist():
    conn = sqlite3.connect('db_users.sqlite')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    users = c.execute("SELECT * FROM users").fetchall()

    if not users:
        return []
    else:
        return [user['username'] for user in users]

def password_change(username, password):
    conn = sqlite3.connect('db_users.sqlite')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("UPDATE users SET password = ? WHERE username = ?", (password, username))
    conn.commit()

    return True

def password_complexity(password):
    return True