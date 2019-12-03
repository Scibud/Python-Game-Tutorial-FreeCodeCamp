import sqlite3

def mailtrigger(id):
    #DB initilization
    User_Log = sqlite3.connect("users.db")
    cursor_user = User_Log.cursor()
    
    # Checking if mail id already registered
    dv = None
    cursor_user.execute('SELECT email FROM users WHERE email = ?;',[id])
    dv = cursor_user.fetchone()
    User_Log.close()

    if dv is not None:
        return False
    else :
        return True

def register(count,name, email, password):
    #DB initilization
    User_Log = sqlite3.connect("users.db")
    cursor_user = User_Log.cursor()
    
    # Updating DB
    cursor_user.execute('INSERT INTO users(UserID, Name, email,password) VALUES(?,?,?,?);',(count,name,email,password))

    # Updating Server
    User_Log.commit()
    User_Log.close()


#                Main Function
count = 0
while True:
    
    entry = input("Would you like to register  [Y/N]: ")
    
    if entry == "Y" or entry == "y":
        name = input("Enter your name : ")
        email = input('Enter your Email ID : ')
        password = input('Enter the password : ')
        flag = mailtrigger(email)
        if flag == True :
            count += 1
            register(count,name, email, password)
        else :
            print("User already registered")
    else:
        exit()
