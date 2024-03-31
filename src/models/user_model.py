import sqlite3

class UserModel:
  def __init__(self, db_path):
    self.db_path = db_path

  def create_table(self):
    conn = sqlite3.connect(self.db_path)
    cursor = conn.cursor()

    cursor.execute('''
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
      )
    ''')

    conn.commit()
    conn.close()

  def insert_user(self, email, password):
    conn = sqlite3.connect(self.db_path)
    cursor = conn.cursor()
    cursor.execute('''
      INSERT INTO users (email, password)
      VALUES (?, ?)
    ''', (email, password))
    conn.commit()
    conn.close()

  def select_user(self, email):
    print(email)
    conn = sqlite3.connect(self.db_path)
    cursor = conn.cursor()
    cursor.execute('''
      SELECT * FROM users WHERE email = ?
    ''', (email,))
    user = cursor.fetchall()
    conn.commit()
    conn.close()
    return user