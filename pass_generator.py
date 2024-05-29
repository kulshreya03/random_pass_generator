import string
import random
import bcrypt
import logging

def generate_pass(len):

    #character set of all elements of password
    #all possible characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special_char = string.punctuation

    #combine all characters
    all_chars = lower+upper+digits+special_char

    #create pass ensuring at least one char from each
    password = [random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(special_char)]

    #fill remaining chars with random
    #k->no. of items
    password += ''.join(random.choices(all_chars,k=len-4))

    #shuffle for better randomness
    random.shuffle(password)

    #return as a string
    return ''.join(password)



#create a file to store hashed pass
file='hashed_pass.log'
logging.basicConfig(filename=file,filemode='a', level=logging.INFO, format='%(levelname)s - %(message)s - %(asctime)s')

len = int(input('Enter the length of pass>>'))
if len<8:
    print('Password should be atleast 8 characters long!!')
    logging.error('Less than 8') #log error in case of minimum length less than 8

else:
    password = generate_pass(len)
    print(f'Your randomly generated password is >>{password}')

    #store hashed in log
    pw = password
    hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
    logging.info(f'Hashed Passwrd>>{hashed}')
