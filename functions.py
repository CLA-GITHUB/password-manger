# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 00:04:56 2021

@author: USER
"""
from mysql.connector import connect
import pyperclip
import random
import string


''''connection function '''
def connect_mysql():
     connection = connect(
          host="localhost",
          user="root",
          password="",
          db="password_manager"
        )
     return connection
'''end connection function'''


'''get user id'''
def get_user_id(username):
    user_id = 0
    connection = connect_mysql()
    cursor = connection.cursor()
    
    query = "SELECT id FROM users WHERE username = username"
    cursor.execute(query)
    results = cursor.fetchall()
    
    for x in results:
        for ii in x:
            user_id = ii
        
    return user_id       
'''end get user id'''


'''add passwords'''
def add_record(user_id, site, password):
    connection = connect_mysql()
    cursor = connection.cursor()
    
    query = "INSERT INTO vault \
        (user_id, site, password) \
        VALUES (%s, %s, %s)"
    values = (user_id, site, password)
    cursor.execute(query, values)
    connection.commit()
    
    pyperclip.copy(password)
    print('Password created and copied to clipboard!')
    
def create_new_passwords(user_id):
    password = input('Enter a password \t')
    site = input('Enter the site you want to use this password on \t')
    
    add_record(user_id, site, password)

'''end add passwords'''


'''view passwords from the database'''
def view_passwords(user_id):
    connection = connect_mysql()
    cursor = connection.cursor()
    query = (f'SELECT site, password FROM password_safe WHERE user_id = {user_id}')
    cursor.execute(query)
    
    results = cursor.fetchall()
    
    for data in results:
        print(f'Site ======== Password \n{data}')
'''end view passwords from the database'''


'''generate random password'''
def random_password():
    password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(12))
    
    pyperclip.copy(password)
    print('Random password created and copied to clipboard!')
'''end generate random password'''


'''log out and clear console'''
def logout():
    print("\033[H\033[J")
'''end log out and clear console'''