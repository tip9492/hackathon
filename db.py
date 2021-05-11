import sqlite3
import hashlib


conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

def make_hashes(password):
 return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
 if make_hashes(password) == hashed_text:
  return hashed_text
 else:
  return False

# DB  Functions
def create_usertable():
 c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
 c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
 conn.commit()

def login_user(username,password):
 c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
 data = c.fetchall()
 return data


def view_all_users():
 c.execute('SELECT * FROM userstable')
 data = c.fetchall()
 return data
