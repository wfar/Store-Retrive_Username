import json

def get_stored_username():
    '''Get stored username if available.'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''Prompt for a new useranme.'''
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print('Nice to meet you, ' + username)
    return username

def greet_user():
    '''Greet the user by name'''
    username = get_stored_username()
    user_check = input('Is this ' + username + ' ? (y/n)')
    if user_check == 'n':
        new_user = get_new_username()
    else:
        if username:
            print('Welcome back, ' + username + '!')
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + '!')

greet_user()
