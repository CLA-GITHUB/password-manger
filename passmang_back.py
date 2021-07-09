from functions import create_new_passwords, view_passwords, random_password, logout, get_user_id


class Password_manager:
    def __init__(self):
        self.username = ''
        self.id = 0
        
    def menue(self):
        print('1. Add new site and password')
        print('2. View existing sites and passwords')
        print('3. Create a random password')
        print('4. Log out and clear console')
        options= input('Enter an option \t')
        
        if( options =='1'):
            print('Add new site and password')
            create_new_passwords(self.id)
            print('\n')
            print('*' * 20)
            self.menue()
            
        elif ( options == '2'):
             print('Existing sites and passwords')
             view_passwords(self.id)
             print('\n')
             print('*' * 20)
             self.menue()
             
        elif(options == '3'):
            print('Random password generator')
            random_password()
            print('\n')
            print('*' * 20)
            self.menue()
            
        elif(options == '4'):
            print('logging out...')
            logout()
            
        else:
            print('Ivalid input')
            print('\n')
            print('*' * 20)
            self.menue()
       
    def login(self):
        username = input('Enter username: \t')
        print(input('Enter password: \t'))
        self.username = username
        self.id = get_user_id(self.username)
       
           
    def header(self):
        
        print('\n')
        print('Password Manager')
        print('\n')
       
        
    def body(self):
        print('*' * 20)
        self.header()
        print('*' * 20)
        print('\n')
        self.login()
        print('\n')
        print('*' * 20)
        print('\n')
        self.menue()
        print('\n')
        print('*' * 20)
        print('\n')
    

    